# SOBEK - Directory & File Fuzzer 🐊

A fast, multi-threaded directory and file fuzzer written in Python.
Named after the Egyptian crocodile god — aggressive, cunning, and
relentless. Designed for penetration testers to discover hidden pages,
admin panels, backup files and exposed configurations on web servers.

## ⚠️ Disclaimer
This tool is intended for authorized penetration testing and educational
purposes only. Always obtain written permission before testing any target
you do not own. Unauthorized use is illegal and unethical.

## Features
- Multi-threaded scanning for fast fuzzing
- Detects 200, 301, 302 and 403 HTTP responses
- Saves discovered paths to an output file
- Handles URLs with and without trailing slashes
- Simple command-line interface

## Requirements
- Python 3.x
- requests

## Installation
git clone https://github.com/C0rmat/SOBEK-Directory-Fuzzer
cd SOBEK-Directory-Fuzzer
pip install requests

## Usage
python3 fuzzer.py --url https://example.com --wordlist wordlist.txt

## Arguments
--url        Target URL (e.g. https://example.com)
--wordlist   Path to your wordlist file
--threads    Number of threads (default: 10)
--output     Output file for results (default: results.txt)

## Example
python3 fuzzer.py --url https://example.com --wordlist common.txt --threads 20

## Wordlists
Recommended wordlists can be found in the SecLists repository:
https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content

## Pairs well with
APEP - Subdomain Enumerator: Use APEP first to find subdomains,
then run SOBEK against each one to discover hidden content.

## Author
C0rmat
