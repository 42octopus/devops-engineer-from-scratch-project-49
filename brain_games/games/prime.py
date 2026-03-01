import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBER = 2
MAX_NUMBER = 100


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)  # NOSONAR python:S2245
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer