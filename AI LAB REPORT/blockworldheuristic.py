def calculate_heuristic(start, goal):
    """
    Calculate the heuristic value for the Blocks World problem.

    :param start: List of lists representing the start state.
    :param goal: List of lists representing the goal state.
    :return: Heuristic value.
    """
    heuristic = 0

    for stack_index in range(len(start)):
        if stack_index < len(goal):  # Ensure the goal stack exists
            start_stack = start[stack_index]
            goal_stack = goal[stack_index]
            
            # Compare blocks in the same stack
            for i in range(min(len(start_stack), len(goal_stack))):
                if start_stack[i] == goal_stack[i]:
                    heuristic += 1  # Correct block in position
                else:
                    heuristic -= 1  # Incorrect block in position

            # Extra blocks in start stack are wrong
            if len(start_stack) > len(goal_stack):
                heuristic -= len(start_stack) - len(goal_stack)
    
    return heuristic


# Example usage:
start_state = [['A'], ['D', 'C', 'B']]  # Example start state
goal_state = [['D'], ['C', 'B', 'A']]   # Example goal state

heuristic_value = calculate_heuristic(start_state, goal_state)
print(f"Heuristic Value: {heuristic_value}")
