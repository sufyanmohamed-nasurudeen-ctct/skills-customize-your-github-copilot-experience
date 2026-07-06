
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic Hangman word-guessing game using Python. In this assignment, you will practice string handling, loops, conditionals, and user input validation while creating an interactive terminal game.

## 📝 Tasks

### 🛠️ Build Core Game Loop

#### Description
Create the main game flow that selects a random word, displays hidden progress, accepts guesses, and updates the game state after each turn.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Display the current word progress using underscores for unguessed letters (for example: `_ _ _ _`).
- Accept one letter guess at a time from the player.
- Reveal correctly guessed letters in all matching positions.

### 🛠️ Handle Win/Loss and Feedback

#### Description
Add game-ending conditions and clear player feedback so users know when they are close to winning or have run out of attempts.

#### Requirements
Completed program should:

- Track remaining incorrect guesses and reduce attempts only for wrong letters.
- Prevent duplicate guesses from incorrectly changing the game state.
- End the game with a win message when the full word is guessed.
- End the game with a loss message when attempts are exhausted and reveal the correct word.
