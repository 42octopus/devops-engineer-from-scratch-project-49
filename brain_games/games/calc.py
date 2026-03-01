import random

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 25


def generate_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)  # NOSONAR python:S2245
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)  # NOSONAR python:S2245
    op = random.choice(['+', '-', '*'])  # NOSONAR python:S2245

    question = f'{num1} {op} {num2}'

    if '+' == op:
        correct = num1 + num2
    elif '-' == op:
        correct = num1 - num2
    else:
        correct = num1 * num2

    return question, correct