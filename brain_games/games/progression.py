import random

DESCRIPTION = 'What number is missing in the progression?'


def generate_round():
    length = 10
    start = random.randint(1, 20)  # NOSONAR python:S2245
    step = random.randint(2, 6)  # NOSONAR python:S2245

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(1, length - 2)  # NOSONAR python:S2245
    correct_answer = progression[hidden_index]

    progression_display = [
        '..' if i == hidden_index else str(num)
        for i, num in enumerate(progression)
    ]
    question = ' '.join(progression_display)

    return question, correct_answer