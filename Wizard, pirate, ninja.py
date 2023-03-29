import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (wizard, pirate, or ninja): ").lower()
        if user_choice in ["wizard", "pirate", "ninja"]:
            return user_choice
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    choices = ["wizard", "pirate", "ninja"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "wizard" and computer_choice == "pirate") or \
         (user_choice == "pirate" and computer_choice == "ninja") or \
         (user_choice == "ninja" and computer_choice == "wizard"):
        return "user"
    else:
        return "computer"

def explain_result(user_choice, computer_choice):
    if user_choice == "wizard" and computer_choice == "pirate":
        return "Wizard casts a spell on Pirate."
    elif user_choice == "pirate" and computer_choice == "ninja":
        return "Pirate shoots Ninja with a gun."
    elif user_choice == "ninja" and computer_choice == "wizard":
        return "Ninja uses stealth to defeat Wizard."
    elif computer_choice == "wizard" and user_choice == "pirate":
        return "Wizard casts a spell on Pirate."
    elif computer_choice == "pirate" and user_choice == "ninja":
        return "Pirate shoots Ninja with a gun."
    elif computer_choice == "ninja" and user_choice == "wizard":
        return "Ninja uses stealth to defeat Wizard."

def main():
    print("Wizard, Pirate, Ninja Game")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")

        winner = determine_winner(user_choice, computer_choice)
        explanation = explain_result(user_choice, computer_choice)
        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print(f"You win! {explanation}")
        else:
            print(f"Computer wins! {explanation}")

        play_again = input("Do you want to play again? (yes or no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
