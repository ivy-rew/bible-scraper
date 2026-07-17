# BibleScraper
Web scraper for BibleGateway

## Installation

This project requires Python 3 and the following dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Command

```bash
python3 main.py <book> <chapter> <verse>
```

### Arguments

- `<book>`: Bible book name (e.g., "john", "genesis", "psalms")
- `<chapter>`: Chapter number (e.g., "1", "3", "23")
- `<verse>`: Verse number (e.g., "16", "1", "45")

### Examples

**Basic usage with all arguments:**
```bash
python3 main.py john 3 16
```

**Interactive mode (no arguments):**
```bash
python3 main.py
```
This will prompt you for:
- Book name
- Chapter number
- Verse number

**HTML output mode:**
```bash
bibleAgent=html python3 main.py john 3 16
```

