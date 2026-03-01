import prompt

from brain_games.cli import welcome_user


def run_game(generate_round, description: str):
    name = welcome_user()
    print(description)

    for _ in range(3):
        question, correct_answer = generate_round()
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ').strip()

        if answer.lower() == str(correct_answer).lower():
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')