import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize variables
player_x = "X"
player_o = "O"
current_player = player_x
game_board = [""] * 9

# Create a function to check for a win
def check_win(player):
    for combo in winning_combinations:
        if all([game_board[i] == player for i in combo]):
            return True
    return False

# Create a function to handle player's move
def make_move(button, index):
    if game_board[index] == "" and not check_win(current_player):
        game_board[index] = current_player
        button.config(text=current_player, state="disabled", disabledforeground="black")
        if check_win(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
        elif "" not in game_board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        else:
            toggle_player()

# Create a function to toggle players
def toggle_player():
    global current_player
    if current_player == player_x:
        current_player = player_o
    else:
        current_player = player_x

# Create buttons for the Tic-Tac-Toe grid
buttons = [tk.Button(root, text="", height=3, width=7, command=lambda index=i: make_move(buttons[index], index)) for i in range(9)]

# Define winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Grid layout for buttons
for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

root.mainloop()
