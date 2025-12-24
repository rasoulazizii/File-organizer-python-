# Python File Organizer

A simple Python CLI tool to automatically organize files into folders by category.  
Supports optional extension filters and dry-run mode.

## Features

- Automatically sorts files into folders like `Images`, `Documents`, `Videos`, `Audio`, `Archives`, `Code`, `Executables`, and `Fonts`.
- Optional filtering: only organize files with specified extensions.
- Dry-run mode: preview actions without moving any files.
- Automatically renames files to avoid overwriting existing ones.
- Cross-platform (Windows, macOS, Linux).

## Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

## Optional: create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
## Usage

```bash
python organizer.py            # Organize all files in the current directory
python organizer.py .jpg .png  # Only organize files with .jpg and .png extensions
python organizer.py --dry      # Preview actions without moving files
python organizer.py .pdf --dry # Preview only PDF files

```

## Example

```bash
python organizer.py .jpg .png --dry
[DRY-RUN] Would move: photo1.jpg -> Images/photo1.jpg
[DRY-RUN] Would move: logo.png -> Images/logo.png

```