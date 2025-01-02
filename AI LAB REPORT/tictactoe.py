def calculate_heuristic(board, player, opponent):
    """
    Calculate the heuristic value for a given Tic-Tac-Toe board state.

    :param board: 2D list representing the Tic-Tac-Toe board (3x3).
    :param player: The player's symbol ('X' or 'O').
    :param opponent: The opponent's symbol ('X' or 'O').
    :return: Heuristic value.
    """
    def is_open_line(line, symbol):
        """Check if a line (row, column, or diagonal) is open for the given symbol."""
        return all(cell == symbol or cell == '' for cell in line)

    def count_open_lines(symbol):
        """Count the number of open lines for a given symbol."""
        open_lines = 0
        
        # Check rows and columns
        for i in range(3):
            if is_open_line([board[i][j] for j in range(3)], symbol):  # Row
                open_lines += 1
            if is_open_line([board[j][i] for j in range(3)], symbol):  # Column
                open_lines += 1
        
        # Check diagonals
        if is_open_line([board[i][i] for i in range(3)], symbol):  # Main diagonal
            open_lines += 1
        if is_open_line([board[i][2 - i] for i in range(3)], symbol):  # Anti-diagonal
            open_lines += 1
        
        return open_lines

    # Calculate heuristic value
    player_open_lines = count_open_lines(player)
    opponent_open_lines = count_open_lines(opponent)
    
    return player_open_lines - opponent_open_lines


# Example usage:
board = [
    ['X', '', ''],
    ['', 'X', ''],
    ['', '', '']
]
player = 'X'
opponent = 'O'

heuristic_value = calculate_heuristic(board, player, opponent)
print(f"Heuristic Value: {heuristic_value}")
