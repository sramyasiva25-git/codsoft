import random

def rock_paper_scissors():
    print("Welcome to Rock Paper Scissors Game")
    print("----------------------------------")

    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose one option:")
        print("rock")
        print("paper")
        print("scissors")

        user_choice = input("Enter your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        if user_choice == computer_choice:
            print("Result: It's a Tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("Result: You Win!")
            user_score += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("Result: You Win!")
            user_score += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("Result: You Win!")
            user_score += 1
        else:
            print("Result: Computer Wins!")
            computer_score += 1

        print("Score Board")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThank you for playing!")
            break

rock_paper_scissors()