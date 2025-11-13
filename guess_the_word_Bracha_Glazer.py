"""
Pseudocode:
I wrote this before I coded and then changed around my functions as I coded so this does not fully line up with my actual code.
Thank you!

import random for choosing a word each round.

word_list = 20 words options.
wins = 0
losses = 0

def difficulty_level():
    while loop:
        try:
            prompt user for difficulty level as an integer
            if input is out of range:
                raise ValueError("out of range")
        except ValueError:
            reprompt
        if level one chosen:
            allowed_attempts = 10
        elif level two:
            allowed_attempts = 8
        elif level three:
            allowed_attempts = 6
        return allowed_attempts

def user_guess(allowed_attempts):
    word = random.choice word from list
    attempts = 0
    while attempts < allowed_attempts:
        letter_guessed = [empty list]
        try:
            prompt user for a letter
            if input is blank:
                raise ValueError
            elif input is two letters:
                raise ValueError
            elif input is non letter:
                raise ValueError
            elif input was already guessed:
                raise ValueError
        except ValueError as e:
            if str(e) == blank
                print("blank input")
            elif str(e) == one letter:
                print("one letter")
            elif str(e) == non letter
                print("non letter")
            elif str(e) == already guessed
                print("already guessed")
            else:
                print("invalid")
            continue
        attempts += 1
        letters_guessed.append(letter)
        return word

def result():
    for character in word:
            if character is in letters_guessed:
                print(character)
            else:
                complete = no
                print("_")
        print(attempts_allowed - attempts)
        print(sorted(letters_guessed))
        if complete is "no":
            continue
        else:
            complete = "yes"
            break
    if complete is "yes":
        wins += 1
    elif complete is "no":
        losses += 1

def play_again():
    while True:
        prompt user to play again
        if input is y:
            user_guess()
        elif input is n:
            break
        else:
            print("Invalid")
            continue
    print(wins and losses)

def main():
    allowed_attempts = difficulty_level():
    word = user_guess(allowed_attempts)
    result()
    play again()

Short Reflection:
I started by creating one main function where everything took place, but then I switched to many smaller functions.
As I was coding, I noticed that it was getting very complicated and needed to be broken up more.
I mainly validated input in loops in separate functions and reprompted on error, this kept it easy and neat.
After learning a bit more, I noticed that there are many ways my code could have been written a lot more sophisticated
and compact. If I spent more time I would go back and recode many parts, learning simpler habits and methods.

Thank you so much!
"""


import random


word_options = {
    "food":["apple", "banana", "cracker", "popcorn", "cheese", "watermelon", "avocado", "pasta", "burger", "sushi",
            "potato", "chicken", "chocolate", "cookie", "pineapple", "grapefruit", "walnut", "broccoli", "carrot", "grape"],
    "animals":["gorilla", "giraffe", "cheetah", "tiger", "elephant", "squirrel", "horse", "dog", "cat", "turtle",
               "chicken", "fish", "rooster", "turkey", "rhinoceros", "dolphin", "shark", "bunny", "racoon", "spider"],
    "random":["hello", "explain", "awesome","picture", "employee", "explore", "language", "joke", "business", "learn",
              "fabulous", "plate", "respect", "computer", "window", "tissue", "poster", "lamp", "document", "project"]
                }


def user_category():
    """In a while loop, asks user which category they want. (food/animals/random); reprompt on error.
    Randomly picks a word from the category chosen, in the dictionary.

    Returns:
        Randomly chosen word from chosen category in dictionary.
    """
    while True:
        category = input("Choose a category (food/animals/random): ").strip().lower()
        if category == "food":
            return random.choice(word_options["food"])  # random word picked from the food category
        elif category == "animals":
            return random.choice(word_options["animals"])  # random word picked from the animals category
        elif category == "random":
            return random.choice(word_options["random"])  # random word picked from the random category
        else:
            print("Invalid choice.")
            continue  # reprompt on error


def difficulty_level():
    """In a while loop, asks user which level they want to play (1-3); reprompt on error.
    Convert level to amount of attempts.

    Returns:
        Amount of attempts user will have in game.
    """
    while True:
        try:
            level = int(input("Which level? (1, 2, 3) "))
            if level < 1 or level > 3:
                raise ValueError("out of range")
        except ValueError as e:
            if str(e) == "out of range":
                print("Not an option, out of range.")
            else:
                print("Invalid number.")
            continue  # Reprompt on error.

        if level == 1:  # attempts are determined by the level chosen.
            allowed_attempts = 10
        elif level == 2:
            allowed_attempts = 8
        elif level == 3:
            allowed_attempts = 6
        return allowed_attempts


