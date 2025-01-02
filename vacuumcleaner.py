class ReflexVacuumAgent:
    def __init__(self):
        self.location = 'A'  # Initial location of the vacuum cleaner
        self.status = {'A': 'clean', 'B': 'clean'}  # Initial status of each location

    def perceive(self):
        return self.location, self.status[self.location]

    def decide(self, location, status):
        if status == 'dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'

    def act(self, action):
        if action == 'Suck':
            self.status[self.location] = 'clean'
        elif action == 'Right':
            self.location = 'B'
        elif action == 'Left':
            self.location = 'A'

    def run(self):
        for _ in range(10):  # Run the agent for 10 steps
            location, status = self.perceive()
            action = self.decide(location, status)
            self.act(action)
            print(f"Location: {location}, Action: {action}, Status: {self.status}")

# Create and run the reflex vacuum agent
agent = ReflexVacuumAgent()
agent.status['A'] = 'dirty'  # Initial dirt status
agent.run()
