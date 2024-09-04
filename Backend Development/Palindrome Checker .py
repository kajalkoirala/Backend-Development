def user_input(word):
  
    removed_space = word.replace(" ", "").upper()

    
    return removed_space == removed_space[::-1]

def main():
    words = input("Enter the word: ")

    if user_input(words):
        print(f"'{words}' is a palindrome")
    else:
        print(f"'{words}' is not a palindrome")

if __name__ == "__main__":
    main()
