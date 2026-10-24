"""A simple two-player Tic-Tac-Toe game for the terminal."""


def print_board(board):
    """Display the board using positions 1 through 9 for empty squares."""
    cells = [mark if mark else str(index + 1) for index, mark in enumerate(board)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}")
    print()


def has_won(board, player):
    """Return True when the player has completed a row, column, or diagonal."""
    winning_lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    return any(all(board[index] == player for index in line) for line in winning_lines)


def play_game():
    """Run one complete game."""
    board = [""] * 9
    player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Choose a square by entering a number from 1 to 9, or enter q to quit.")

    while True:
        print_board(board)
        choice = input(f"Player {player}, choose a square (1-9): ").strip()

        if choice.lower() == "q":
            print("Game ended.")
            break

        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        square = int(choice) - 1
        if board[square]:
            print("That square is already taken. Choose another one.")
            continue

        board[square] = player

        if has_won(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if all(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    play_game()