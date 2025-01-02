import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        """
        Initialize a puzzle state.
        :param board: 2D tuple representing the puzzle board.
        :param moves: Number of moves taken to reach this state.
        :param previous: Reference to the previous PuzzleState.
        """
        self.board = board
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.find_blank()  # Locate the blank tile (0)

    def find_blank(self):
        """Find the position of the blank tile (0)."""
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)

    def manhattan_distance(self, goal):
        """
        Calculate the Manhattan distance heuristic.
        :param goal: Goal state as a 2D tuple.
        :return: Total Manhattan distance of the board from the goal state.
        """
        distance = 0
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value != 0:  # Skip the blank tile
                    goal_x, goal_y = [(x, y) for x, row in enumerate(goal) for y, v in enumerate(row) if v == value][0]
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def possible_moves(self):
        """
        Generate possible moves by sliding tiles.
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
                moves.append(PuzzleState(tuple(tuple(row) for row in new_board), self.moves + 1, self))
        return moves

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __lt__(self, other):
        return self.board < other.board  # For priority queue ordering


def a_star(initial, goal):
    """
    Solve the 8-puzzle problem using the A* algorithm.
    :param initial: Initial state as a 2D tuple.
    :param goal: Goal state as a 2D tuple.
    :return: List of moves to reach the goal state.
    """
    open_list = []
    closed_set = set()

    # Initialize the starting state
    start_state = PuzzleState(initial)
    heapq.heappush(open_list, (start_state.manhattan_distance(goal) + start_state.moves, start_state))

    while open_list:
        _, current_state = heapq.heappop(open_list)

        if current_state.board == goal:
            return reconstruct_path(current_state)

        closed_set.add(current_state)

        for neighbor in current_state.possible_moves():
            if neighbor in closed_set:
                continue

            cost = neighbor.moves + neighbor.manhattan_distance(goal)
            heapq.heappush(open_list, (cost, neighbor))

    return None  # No solution


def reconstruct_path(state):
    """
    Reconstruct the path from the initial state to the goal state.
    :param state: Final PuzzleState.
    :return: List of boards representing the path.
    """
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    path.reverse()
    return path


# Example: Define the initial and goal states
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

# Solve the puzzle
solution_path = a_star(initial_state, goal_state)

# Print the solution path
if solution_path:
    print("Solution found! Steps:")
    for step in solution_path:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
