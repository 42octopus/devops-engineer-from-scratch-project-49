import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a: int, b: int) -> int:
    # """Euclidean algorithm"""
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    num1 = random.randint(1, 100)  # NOSONAR python:S2245
    num2 = random.randint(1, 100)  # NOSONAR python:S2245
    question = f'{num1} {num2}'
    correct_answer = gcd(num1, num2)
    return question, correct_answer