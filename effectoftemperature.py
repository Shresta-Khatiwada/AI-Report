import math
import random
import matplotlib.pyplot as plt


def simulated_annealing_demo(start_energy, inferior_energy, initial_temp, cooling_rate):
    """
    Demonstrates the effect of temperature on the probability of accepting an inferior node.
    
    :param start_energy: Energy of the current (better) state.
    :param inferior_energy: Energy of the inferior (worse) state.
    :param initial_temp: Initial temperature for the simulation.
    :param cooling_rate: Cooling rate to reduce the temperature.
    """
    temperatures = []
    probabilities = []

    # Initialize temperature
    temp = initial_temp

    while temp > 0.01:
        # Calculate the probability of accepting the inferior state
        delta_energy = inferior_energy - start_energy
        probability = math.exp(-delta_energy / temp)

        # Store temperature and probability for plotting
        temperatures.append(temp)
        probabilities.append(probability)

        # Reduce the temperature
        temp *= cooling_rate

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(temperatures, probabilities, marker="o")
    plt.title("Effect of Temperature on Probability of Choosing an Inferior Node")
    plt.xlabel("Temperature")
    plt.ylabel("Probability of Choosing Inferior Node")
    plt.grid()
    plt.show()


# Parameters
start_energy = 10  # Energy of the current state
inferior_energy = 15  # Energy of the inferior state (higher energy)
initial_temp = 100  # Initial temperature
cooling_rate = 0.95  # Cooling rate

# Run the simulation
simulated_annealing_demo(start_energy, inferior_energy, initial_temp, cooling_rate)
