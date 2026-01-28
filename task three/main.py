import sys
from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    parts = line.strip().split()
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "info": " ".join(parts[3:])
    }

def load_logs(file_path: str) -> list:
    all_logs = []

    try:
        with open(file_path, 'r', encoding='utf-8') as fh:
            for line in fh:
                all_logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("File not found.")

    return all_logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log["level"] == level, logs))
    #return [log for log in logs if log.get("type") == level] - Isn't this better?

def count_logs_by_level(logs: list) -> dict:
    return Counter(log["level"] for log in logs)


def display_log_counts(counts: dict):
    TYPE_WIDTH = 17
    COUNT_WIDTH = 10
    print("Рівень логування | Кількість")
    print(f"{'-' * TYPE_WIDTH}|{'-' * COUNT_WIDTH}")

    for type, count in counts.items():
        print(f"{type:<{TYPE_WIDTH}}|{count}")


log_path = Path(sys.argv[1])
saved_logs = load_logs(str(log_path))
display_log_counts(count_logs_by_level(saved_logs))

if len(sys.argv) > 2:
    argument_two = sys.argv[2].upper()
    filtered_logs = filter_logs_by_level(saved_logs, argument_two)
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['info']}")
else:
    print("Error. Please enter correct log type!")
