import hashlib
from pathlib import Path


def calculate_hash(filepath):
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    sha256 = hashlib.sha256()

    with path.open("rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        target = input("Enter file path to hash: ").strip()

    try:
        print(calculate_hash(target))
    except (FileNotFoundError, ValueError) as exc:
        print(exc)