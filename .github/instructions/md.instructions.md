---
applyTo: '**/*.md, **/*.ipynb'
description: Markdown style and spelling guidelines for consistency across documentation.
---

# Markdown Style and spellingGuidelines

This document defines the Markdown style guidelines for all Markdown and jupyter notebook files in this repository. 

- find all words in the markdown text of the markdown files and jupyter notebook files that are not in the English dictionary nor in the Dutch dictionary
- ignore words in wordlists provided in the folder '.github/dictionaries/'
- ignore code blocks, inline code, URLs, and file paths
- ignore proper nouns, technical terms, and acronyms specific to the project
- provide suggestions for spelling corrections based on the closest matching words in the Dutch and English dictionaries
- save the list of identified words along with their suggested corrections in a separate report file in the folder '.github/reports/' named 'spelling_report.md'. Identify the file and line number (or cell number for jupyter notebooks) where each word was found. Also report the total number of unique misspelled words found across all files and the most recent date and time when the spell-checking was performed. Also provide a list of all files that were checked.
- if files are added or modified, re-run the spell-checking process only on those files. If files are deleted, remove any related entries from the report file. 
- do not make changes to the original markdown or jupyter notebook files

Ensure that the spell-checking process is efficient and can handle large files without significant performance degradation.