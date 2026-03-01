import random

DESCRIPTION = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 2
MAX_STEP = 6


def generate_round():
    start = random.randint(MIN_START, MAX_START)  # NOSONAR python:S2245
    step = random.randint(MIN_STEP, MAX_STEP)  # NOSONAR python:S2245

    progression = [start + i * step for i in range(PROGRESSION_LENGTH)]

    hidden_index = random.randint(  # NOSONAR python:S2245
        MIN_START, PROGRESSION_LENGTH - 2
        ) 
    correct_answer = progression[hidden_index]

    progression_display = [
        '..' if i == hidden_index else str(num)
        for i, num in enumerate(progression)
    ]
    question = ' '.join(progression_display)

    return question, correct_answer