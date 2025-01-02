import random

class PuzzleState:
    def __init__(self, board, heuristic_func, goal):
        """
        Initialize a puzzle state.
        :param board: 2D tuple representing the puzzle board.
        :param heuristic_func: Heuristic function to evaluate the state.
        :param goal: Goal state as a 2D tuple.
        """
        self.board = board
        self.goal = goal
        self.heuristic_func = heuristic_func
        self.heuristic_value = self.heuristic_func(self.board, self.goal)
        self.blank_pos = self.find_blank()

    def find_blank(self):
        """Find the position of the blank tile (0)."""
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)

    def possible_moves(self):
        """
        Generate all possible moves by sliding tiles.
        :return: List of new PuzzleState instances after making moves.
        """
        moves = []
        x, y = self.blank_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.board) and 0 <= ny < len(self.board[0]):  # Check bounds
                new_board = [list(row) for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                moves.append(PuzzleState(tuple(tuple(row) for row in new_board), self.heuristic_func, self.goal))
        return moves


def misplaced_tiles(board, goal):
    """Heuristic: Count the number of misplaced tiles."""
    return sum(board[i][j] != goal[i][j] and board[i][j] != 0 for i in range(3) for j in range(3))


def manhattan_distance(board, goal):
    """Heuristic: Calculate the total Manhattan distance."""
    distance = 0
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value != 0:  # Skip the blank tile
                goal_x, goal_y = [(x, y) for x, r in enumerate(goal) for y, v in enumerate(r) if v == value][0]
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


def steepest_ascent_hill_climbing(initial, goal, heuristic_func):
    """
    Solve the 8-puzzle problem using steepest ascent hill climbing.
    :param initial: Initial state as a 2D tuple.
    :param goal: Goal state as a 2D tuple.
    :param heuristic_func: Heuristic function to evaluate states.
    :return: Solution path and success status.
    """
    current_state = PuzzleState(initial, heuristic_func, goal)
    path = [current_state.board]

    while True:
        neighbors = current_state.possible_moves()
        best_neighbor = min(neighbors, key=lambda state: state.heuristic_value)

        # If no improvement, terminate
        if best_neighbor.heuristic_value >= current_state.heuristic_value:
            break

        # Move to the best neighbor
        current_state = best_neighbor
        path.append(current_state.board)

        # Check if goal is reached
        if current_state.heuristic_value == 0:
            return path, True

    return path, False


# Example: Define initial and goal states
initial_state = (
    (1, 2, 3),
    (4, 0, 5),
    (7, 8, 6)
)

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

# Solve the puzzle using both heuristics
path, success = steepest_ascent_hill_climbing(initial_state, goal_state, manhattan_distance)

# Print the result
if success:
    print("Solution found! Steps:")
    for step in path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found. Final state:")
    for row in path[-1]:
        print(row)
