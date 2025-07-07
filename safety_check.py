import csv
from datetime import datetime

fields = ["Supervisor", "Checklist", "Notes", "Timestamp"]

def log_check():
    supervisor = input("Supervisor name: ")
    checklist = input("Checklist passed? (Yes/No): ")
    notes = input("Additional notes: ")
    timestamp = datetime.now().isoformat()

    with open('safety_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([supervisor, checklist, notes, timestamp])

    print("Safety check logged.")

if __name__ == "__main__":
    log_check()
