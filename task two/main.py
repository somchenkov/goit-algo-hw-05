import re

def generator_numbers(text: str):
    for char in re.finditer(r' \d+?\.\d+ ', text):
        yield float(char.group(0))

def sum_profit(text, func):
    total = 0
    for number in func(text):
        print(number)
        total = total + number
    return total


text = "20.12 or 12.28 . A2 333.1 and 2.9 or 0.2 and 2 or4.4 end 5.5."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
