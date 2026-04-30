
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. In this assignment, you will practice working with strings, loops, conditionals, and user input to create an interactive game.

## 📝 Tasks

### 🛠️	Set Up Game Data and State

#### Description
Create the core data and variables needed to run the Hangman game. Start with a word list, choose one word for the round, and initialize the values used to track guesses and remaining attempts.

#### Requirements
Completed program should:

- Include a predefined list of possible words.
- Select one word for the current game round.
- Create a structure to store guessed letters.
- Track the number of incorrect guesses the player has left.


### 🛠️	Implement the Game Loop

#### Description
Write the main game loop that asks the player for letter guesses, updates progress, and checks win or loss conditions. Show the current word state after each guess (for example, `_ _ a _ _`).

#### Requirements
Completed program should:

- Prompt the player to enter one letter at a time.
- Update and display the revealed letters after each guess.
- Decrease remaining attempts only for incorrect guesses.
- End with a clear win message when the word is guessed.
- End with a clear lose message when attempts reach zero.
