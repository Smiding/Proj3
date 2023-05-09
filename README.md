# HANGMAN
Hangman is a Python terminal game that can be played on the Code Institute mock terminal hosted on Heroku.

The objective of the game is to guess a hidden word. A hangman figure will be gradually built with each incorrect guess. Your task is to uncover the word before the hangman is completely formed. Good luck!


## How to play
The game "Hangman" is a Python terminal game inspired by the classic game called Hangman.

At the beginning of the game, the player selects a theme for the hidden word they will be guessing.

The player then proceeds to make guesses in order to uncover the word. Guesses can be made for either the full word or individual letters. If the guessed letter or word is not present in the hidden word, a symbol representing a part of the hanged man will be displayed.

If the guessed letter is correct and exists in the word, it will be revealed, making it easier for the player to deduce the word.

The game continues until either the player correctly guesses all the letters in the word, resulting in a win where the man is not hanged, or the player reaches 6 incorrect guesses, at which point the hangman image is fully displayed and the game is lost.