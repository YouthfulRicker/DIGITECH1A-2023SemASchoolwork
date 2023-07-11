# Pseudocode Planning

This is the pseudocode for numbrguessr.py, which is the basic example of how the code will be implemented and formed. The pseudocode was made mostly by following [this guide](https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/).

## Changelog/Featurelist
Most of these changes were recommended to me by peers.
### Set 1
- The player is prompted to guess the number.
- If the player's guess is correct, they receive a success message and the game ends.
- If the player's guess is incorrect, they receive a failure message and can try again.
- The attempt count decreases by 1 after each guess.
- If the player runs out of attempts, a message is displayed with the correct number.

### Set 2
- The program includes additional validation for the player's guess.
- The player is prompted to enter a valid number between 1 and 100.
- Invalid guesses are handled with error messages.
- The player receives hints about whether the guess is too high or too low.
- The attempt count decreases by 1 after each valid guess.
- If the player runs out of attempts, a message is displayed with the correct number.

### Set 3
- The program is structured as a function called "start_game."
- The game is initiated by calling the "start_game" function.
- The player is prompted to guess the number and receives hints about the guess.
- The attempt count decreases by 1 after each valid guess.
- If the player runs out of attempts, a message is displayed with the correct number.
- After each game, the player is asked if they want to play again.
- If the player wants to play again, the "start_game" function is recursively called.
- If the player does not want to play again, a goodbye message is displayed.

### Set 4
- The program is now the same as set 3, only with a greeting added to comfort the player.