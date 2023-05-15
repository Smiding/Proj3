# HANGMAN
Hangman is a Python terminal game that can be played on the Code Institute mock terminal hosted on Heroku.

The objective of the game is to guess a hidden word. A hangman figure will be gradually built with each incorrect guess. Your task is to uncover the word before the hangman is completely formed. Good luck!


## How to play
The game "Hangman" is a Python terminal game inspired by the classic game called Hangman.

At the beginning of the game, the player selects a theme for the hidden word they will be guessing.

The player then proceeds to make guesses in order to uncover the word. Guesses can be made for either the full word or individual letters. If the guessed letter or word is not present in the hidden word, a symbol representing a part of the hanged man will be displayed.

If the guessed letter is correct and exists in the word, it will be revealed, making it easier for the player to deduce the word.

The game continues until either the player correctly guesses all the letters in the word, resulting in a win where the man is not hanged, or the player reaches 6 incorrect guesses, at which point the hangman image is fully displayed and the game is lost.

## Features

Display Images: The game will display hangman images representing the number of incorrect guesses made by the player.

Display Underscores as "Hidden Word": The game will display underscores to represent the letters of the word that the player needs to guess.


IMG 

Accept User Input: The game will accept user input for choosing themes and making guesses.

Choose Theme: The player can choose a theme from a list of available themes. Each theme has a set of words associated with it.

Make Guesses: The player can guess letters to uncover the hidden word. The game will provide feedback on whether the guess is correct or incorrect.

Play Again: After a game ends, the player can choose to play again. The game will reset and start a new round.

Maintain Scores: The game will maintain scores to keep track of the player's wins and losses.


IMG 

Random Word Generation: The game will generate a random word from the chosen theme for each round.

Maintain Tries: The game will keep track of the number of tries the player has made.

Maintain Correct Guesses: The game will keep track of the correct guesses made by the player and update the display accordingly.


IMG

Input Validation and Error Checking: The game will validate user input to ensure it meets certain criteria. It will check for duplicate guesses, disallowed symbols, and words that are not the same length as the hidden word.

Play Again Input Restrictions: When asked to play again, the player can only respond with words that start with 'y' or 'n'.


## Testing
- I have manually tested this project by doing this:

- Passing the code through the PEP8 linter.
- Testing in gitpod terminal and Code Institute Heroku terminal.
- Let different users on different screens test the game on Code Institute Heroku terminal.

## Validator testing
- No errors were found when passing through PEP8 Validator

## Deployment
- This project was deployed using Code Institutes mock terminal for Heroku.

- Deployment at regular intervals:
  - I used command git add filename to add the various files into it.
  - Then i committed to local repo with command git commit -m "useful string info".
  - Then finally uploaded it to my GitHub repo with git push.
- Final deployment in Heroku:
  - Fork github repository.
  - Create new Heroku app.
  - Set the buildbacks to Python and NodeJS in that order.
  - Link the Heroku app to the repository.
  - Enable automatic deployment.
  - Click on Deploy.

  Deployment
This project was deployed using Code Institutes mock terminal for Heroku.

## Credits
Code Institute for the deployment terminal.

Inspiration:
- [Youtube tutorial.] https://www.youtube.com/watch?v=m4nEnsavl6w
- [This code.] [Youtube turtorial.]

Help:
Jessica Rydberg

