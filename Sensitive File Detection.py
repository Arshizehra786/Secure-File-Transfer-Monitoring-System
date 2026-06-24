from pathlib import Path

SENSITIVE_FILES = [
    "salary.xlsx",
    "employee_data.csv",
    "passwords.txt",
]


def find_sensitive_files(root: str = ".") -> list[Path]:
    base_path = Path(root).expanduser().resolve()
    matches = []

    if not base_path.exists():
        raise FileNotFoundError(f"Directory not found: {base_path}")

    for path in base_path.rglob("*"):
        if path.is_file() and path.name.lower() in {name.lower() for name in SENSITIVE_FILES}:
            matches.append(path)

    return matches


if __name__ == "__main__":
    target_dir = input("Enter directory to scan (press Enter for current directory): ").strip() or "."
    try:
        matches = find_sensitive_files(target_dir)
    except FileNotFoundError as exc:
        print(exc)
    else:
        if matches:
            print("Sensitive files found:")
            for match in matches:
                print(match)
        else:
            print("No sensitive files found.")