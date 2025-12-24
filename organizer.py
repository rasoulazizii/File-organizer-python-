from pathlib import Path
import shutil
import argparse

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".svg"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mpeg"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".xls", ".xlsx", ".csv", ".ppt", ".pptx"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "Executables": {".exe", ".msi", ".sh", ".bat", ".cmd", ".app"},
    "Code": {".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rs", ".php", ".rb", ".swift", ".kt"},
    "Fonts": {".ttf", ".otf", ".woff", ".woff2"}
}

DEFAULT_CATEGORY = "Others"

def get_category(ext):
    ext = ext.lower()
    for category, exts in CATEGORIES.items():
        if ext in exts:
            return category
    return DEFAULT_CATEGORY

def organize(base_dir=".", extensions=None, dry_run=False):
    base_dir = Path(base_dir)
    if extensions:
        extensions = set(ext.lower() for ext in extensions)

    for item in base_dir.iterdir():
        if not item.is_file() or item.name == Path(__file__).name:
            continue

        ext = item.suffix.lower()
        if extensions and ext not in extensions:
            continue

        category = get_category(ext)
        target_dir = base_dir / category
        target_dir.mkdir(exist_ok=True)
        dst = target_dir / item.name

        counter = 1
        while dst.exists():
            dst = target_dir / f"{item.stem}_{counter}{item.suffix}"
            counter += 1

        if dry_run:
            print(f"[DRY-RUN] Would move: {item.name} -> {dst}")
        else:
            shutil.move(item, dst)
            print(f"Moved: {item.name} -> {dst}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python File Organizer: Automatically sort files into folders by category."
    )
    parser.add_argument(
        "extensions",
        nargs="*",
        help="Optional list of file extensions to move (e.g., .jpg .png .pdf). Only these files will be organized."
    )
    parser.add_argument(
        "--dry", action="store_true", help="Perform a dry run without actually moving any files."
    )

    args = parser.parse_args()
    organize(extensions=args.extensions, dry_run=args.dry)
