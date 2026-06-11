import csv
import random
import os
import sys

NUM_ROWS = 100


COLUMNS = ["ИМЯ", "ФАМИЛИЯ", "БАЛЛЫ_МАТЕМАТИКА", "БАЛЛЫ_РУССКИЙ"]

def generate_row():

    return {
        "ИМЯ": random.choice(["Тимофей", "Евгений", "Владимир", "Влад", "Пётр"]),
        "ФАМИЛИЯ": random.choice(["Карпов", "Климкин", "Иванов", "Гнидкинс", "Петров"]),
        "БАЛЛЫ_МАТЕМАТИКА": random.randint(27, 100),
        "БАЛЛЫ_РУССКИЙ": random.randint(27, 100),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

