import csv
from datetime import datetime
import os

def log_check():
    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)

    # File path to log inside /data
    file_path = 'data/safety_log.csv'

    # Prompt user for inputs
    supervisor = input("Supervisor name: ")
    checklist = input("Checklist passed? (Yes/No): ")
    notes = input("Additional notes: ")
    timestamp = datetime.now().isoformat()

    # Row to write
    row = [supervisor, checklist, notes, timestamp]

    # Write to CSV
    file_exists = os.path.exists(file_path)
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header only if file doesn't exist
        if not file_exists:
            writer.writerow(["Supervisor", "Checklist", "Notes", "Timestamp"])

        writer.writerow(row)

    print("\n Safety check logged!")
    print("Logged Entry:", row)

if __name__ == "__main__":
    log_check()