def valid_letter(letters_guessed):
    """In a while loop, ask user for one letter, reprompt on error.
    Args:
        letters_guessed - list of letters user has already entered
    Return:
         letter - valid letter user entered
    Notes:
         Reprompt if letter has been previously entered.
    """
    while True:
        print()
        try:
            letter = input("Guess a letter: ").strip().lower()
            if letter == "":  # if input is blank
                raise ValueError("blank")
            elif len(letter) > 1:  # if more than one character is entered
                raise ValueError("multiple letters")
            elif not letter.isalpha():  # if a character other than a letter is entered
                raise ValueError("not a letter")
            elif letter in letters_guessed:  # if letter has been previously guessed
                raise ValueError("already guessed")
            else:
                break
        except ValueError as e:
            if str(e) == "blank":
                print("No letter guessed.")
            elif str(e) == "multiple letters":
                print("Only one letter allowed.")
            elif str(e) == "not a letter":
                print("Only letters allowed.")
            elif str(e) == "already guessed":
                print("You already guessed this letter. Try another.")
            else:
                print("Invalid input.")
            continue
    return letter  # return valid input only


def word_revealed(word, letters_guessed):
    """Print the word with the correct letters guessed revealed and the other letters hidden with underscores.
    Args:
        word - randomly picked word from the word_option list provided
        letters_guessed - list of letters user has already entered
    """
    for character in word:  # Loop for each letter in word.
        if character in letters_guessed:  # if user guessed letter, reveal it.
            print(character, end="")
        else:  # Hide letters user hasn't guessed yet.
            print("_", end="")
            continue


def response(word, letters_guessed, allowed_attempts, attempts):
    """Print the letters the user guessed.
    If user guessed all letters, print win message. Otherwise, print attempts remaining.
    Args:
        word - randomly picked word from the word_option list provided
        letters_guessed - list of letters user has already entered
        allowed_attempts - amount of tries user has to guess letters, determined by the game level chosen
        attempts - how many tries the user used
    Return:
        status - if user won
    Notes:
        if user did not yet win, print statements indicating attempts remaining instead of a return.
    """
    if not any(character not in letters_guessed for character in word):  # if user guessed all the letters in the word
        print()
        print(f"Letters guessed: {sorted(letters_guessed)}")  # print a sorted list of all the letters guessed
        print("You won!")
        status = "won"
        return status
    else:
        print()
        print(f"{allowed_attempts - attempts} attempt(s) remaining.")
        print(f"Letters guessed: {sorted(letters_guessed)}")


def play_again(wins, losses):
    """In a while loop, ask user if they want to play again. If yes, call user_guess(wins,losses).
    Args:
        wins - how many times the user guessed all letters in the word
        losses - how many times the user used all attempts before guessing the word correctly
    Return:
        wins - how many times the user guessed all letters in the word
        losses - how many times the user used all attempts before guessing the word correctly
    """
    while True:
        print()
        again = input("Do you want to play again? (y/n) ").strip().lower()
        if again == "y":
            wins, losses = user_guess(wins, losses)  # call to generate a new round, with a new word
        elif again == "n":
            return wins, losses
        else:
            print("Invalid")
            continue


def user_guess(wins, losses):
    """Call the category function to generate a word and the level function to determine amount of attempts allowed.
     In a while loop, call functions necessary for user to guess letters and the program to print the results.
     While loop runs until attempt exhausted.
    Args:
        wins - how many times the user guessed all letters in the word
        losses - how many times the user used all attempts before guessing the word correctly
    Return:
        wins - how many times the user guessed all letters in the word
        losses - how many times the user used all attempts before guessing the word correctly
    """
    word = user_category()  # Unpack the word chosen.
    allowed_attempts = difficulty_level()  # Attempts allowed is determined by the difficulty level chosen by the user.
    attempts = 0
    letters_guessed = []

    while attempts < allowed_attempts:  # Loop runs until attempts exhausted.
        #attempts = user_hint(attempts, word, letters_guessed)
        letter = valid_letter(letters_guessed)  # Call function to prompt user for input.
        letters_guessed.append(letter)  # Add letter to list of letters guessed.
        #attempts = user_hint(attempts)
        word_revealed(word, letters_guessed)  # Call function to print updated word with revealed and hidden letters.
        if letter not in word:  # if user guessed incorrectly.
            attempts += 1
        status = response(word, letters_guessed, allowed_attempts, attempts)
        if status == "won":
            wins += 1
            return wins, losses
    print("You lost!")
    print(f"The word was '{word}'.")
    losses += 1
    return wins, losses


def main():
    """Prompt user, run game, and print scores."""
    wins = 0
    losses = 0
    print("Welcome to 'Guess the Word'!")
    wins, losses = user_guess(wins, losses)
    wins, losses = play_again(wins, losses)
    print(f" wins: {wins} losses: {losses}")


if __name__ == "__main__":
    main()
