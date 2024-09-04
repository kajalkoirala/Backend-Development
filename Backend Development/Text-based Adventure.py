import random

def start_game():
    print("Welcome to Life is Unfair!")
    print("You have a chance to win a crazy huge gift!")
    print("But remember... life is unfair.")
    
    print("\nLet's begin with a simple question.")
    choice = input("How are you feeling today? (fine/notfine): ").lower()

    if choice == "fine":
        print("\nOh, you're feeling fine? That's wonderful!")
        print("But wait... life's unfair, right? You don't get the gift. Bye!")
        return
    elif choice == "notfine":
        print("\nYou're not fine? Well, that's unfortunate.")
        print("But hey, maybe today will be your lucky day! Let's continue...")
        offer_gift()
    else:
        print("\nThat's not even an option! Life doesn't have time for nonsense. You're out!")
        return

def offer_gift():
    print("\nAlright, you've made it this far. Let's talk about the gift.")
    print("I could give you something amazing, but...")
    
    choice = input("Do you think you deserve a gift? (yes/no): ").lower()

    if choice == "yes":
        print("\nConfidence! I like it. But you know what? Life is unfair. No gift for you!")
        check_luck()
    elif choice == "no":
        print("\nWow, humble and honest. But life's still unfair... let's see what happens next.")
        check_luck()
    else:
        print("\nInvalid response. Looks like life's unfair to those who can't make decisions. Goodbye!")
        return

def check_luck():
    print("\nLet's test your luck. Pick a number between 1 and 10.")
    
    try:
        user_number = int(input("Enter your number: "))
        lucky_number = random.randint(1, 10)

        if user_number == lucky_number:
            print(f"\nWow, you guessed it! The lucky number was {lucky_number}.")
            print("You should totally get a gift for that... but life's unfair, remember?")
            final_twist()
        else:
            print(f"\nOops! The lucky number was {lucky_number}, not {user_number}.")
            print("No worries, though. Life is unfair, so you wouldn't have gotten the gift anyway!")
            final_twist()
    except ValueError:
        print("\nThat's not a number! Life doesn't deal well with rule-breakers. You're out!")
        return

def final_twist():
    print("\nOkay, okay. You've been a good sport, so how about this?")
    print("I'm going to give you a gift. Yes, you heard me right!")

    gifts = [
        "A trip to the moon! (Just kidding, you'll have to settle for a poster of the moon.)",
        "A brand new sports car! (Actually, it's a toy car, but it's still cool, right?)",
        "A lifetime supply of chocolate! (By lifetime, I mean one bar. Enjoy!)",
        "An all-expense paid vacation! (In your imagination, of course.)",
        "A personal butler! (His name is 'Yourself', and he's been with you all along.)"
    ]

    gift = random.choice(gifts)
    print(f"\nCongratulations! You've won: {gift}")
    
    print("\nBut wait... what's this? Life just handed me a note...")
    print("It says: 'In this game, no one can be the winner.' So, you're out!")
    print("Sorry, life is unfair... but thanks for playing!")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    
    if play_again == 'y':
        print("\nLet's see if life is still unfair!")
        start_game()
    else:
        print("\nGreat to play with you... but remember, life is unfair. I'll be waiting!")

if __name__ == "__main__":
    start_game()
