import random


def get_word():
    print("\n")
    print("Welcome to Hangman!\n")
    print("Want to play!\n")
    print("Choose between four themes: Cities, Sports, Movies or Cars")
    themes = ["cities", "sports", "cars", "movies"]
    while True:
        theme = input("What theme would you like to play: \n").lower()
        if theme in themes:
            break
        else:
            print(f"{theme} is not available. Try again!")
    if theme == "cities":
        words = "paris london tokyo rome dubai sydney".split()
    elif theme == "sports":
        words = "football basketball tennis swimming cycling".split()
    elif theme == "cars":
        words = "bmw ferrari lamborghini tesla audi".split()
    elif theme == "movies":
        words = "fargo godfather aladdin starwars".split()    
    number = random.randint(0, len(words)-1)
    word = list(words[number].upper())
    print("\n")
    print("What word do you think it is?")
    print("You can guess letters or words!")
    print("Guess wisely or the man will hang.")
    blank = "_"
    hidden_word = [blank]*len(word)
    return word, hidden_word