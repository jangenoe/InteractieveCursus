#!/usr/bin/env python3
"""
Incremental spell-checking script for markdown and Jupyter notebook files.
Only checks files that have changed since the last spelling report generation.
Checks against English and Dutch dictionaries, excluding custom wordlist.
"""

import os
import re
import json
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict

try:
    from spellchecker import SpellChecker
except ImportError:
    print("ERROR: pyspellchecker not installed. Run: pip install pyspellchecker")
    exit(1)

# Initialize spell checkers for English and Dutch
spell_en = SpellChecker(language='en')
spell_nl = SpellChecker(language='nl')

def load_wordlist(wordlist_path):
    """Load custom wordlist from file."""
    if not os.path.exists(wordlist_path):
        return set()
    
    with open(wordlist_path, 'r', encoding='utf-8') as f:
        words = set()
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if line and not line.startswith('#'):
                words.add(line.lower())
        return words

def extract_text_from_markdown(content):
    """Extract text from markdown, excluding code blocks, inline code, URLs, and paths."""
    # Remove code blocks (``` ... ```)
    content = re.sub(r'```[\s\S]*?```', '', content)
    
    # Remove inline code (`...`)
    content = re.sub(r'`[^`]+`', '', content)
    
    # Remove HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Remove URLs
    content = re.sub(r'https?://[^\s]+', '', content)
    content = re.sub(r'www\.[^\s]+', '', content)
    
    # Remove markdown links [text](url)
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove file paths (anything with / or \ and file extensions)
    content = re.sub(r'[^\s]*[/\\][^\s]*', '', content)
    content = re.sub(r'\b\w+\.\w+\b', '', content)
    
    # Remove markdown formatting
    content = re.sub(r'[#*_~]', '', content)
    
    return content

def extract_text_from_jupyter(content):
    """Extract text from Jupyter notebook, excluding code cells and outputs."""
    try:
        notebook = json.loads(content)
        text_parts = []
        
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = cell.get('source', [])
                if isinstance(source, list):
                    text = ''.join(source)
                else:
                    text = source
                text_parts.append(text)
        
        return extract_text_from_markdown('\n'.join(text_parts))
    except json.JSONDecodeError:
        return ""

def extract_words(text):
    """Extract individual words from text."""
    # Split on whitespace and punctuation
    words = re.findall(r'\b[a-zA-ZäëïöüÄËÏÖÜáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛ]+\b', text)
    return words

def check_spelling(word, custom_words):
    """Check if a word is correctly spelled in English or Dutch."""
    word_lower = word.lower()
    
    # Skip if in custom wordlist
    if word_lower in custom_words:
        return True, []
    
    # Skip very short words (likely acronyms or valid)
    if len(word) <= 2:
        return True, []
    
    # Skip if it's all uppercase (likely acronym)
    if word.isupper():
        return True, []
    
    # Skip if it contains numbers
    if re.search(r'\d', word):
        return True, []
    
    # Check in both dictionaries
    if word_lower in spell_en or word_lower in spell_nl:
        return True, []
    
    # Get suggestions from both dictionaries
    suggestions_en = list(spell_en.candidates(word_lower) or [])[:3]
    suggestions_nl = list(spell_nl.candidates(word_lower) or [])[:3]
    
    # Combine suggestions, removing duplicates
    all_suggestions = list(dict.fromkeys(suggestions_en + suggestions_nl))
    
    return False, all_suggestions[:5]

def process_file(filepath, custom_words, repo_root):
    """Process a single file and return misspelled words with locations."""
    misspellings = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract text based on file type
        if filepath.endswith('.ipynb'):
            text = extract_text_from_jupyter(content)
            lines = text.split('\n')
        else:
            text = extract_text_from_markdown(content)
            lines = text.split('\n')
        
        # Process line by line
        for line_num, line in enumerate(lines, 1):
            words = extract_words(line)
            seen_in_line = set()
            
            for word in words:
                if word.lower() not in seen_in_line:
                    is_correct, suggestions = check_spelling(word, custom_words)
                    if not is_correct:
                        rel_path = os.path.relpath(filepath, repo_root)
                        misspellings.append({
                            'file': rel_path,
                            'line': line_num,
                            'word': word,
                            'suggestions': suggestions
                        })
                        seen_in_line.add(word.lower())
    
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    
    return misspellings

def get_changed_files(repo_root, report_path):
    """Get list of *.md and *.ipynb files changed since the report was last modified."""
    changed_files = []
    
    if not os.path.exists(report_path):
        print(f"Report file {report_path} does not exist. Run full spell check first.")
        return []
    
    # Get the modification time of the report
    report_mtime = os.path.getmtime(report_path)
    
    # Find all markdown and Jupyter notebook files
    for ext in ['*.md', '*.ipynb']:
        for filepath in Path(repo_root).rglob(ext):
            # Skip .git directory
            if '.git' in str(filepath):
                continue
            
            # Check if file was modified after the report
            file_mtime = os.path.getmtime(filepath)
            if file_mtime > report_mtime:
                changed_files.append(filepath)
    
    return sorted(changed_files)

