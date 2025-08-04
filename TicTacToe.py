import random

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check for a win
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Check if the board is full (Draw)
def is_draw(board):
    return all([cell != ' ' for row in board for cell in row])

# Get player's move
def player_move(board):
    while True:
        move = input("Enter your move (row and column from 1 to 3, e.g., 1 3): ")
        try:
            row, col = map(int, move.split())
            if board[row-1][col-1] == ' ':
                return (row-1, col-1)
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

# Computer's move
def computer_move(board):
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

# Main Game Loop
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's Move
        row, col = player_move(board)
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print("It's a Draw!")
            break

        # Computer's Move
        print("Computer's Turn:")
        row, col = computer_move(board)
        board[row][col] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("Computer Wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a Draw!")
            break

# Run the game
play_game()
