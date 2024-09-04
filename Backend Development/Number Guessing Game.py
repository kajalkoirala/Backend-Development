
import random

def num_guess():
    number = random.randint(1, 500)
    counts = 0

    print("Hey buddy! Welcome to the Game.")
    print("Can you guess the number between 1 and 500?")

    while True:
        counts += 1

        try:
            guess = int(input("Enter your guess: "))

            # Check if the guess is within the valid range
            if guess < 1 or guess > 1000:
                print("Please enter a number between 1 and 500.")
                continue  

            if guess < number:
                print("Sorry, it's a lower number. Try again.")
            elif guess > number:
                print("Sorry, it's a higher number. Try again.")
                
            else:
                print(f"Bravo! You've guessed {number} correctly in {counts} attempts.")
                break  

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    num_guess()
