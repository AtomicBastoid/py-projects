"""
Welcome to WordCraft 🧩!!

@ Goal:
--> The player will be prompted with random number of characters (minimum of 6 characters).
--> Using those characters the player has to make as many word possible of minimum leght 3.
--> If the player cannot form anymore words they can exit using the "exit()" command.

This game is property of AtomicBastoid aka Eishal Keshwani.
"""

# Importing required libraries
from colorama import Fore, Style
import random
import confetti
import requests

# Setting global variables
username = str()
score = int()
usedWords = list()

# Setting global constants
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/" # append word to search in end

def main():
    """
    Define main logic and flow of the program calls appropirate functions.
    @ Parameters: None
    @ return: None
    """

    rules()
    get_username()

    chars = get_characters()
    print()
    print("Your Characters: ", end="")
    for char in chars:
        print(Fore.MAGENTA + Style.BRIGHT + char, end=" ")
    print('\n')
    inp = input("Enter your word: ")
    while inp != "exit()":
        if valid_characters(chars, inp) and valid_word(inp):
            update_score()
            update_usedWords(inp)
            print(Fore.GREEN + "✔ CORRECT")
        else:
            print(Fore.RED + "✘ Better luck next time...")
        
        inp = input("Enter your word: ")

    if score >= 10:
        confetti.confetti()
        
    print("\n" + Style.BRIGHT + Fore.MAGENTA + f"Your Score is: {score}")



    # End of main()

def get_username():
    '''
    Gets player username and store in global variable username
    '''
    global username
    username = input("Enter your username: ")

    # End get_username()

def rules():
    '''
    initialises a list of rules and print it one by one.
    '''
    rul_list = [
        "Welcome to AtomicBastoid's game: WordCraft 🧩!!",
        "Your mission should you choose to accept it.",
        "Is to create as many word from the provided characters.",
        "The same character can be used as many times in a word.",
        "However same word cannot be entered more than once.",
    ]
    for rul in rul_list:
        print(rul)
    print(Fore.YELLOW + "Once you are sure you have made all possible combinations.")
    print(Fore.RED + "Enter 'exit()' to end game.")
    print(Fore.RESET)

    # end rules()

def update_score():
    '''
    Updates global variable score.
    '''
    global score
    score += 1

    # end update_score

def update_usedWords(word):
    '''
    Upadtes the usedWords list 
    @ Parameter: str :str():Value to be appended to usedWords list. 
    '''
    global usedWords
    usedWords.append(word)

    # end update_usedWords

def get_characters():
    '''
    Generate a list of random characters.
    @ paramters: None
    @ return ['A', 'B', 'C', 'D']
    '''
    letters = list()
    num = random.randint(6, 10)
    letter = random.sample('abcdefghijklmnopqrstuvwxyz', k=num)
    return letter

    # end get_characters()


def valid_characters(opt, inp):
    '''
    Checks to see if the 'inp' is madeup of chars in 'opt'.
    Also checks that this answer has not been used before.
    @ Parameters:
    --> opt :list(): list of allowed char options
    --> inp :str(): the input the user has provided
    @ return Boolean() #True/False
    '''
    global usedWords
    
    for char in inp:
        if (char not in opt) or (inp in usedWords) or (len(inp) < 3):
            return False
    
    return True

    # end valid_characters()


def valid_word(inp):
    '''
    Checks if the word provided by the player is a valid english word. 
    Using the dictionary api.
    @ Parameters:
    --> inp :str(): the input the user has provided
    @ return Boolean() #True/False
    '''
    
    inp = str(inp).lower()
    url = API_URL + inp
    response = requests.get(url).json()
    
    if isinstance(response, dict) and "title" in response:
        return False
    else:
        return True









if __name__ == "__main__":
    main()