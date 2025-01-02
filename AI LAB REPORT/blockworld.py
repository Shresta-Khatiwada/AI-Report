from collections import deque

class BlockWorld:
    def __init__(self, initial_state, goal_state):
        """
        Initializes the Block World problem.
        :param initial_state: Tuple of stacks representing the initial state.
        :param goal_state: Tuple of stacks representing the goal state.
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def goal_test(self, state):
        """Check if the current state matches the goal state."""
        return state == self.goal_state

    def successor(self, state):
        """
        Generate all possible successor states by moving one block at a time.
        :param state: Current state represented as a tuple of stacks.
        :return: List of successor states.
        """
        successors = []
        n = len(state)  # Number of stacks (including table)

        # Iterate over each stack and generate moves
        for i in range(n):
            if state[i]:  # If stack `i` is not empty
                # Remove the top block from stack `i`
                new_state = [list(stack) for stack in state]  # Create a deep copy
                block = new_state[i].pop()

                for j in range(n):  # Move the block to each other stack
                    if i != j:  # Avoid moving to the same stack
                        new_stack_state = [list(stack) for stack in new_state]
                        new_stack_state[j].append(block)  # Add block to stack `j`
                        successors.append(tuple(tuple(stack) for stack in new_stack_state))

        return successors

    def bfs(self):
        """
        Perform BFS to find the solution.
        :return: List of states representing the solution path.
        """
        open_list = deque()  # BFS queue
        closed_list = set()  # Visited states
        parent_map = {}  # Track parent states

        # Initialize BFS
        initial_state = tuple(tuple(stack) for stack in self.initial_state)
        open_list.append(initial_state)
        closed_list.add(initial_state)
        parent_map[initial_state] = None

        while open_list:
            current_state = open_list.popleft()

            # Check if the goal state is reached
            if self.goal_test(current_state):
                return self.generate_path(parent_map, current_state)

            # Generate and explore successors
            for successor in self.successor(current_state):
                if successor not in closed_list:
                    open_list.append(successor)
                    closed_list.add(successor)
                    parent_map[successor] = current_state

        return None  # No solution found

    def generate_path(self, parent_map, current_state):
        """
        Generate the solution path from the initial state to the goal state.
        :param parent_map: Dictionary mapping states to their parents.
        :param current_state: Current state (goal state).
        :return: List of states representing the solution path.
        """
        path = []
        while current_state:
            path.append(current_state)
            current_state = parent_map[current_state]
        path.reverse()
        return path


# Example: Define initial and goal states
initial_state = (('A', 'B'), ('C',), ())  # Three stacks: A and B in one, C in another, one empty
goal_state = (('B',), ('A', 'C'), ())    # Move blocks to achieve goal configuration

# Solve the Block World problem
block_world = BlockWorld(initial_state, goal_state)
solution_path = block_world.bfs()

# Print the solution path
if solution_path:
    print("Solution found!")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")

