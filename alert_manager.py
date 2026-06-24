from pathlib import Path


def generate_alert(message):
    print("SECURITY ALERT:", message)

    log_path = Path("logs/activity_log.txt")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"ALERT: {message}\n")


if __name__ == "__main__":
    message = input("Enter alert message: ").strip() or "No message provided"
    generate_alert(message)