import sys
from pathlib import Path
from collections import Counter

def store_logs(direction):
    all_logs = []
    try:
        fh = open(direction, 'r', encoding='utf-8')
        with fh:
            for line in fh:
                try:
                    parts = line.strip().split(' ')  # remove any spaces, split data with delimiter ','
                    log_info = {
                        "date": parts[0],
                        "time": parts[1],
                        "level": parts[2],
                        "info": " ".join(parts[3:])
                    }
                    all_logs.append(log_info)  # save information about each cat into cats_info

                except ValueError:
                    continue
            return all_logs
    except FileNotFoundError:
        print("File not found.")

def printing_logs(logs):
    TYPE_WIDTH = 17
    COUNT_WIDTH = 10

    counts = Counter(log["level"] for log in logs)

    print("Рівень логування | Кількість")
    print(f"{'-' * TYPE_WIDTH}|{'-' * COUNT_WIDTH}")

    for type, count in counts.items():
        print(f"{type:<{TYPE_WIDTH}}|{count}")


log_path = Path(sys.argv[1])
saved_logs = store_logs(log_path)

printing_logs(saved_logs)
if len(sys.argv) > 2:
    argument_two = sys.argv[2].upper()
    if any(log["level"] == argument_two for log in saved_logs):
        for log in saved_logs:
            if log["level"] == argument_two.upper():
                print(f"{log['date']} {log['time']} - {log['info']}")
    else:
        print("Error. Please enter correct log level!")