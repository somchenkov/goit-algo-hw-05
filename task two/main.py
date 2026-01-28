import re

def generator_numbers(text: str):
    for char in re.finditer(r'\.?\d+', text):
        yield float(char.group(0))

def sum_profit(text, func):
    total = 0
    for number in func(text):
        total = total + number
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