def load_existing_report(report_path):
    """Load existing misspellings from the report."""
    existing_misspellings = {}
    
    if not os.path.exists(report_path):
        return existing_misspellings
    
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse the report to extract existing misspellings per file
    current_word = None
    for line in content.split('\n'):
        if line.startswith('### `'):
            current_word = line.replace('### `', '').replace('`', '').strip()
        elif line.startswith('- `') and current_word:
            # Extract file path
            match = re.match(r'- `([^`]+)` \(line (\d+)\)', line)
            if match:
                filepath = match.group(1)
                if filepath not in existing_misspellings:
                    existing_misspellings[filepath] = set()
                existing_misspellings[filepath].add(current_word.lower())
    
    return existing_misspellings

def merge_results(old_misspellings, new_misspellings, changed_files, repo_root):
    """Merge old and new misspellings, updating only changed files."""
    # Convert changed_files to relative paths
    changed_rel_paths = set()
    for f in changed_files:
        changed_rel_paths.add(os.path.relpath(f, repo_root))
    
    # Start with old misspellings
    merged = []
    
    # Add back old misspellings for files that haven't changed
    for filepath, words in old_misspellings.items():
        if filepath not in changed_rel_paths:
            # Keep old entries (we'll need to reconstruct from report)
            pass
    
    # Add new misspellings
    merged.extend(new_misspellings)
    
    return merged

def generate_report(misspellings, checked_files, output_path):
    """Generate the spelling report."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Group by unique words
    word_occurrences = defaultdict(list)
    for m in misspellings:
        word_occurrences[m['word'].lower()].append(m)
    
    # Count unique misspelled words
    unique_count = len(word_occurrences)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Spelling Report\n\n")
        f.write(f"**Last updated:** {now}\n\n")
        f.write(f"**Total unique misspelled words:** {unique_count}\n\n")
        f.write(f"**Files checked:** {len(checked_files)}\n\n")
        
        if unique_count == 0:
            f.write("✅ No spelling issues found!\n\n")
        else:
            f.write("## Misspelled Words\n\n")
            
            # Sort words alphabetically
            for word in sorted(word_occurrences.keys()):
                occurrences = word_occurrences[word]
                f.write(f"### `{occurrences[0]['word']}`\n\n")
                
                # Show suggestions if available
                if occurrences[0]['suggestions']:
                    f.write(f"**Suggestions:** {', '.join(occurrences[0]['suggestions'])}\n\n")
                else:
                    f.write("**Suggestions:** (none available)\n\n")
                
                f.write("**Occurrences:**\n\n")
                for occ in occurrences:
                    f.write(f"- `{occ['file']}` (line {occ['line']})\n")
                f.write("\n")
        
        f.write("## Files Checked\n\n")
        for filepath in sorted(checked_files):
            f.write(f"- `{filepath}`\n")

def generate_flagged_txt(report_path, output_path):
    """Generate flagged.txt from the spelling report."""
    if not os.path.exists(report_path):
        return
    
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract all flagged words
    flagged_words = []
    for line in content.split('\n'):
        if line.startswith('### `'):
            word = line.replace('### `', '').replace('`', '').strip()
            flagged_words.append(word)
    
    # Write to flagged.txt
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in flagged_words:
            f.write(f"{word}\n")

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    wordlist_path = os.path.join(repo_root, '.github/dictionaries/wordlist.txt')
    report_path = os.path.join(repo_root, '.github/reports/spelling_report.md')
    flagged_path = os.path.join(repo_root, '.github/reports/flagged.txt')
    
    print("="*60)
    print("Incremental Spell-Checking Script")
    print("="*60)
    print()
    
    print("Loading custom wordlist...")
    custom_words = load_wordlist(wordlist_path)
    print(f"✓ Loaded {len(custom_words)} custom words")
    print()
    
    print("Finding changed files since last report...")
    changed_files = get_changed_files(repo_root, report_path)
    
    if not changed_files:
        print("✓ No files have changed since the last report generation.")
        print("  The spelling report is up to date.")
        return
    
    print(f"✓ Found {len(changed_files)} changed file(s):")
    for f in changed_files:
        rel_path = os.path.relpath(f, repo_root)
        print(f"  - {rel_path}")
    print()
    
    print("Checking spelling in changed files...")
    all_misspellings = []
    checked_files = []
    
    for i, filepath in enumerate(changed_files, 1):
        rel_path = os.path.relpath(filepath, repo_root)
        print(f"[{i}/{len(changed_files)}] Checking {rel_path}...")
        misspellings = process_file(str(filepath), custom_words, repo_root)
        all_misspellings.extend(misspellings)
        checked_files.append(rel_path)
    
    print()
    print(f"Generating updated report at {report_path}...")
    generate_report(all_misspellings, checked_files, report_path)
    
    print(f"Generating updated flagged list at {flagged_path}...")
    generate_flagged_txt(report_path, flagged_path)
    
    unique_words = len(set(m['word'].lower() for m in all_misspellings))
    print()
    print("="*60)
    print(f"✓ Done! Found {unique_words} unique misspelled word(s) in changed files")
    print(f"  Report saved to: {report_path}")
    print(f"  Flagged words saved to: {flagged_path}")
    print("="*60)

if __name__ == '__main__':
    main()
