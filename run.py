import random

import random

HANGMAN = ["""
            +------+
                   |
                   |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
                   |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
            |      |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|      |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
            |      |
                   |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
            |      |
           /       |
                   |
                   |
                 =====""", """
            +------+
            O      |
           /|\     |
            |      |
           / \     |
                   |
                   |
                 =====""", ]


def get_word():
    print("\nWelcome to Hangman!\n")
    print("Want to play?\n")
    print("Choose between four themes: Cities, Sports, Movies, or Cars.")
    
    themes = ["cities", "sports", "cars", "movies"]
    
    while True:
        theme = input("What theme would you like to play? ").lower()
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
    
    print("\nWhat word do you think it is?")
    print("You can guess letters or words!")
    print("Guess wisely or the man will hang.")
    
    blank = "_"
    hidden_word = [blank] * len(word)
    
    return word, hidden_word


def get_guess(word, hidden_word, tries):
    while True:
        print("\n")
        guess = input("Please make a guess: \n").upper()
        list_guess = list(guess)
        if validate_guess(list_guess, guess, word, hidden_word, tries):
            break
    if guess in word or list_guess == word:
        return guess, "correct"
    else:
        return guess, "fail"


def validate_guess(list_guess, guess, word, hidden_word, tries):
    try:
        if guess.isalpha():
            if len(list_guess) != len(word):
                if len(list_guess) != 1:
                    raise ValueError(
                        f'Your guess needs to contain 1 or {len(word)} letters'
                    )
            if len(list_guess) == 1:
                if guess in hidden_word or guess in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
            if len(list_guess) == len(word):
                if guess in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
        else:
            raise ValueError(
                "Your guess needs to contain letters only"
            )
    except ValueError as err:
        print(HANGMAN[len(tries)])
        print(' '.join(hidden_word) + "\n")
        print(f"Invalid input: {err}. Please try again!" + "\n")
        print("Failed guesses: "+(' '.join(tries)).upper())
        return False

    return True

def add_letter(guess, word, hidden_word):
    
    
    if list(guess) == word:
        return "win"
    else:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        if "_" in hidden_word:
            return hidden_word
        else:
            return "win"   

def collect_tries(tries, guess):
   
    tries.append(guess)
    if len(tries) == 6:
        return "loose"
    else:
        return tries


def end_game(saved, killed):
    
   
    if saved == 1:
        print("You have managed to save 1 man")
    else:
        print(f'You have managed to save {saved} men')
    if killed == 1:
        print("and kill 1 man.")
        print("\n")
    else:
        print(f'and kill {killed} men.')
        print("\n")
    while True:
        play = input("Try again? (Yes or No): \n")
        try:
            if play.lower().startswith('y') or play.lower().startswith('n'):
                break
            else:
                raise ValueError(
                    f'{play} is not a valid input'
                )
        except ValueError as err:
            print(f'{err}. Answer Yes or No!')

def main():
   
    saved = 0
    killed = 0
    while True:
        tries = []
        word, hidden_word = get_word()
        print(HANGMAN[len(tries)])
        print(' '.join(hidden_word))
        while True:
            guess, result = get_guess(word, hidden_word, tries)
            if result == "fail":
                result = collect_tries(tries, guess)
                if result == "loose":
                    print(HANGMAN[6] + "\n")
                    print("Nope! " + f'{guess} is not in the word.')
                    print("\n")
                    print("The word is: " + (' '.join(word)) + "\n")
                    print("No tries left...\n")
                    print("...the man is now hanged!\n")
                    killed += 1
                    break
                elif result == tries:
                    tries = result
                    print(HANGMAN[len(tries)])
                    print(' '.join(hidden_word) + "\n")
                    print("Nope! " + f'{guess} is not in the word.' + "\n")
                    print("Failed guesses: "+(' '.join(tries)).upper())
            elif result == "correct":
                result = add_letter(guess, word, hidden_word)
                if result == "win":
                    print(' '.join(word) + "\n")
                    word = ''.join(word)
                    print("Nice guess!")
                    print("Congratulations!\n")
                    print(f'{word} is the word' + "\n")
                    saved += 1
                    break
                elif result == hidden_word:
                    hidden_word = result
                    print(HANGMAN[len(tries)])
                    print(' '.join(hidden_word) + "\n")
                    print(f'Nice guess, {guess} is in the word.' + "\n")
                    if len(tries) > 0:
                        print("Failed guesses: "+(' '.join(tries)).upper())
        if end_game(saved, killed):
            break


