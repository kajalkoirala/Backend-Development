import random

def system_choice():
    system = ['scissor', 'paper', 'rock']
    return random.choice(system)

def users_choice():
    valid_choices = ['scissor', 'paper', 'rock']

    while True:
        users = input("Enter your choice (scissor, paper, rock): ").lower()

        if users not in valid_choices:
            print("Invalid choice! Please choose 'scissor', 'paper', or 'rock'.")
            continue
        
        system = system_choice()
        print(f"System chose: {system}")

        if (system == "scissor" and users == "paper") or \
           (system == "paper" and users == "rock") or \
           (system == "rock" and users == "scissor"):
            print("You lose!")
            return 'lose'
        elif system == users:
            print("It's a tie!")
            return 'tie'
        else:
            print("Congratulations, you win!")
            return 'win'

if __name__ == "__main__":
    win_count = 0
    lose_count = 0

    while True:
        result = users_choice()
        if result == 'win':
            win_count += 1
        elif result == 'lose':
            lose_count += 1

        again = input("Wanna play again? (Y/N): ").upper()
        if again == "Y":
            continue
        else:
            print(f"Thank you for playing. You won {win_count} times and lost {lose_count} times.")
            break
