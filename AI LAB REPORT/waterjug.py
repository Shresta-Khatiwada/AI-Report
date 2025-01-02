from collections import deque

class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goalTest(self, current_state):
        """Check if the current state is the goal state."""
        return current_state == self.goal_state

    def successor(self, state):
        """Generate all possible successor states."""
        successors = []
        jug1, jug2 = state

        # Production rules
        # Fill jug1 (4L jug)
        if jug1 < 4:
            successors.append((4, jug2))
        # Fill jug2 (3L jug)
        if jug2 < 3:
            successors.append((jug1, 3))
        # Empty jug1
        if jug1 > 0:
            successors.append((0, jug2))
        # Empty jug2
        if jug2 > 0:
            successors.append((jug1, 0))
        # Pour water from jug1 to jug2
        if jug1 > 0 and jug2 < 3:
            transfer = min(jug1, 3 - jug2)
            successors.append((jug1 - transfer, jug2 + transfer))
        # Pour water from jug2 to jug1
        if jug2 > 0 and jug1 < 4:
            transfer = min(jug2, 4 - jug1)
            successors.append((jug1 + transfer, jug2 - transfer))

        return successors

    def bfs(self):
        """Breadth-First Search algorithm to find the solution."""
        open_list = deque()  # Queue for BFS
        closed_list = set()  # Visited states
        parent_map = {}  # Track parent of each state

        # Initialize
        open_list.append(self.initial_state)
        closed_list.add(self.initial_state)
        parent_map[self.initial_state] = None

        while open_list:
            current_state = open_list.popleft()

            # Check if goal state is reached
            if self.goalTest(current_state):
                return self.generate_path(parent_map, current_state)

            # Explore successors
            for successor in self.successor(current_state):
                if successor not in closed_list:
                    open_list.append(successor)
                    closed_list.add(successor)
                    parent_map[successor] = current_state

        return None  # No solution found

    def generate_path(self, parent_map, current_state):
        """Generate the solution path from the initial state to the goal state."""
        path = []
        while current_state:
            path.append(current_state)
            current_state = parent_map[current_state]
        path.reverse()
        return path


# Instantiate the WaterJug class
initial_state = (4, 0)  # 4-liter jug full, 3-liter jug empty
goal_state = (2, 0)     # Goal: 2 liters in 4-liter jug

water_jug_problem = WaterJug(initial_state, goal_state)

# Solve the problem using BFS
solution_path = water_jug_problem.bfs()

# Print the solution path
if solution_path:
    print("Solution found!")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")

   