print("Welcome to hangman game!")

def get_letter():
    letter = input("Enter a letter: ")

    # Check if input is one character and alphabetical
    if len(letter) == 1 and letter.isalpha():
        return letter
    else:
        return False