main()                    

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

def get_guess(word, hidden_word, tries):
    while True:
        print("\n")
        guess = input("Please make a guess: \n").upper()
        list_guess = list(guess)
        if validate_guess(list_guess, guess, word, hidden_word, tries):
            break
    if guess in word or list_guess == word:
        return guess, "correct"
    else:
        return guess, "fail"


def validate_guess(list_guess, guess, word, hidden_word, tries):
    try:
        if guess.isalpha():
            if len(list_guess) != len(word):
                if len(list_guess) != 1:
                    raise ValueError(
                        f'Your guess needs to contain 1 or {len(word)} letters'
                    )
            if len(list_guess) == 1:
                if guess in hidden_word or guess in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
            if len(list_guess) == len(word):
                if guess in tries:
                    raise ValueError(
                        f'You already guessed for {guess}'
                    )
        else:
            raise ValueError(
                "Your guess needs to contain letters only"
            )
    except ValueError as err:
        print(HANGMAN[len(tries)])
        print(' '.join(hidden_word) + "\n")
        print(f"Invalid input: {err}. Please try again!" + "\n")
        print("Failed guesses: "+(' '.join(tries)).upper())
        return False

    return True

def add_letter(guess, word, hidden_word):
    
    
    if list(guess) == word:
        return "win"
    else:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        if "_" in hidden_word:
            return hidden_word
        else:
            return "win"   

def collect_tries(tries, guess):
   
    tries.append(guess)
    if len(tries) == 6:
        return "loose"
    else:
        return tries


def end_game(saved, killed):
    
   
    if saved == 1:
        print("You have managed to save 1 man")
    else:
        print(f'You have managed to save {saved} men')
    if killed == 1:
        print("and kill 1 man.")
        print("\n")
    else:
        print(f'and kill {killed} men.')
        print("\n")
    while True:
        play = input("Do you want to try again? (Yes or No): \n")
        try:
            if play.lower().startswith('y') or play.lower().startswith('n'):
                break
            else:
                raise ValueError(
                    f'{play} is not a valid input'
                )
        except ValueError as err:
            print(f'{err}. Please answer Yes or No!')

def main():
   
    saved = 0
    killed = 0
    while True:
        tries = []
        word, hidden_word = get_word()
        print(HANGMAN[len(tries)])
        print(' '.join(hidden_word))
        while True:
            guess, result = get_guess(word, hidden_word, tries)
            if result == "fail":
                result = collect_tries(tries, guess)
                if result == "loose":
                    print(HANGMAN[6] + "\n")
                    print("Nope! " + f'{guess} is not in the word.')
                    print("\n")
                    print("The word is: " + (' '.join(word)) + "\n")
                    print("No tries left...\n")
                    print("...the man is now hanged!\n")
                    killed += 1
                    break
                elif result == tries:
                    tries = result
                    print(HANGMAN[len(tries)])
                    print(' '.join(hidden_word) + "\n")
                    print("Nope! " + f'{guess} is not in the word.' + "\n")
                    print("Failed guesses: "+(' '.join(tries)).upper())
            elif result == "correct":
                result = add_letter(guess, word, hidden_word)
                if result == "win":
                    print(' '.join(word) + "\n")
                    word = ''.join(word)
                    print("Nice guess!")
                    print("Congratulations!\n")
                    print(f'{word} is the word' + "\n")
                    saved += 1
                    break
                elif result == hidden_word:
                    hidden_word = result
                    print(HANGMAN[len(tries)])
                    print(' '.join(hidden_word) + "\n")
                    print(f'Nice guess, {guess} is in the word.' + "\n")
                    if len(tries) > 0:
                        print("Failed guesses: "+(' '.join(tries)).upper())
        if end_game(saved, killed):
            break


main()                    