# Incremental Spell-Checking Script

This script performs spell-checking only on `*.md` and `*.ipynb` files that have been modified since the last generation of `spelling_report.md`.

## Requirements

```bash
pip install pyspellchecker
```

## Usage

Run the script from the repository root or from any directory:

```bash
python3 .github/scripts/incremental_spellcheck.py
```

## How It Works

1. **Detects Changed Files**: The script compares file modification timestamps with the `spelling_report.md` timestamp to identify which files have changed.

2. **Spell-Checks Only Changed Files**: Instead of checking all 63+ files in the repository, it only processes files that were modified after the last report generation.

3. **Updates Reports**: Generates updated versions of:
   - `.github/reports/spelling_report.md` - Detailed report with suggestions and line numbers
   - `.github/reports/flagged.txt` - Simple list of flagged words (one per line)

4. **Dictionary Checking**: Uses both English and Dutch dictionaries, and excludes words from `.github/dictionaries/wordlist.txt`.

## Example Output

```
============================================================
Incremental Spell-Checking Script
============================================================

Loading custom wordlist...
✓ Loaded 41 custom words

Finding changed files since last report...
✓ Found 2 changed file(s):
  - CursusIndex/intro.md
  - AnalogDesignTechniques/intro.md

Checking spelling in changed files...
[1/2] Checking CursusIndex/intro.md...
[2/2] Checking AnalogDesignTechniques/intro.md...

Generating updated report at .github/reports/spelling_report.md...
Generating updated flagged list at .github/reports/flagged.txt...

============================================================
✓ Done! Found 15 unique misspelled word(s) in changed files
  Report saved to: .github/reports/spelling_report.md
  Flagged words saved to: .github/reports/flagged.txt
============================================================
```

## Features

- **Efficient**: Only checks files that have actually changed
- **Smart Filtering**: Ignores code blocks, inline code, URLs, and file paths
- **Bilingual**: Checks against both English and Dutch dictionaries
- **Customizable**: Respects custom wordlist in `.github/dictionaries/wordlist.txt`
- **Comprehensive Output**: Provides both detailed report and simple word list

## When to Use

- After editing markdown documentation
- After modifying Jupyter notebook text cells
- Before committing documentation changes
- As part of a CI/CD pipeline to validate spelling

## Notes

- If no files have changed since the last report, the script will exit with a message indicating the report is up to date.
- The script uses file modification timestamps, so if you want to force a full check, simply touch the files you want to re-check or delete the `spelling_report.md` file.
