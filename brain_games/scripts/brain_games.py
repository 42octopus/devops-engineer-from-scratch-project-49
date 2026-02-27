import prompt

from brain_games.cli import welcome_user


def main():
	print("Welcome to the Brain Games!")
	name = prompt.string('May I have your name? ')
	welcome_user(name)


if __name__ == "__main__":
	main()
