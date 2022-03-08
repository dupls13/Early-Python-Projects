import random

while True:
	user_choice = input("Please choose rock, paper, or scissors: ")
	computer_choice = random.choice(["rock", "paper", "scissors"])

	def play():
		if user_choice == computer_choice:
			return "It's a tie!"

		if player_win(user_choice,computer_choice):
			return "You win!"

		return "You lose!"


	def player_win(user_choice, computer_choice):
		if (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
			return True

	print(play())