import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)  # NOSONAR python:S2245
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer