import random

print("Welcome to Rock Paper Scissors!")
print("You are playing against an AI opponent.")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    ai = random.choice(choices)

    print("You chose:", player)
    print("AI chose:", ai)

    if player == ai:
        print("It's a tie!")

    elif (player == "rock" and ai == "scissors") or \
         (player == "paper" and ai == "rock") or \
         (player == "scissors" and ai == "paper"):
        print("You win!")

    else:
        print("AI wins!")

    play_again = input("\nPlay again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break