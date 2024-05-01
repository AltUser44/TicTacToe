![Screenshot 2024-05-01 040028](https://github.com/AltUser44/TicTacToe/assets/138399028/f514d761-9fb9-4b37-bbf2-df9ba300378d)

A Tic-Tac-Toe game with a colorful 3x3 matrix display.
'A' and 'B' represent the two players, using 'X' and 'O' as their respective pointers.
The game begins with the user (Player A) making the first move, and the computer (Player B) strategically
responding to either win the game or block Player A from winning.

-------------------------------------
The code implements ANSI escape codes for text color to add a vibrant touch to the game display.
After printing the colorful game grid, a function allows the user to place their pointer in a desired position.
The 'check_win' function determines all possible winning combinations and checks if the pointers are the same,
displaying an appropriate message when a player wins or when the game results in a draw.

------------------------------------

The code also implements Error handling for both the user and computer inputs, ensuring that only valid moves are accepted.
If an invalid move is attempted, the game prompts the user to try again, maintaining a smooth and engaging gameplay experience.
Upon completion of a game, the player is given the option to redo, resetting the game for another round.
