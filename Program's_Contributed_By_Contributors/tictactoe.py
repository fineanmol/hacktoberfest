import math
import random

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

def create_board():
    return [EMPTY] * 9

def print_board(board):
    # Displays board in 3x3 format with positions 1-9
    template = (
        f" {board[0]} | {board[1]} | {board[2]}       1 | 2 | 3\n"
        f"---+---+---     ---+---+---\n"
        f" {board[3]} | {board[4]} | {board[5]}       4 | 5 | 6\n"
        f"---+---+---     ---+---+---\n"
        f" {board[6]} | {board[7]} | {board[8]}       7 | 8 | 9\n"
    )
    print(template)

def available_moves(board):
    return [i for i, v in enumerate(board) if v == EMPTY]

def make_move(board, position, player):
    board[position] = player

def winner(board):
    # Returns PLAYER_X, PLAYER_O or None
    lines = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in lines:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None

def is_draw(board):
    return EMPTY not in board and winner(board) is None

def human_turn(board, player):
    moves = available_moves(board)
    while True:
        try:
            choice = input(f"Player {player}, enter cell (1-9): ").strip()
            pos = int(choice) - 1
            if pos in moves:
                make_move(board, pos, player)
                return
            else:
                print("Invalid move. Choose an empty cell between 1 and 9.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

def ai_turn(board, ai_player, human_player):
    # Perfect play using minimax
    best_score = -math.inf
    best_move = None
    for move in available_moves(board):
        board_copy = board[:]
        board_copy[move] = ai_player
        score = minimax(board_copy, False, ai_player, human_player)
        if score > best_score:
            best_score = score
            best_move = move
    make_move(board, best_move, ai_player)
    print(f"AI ({ai_player}) placed on {best_move + 1}")

def minimax(board, is_maximizing, ai_player, human_player):
    win = winner(board)
    if win == ai_player:
        return 1
    elif win == human_player:
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for move in available_moves(board):
            board[move] = ai_player
            val = minimax(board, False, ai_player, human_player)
            board[move] = EMPTY
            best = max(best, val)
        return best
    else:
        best = math.inf
        for move in available_moves(board):
            board[move] = human_player
            val = minimax(board, True, ai_player, human_player)
            board[move] = EMPTY
            best = min(best, val)
        return best

def choose_symbol():
    while True:
        sym = input("Choose your symbol (X goes first). Pick X or O: ").strip().upper()
        if sym in ("X", "O"):
            return sym
        print("Invalid choice. Enter X or O.")

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    mode = ""
    while mode not in ("1", "2"):
        mode = input("Choose mode: 1) Two-player  2) Play vs AI : ").strip()

    board = create_board()

    if mode == "1":
        current = PLAYER_X
        while True:
            print_board(board)
            human_turn(board, current)
            if winner(board):
                print_board(board)
                print(f"Player {winner(board)} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw.")
                break
            current = PLAYER_O if current == PLAYER_X else PLAYER_X

    else:
        human_symbol = choose_symbol()
        ai_symbol = PLAYER_O if human_symbol == PLAYER_X else PLAYER_X
        # If human chooses O, AI starts
        current = PLAYER_X  # X always goes first
        while True:
            print_board(board)
            if current == human_symbol:
                human_turn(board, human_symbol)
            else:
                # AI move
                ai_turn(board, ai_symbol, human_symbol)
            if winner(board):
                print_board(board)
                print(f"{winner(board)} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw.")
                break
            current = PLAYER_O if current == PLAYER_X else PLAYER_X

def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
