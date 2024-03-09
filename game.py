import os
import random


# ANSI escape codes for text color
FONT_PINK = '\033[95m'
FONT_NORMAL = '\033[0m'


# Function to print the Tic-Tac-Toe grid with color
def print_grid(grid):
   os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
   print(f"{FONT_PINK}Tic-Tac-Toe ❌➖➕➖➕➖⭕{FONT_NORMAL}")
   print(f' {grid[1]} | {grid[2]} | {grid[3]}')
   print('-----------')
   print(f' {grid[4]} | {grid[5]} | {grid[6]}')
   print('-----------')
   print(f' {grid[7]} | {grid[8]} | {grid[9]}')


# Function to check for a win
def check_win(grid, marker):
   # Check rows, columns, and diagonals for a win
   return ((grid[1] == grid[2] == grid[3] == marker) or
           (grid[4] == grid[5] == grid[6] == marker) or
           (grid[7] == grid[8] == grid[9] == marker) or
           (grid[1] == grid[4] == grid[7] == marker) or
           (grid[2] == grid[5] == grid[8] == marker) or
           (grid[3] == grid[6] == grid[9] == marker) or
           (grid[1] == grid[5] == grid[9] == marker) or
           (grid[3] == grid[5] == grid[7] == marker))


# Function to check for a tie
def check_tie(grid):
   return ' ' not in grid.values()


# Function to validate user input
def validate_input(input_str):
   try:
       position = int(input_str)
       if 1 <= position <= 9 and position == int(input_str):
           return position
       else:
           raise ValueError
   except ValueError:
       return None


# Function to get computer's move
def get_computer_move(grid):
   empty_positions = [pos for pos in grid if grid[pos] == ' ']
   return random.choice(empty_positions) if empty_positions else None


# Function to play the game with a computer opponent
def play_tic_tac_toe_with_computer():
   grid = {1: ' ', 2: ' ', 3: ' ',
           4: ' ', 5: ' ', 6: ' ',
           7: ' ', 8: ' ', 9: ' '}


   player = 'A'
   marker = 'X'
   computer_marker = 'O'


   while True:
       print_grid(grid)


       if player == 'A':
           input_str = input(f"Player {player}, choose a position (1-9): ")
           position = validate_input(input_str)


           if position and grid[position] == ' ':
               grid[position] = marker


               if check_win(grid, marker):
                   print_grid(grid)
                   print(f"\n{FONT_PINK}Player {player} wins!{FONT_NORMAL}")
                   break
               elif check_tie(grid):
                   print_grid(grid)
                   print(f"\n{FONT_PINK}It's a tie!{FONT_NORMAL}")
                   break
           else:
               print(f"\n{FONT_PINK}Sorry, that was incorrect. Try again!{FONT_NORMAL}")
               continue
       else:  # Computer's turn
           position = get_computer_move(grid)


           if position:
               grid[position] = computer_marker


               if check_win(grid, computer_marker):
                   print_grid(grid)
                   print(f"\n{FONT_PINK}Computer (Player B) wins!{FONT_NORMAL}")
                   break
               elif check_tie(grid):
                   print_grid(grid)
                   print(f"\n{FONT_PINK}It's a tie!{FONT_NORMAL}")
                   break


       player, marker = ('B', 'O') if player == 'A' else ('A', 'X')


   play_again = input("Do you want to play again? (yes/no): ")
   return play_again.lower() == 'yes'


# Main game loop
while True:
   if not play_tic_tac_toe_with_computer():
       break
