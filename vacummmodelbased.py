class ModelBasedVacuumAgent:
    def __init__(self):
        self.location = 'A'
        self.status = {'A': 'clean', 'B': 'clean'}
        self.environment_model = {'A': 'unknown', 'B': 'unknown'}

    def perceive(self):
        return self.location, self.status[self.location]

    def update_model(self, location, status):
        self.environment_model[location] = status

    def decide(self, location, status):
        if status == 'dirty':
            return 'Suck'
        if self.environment_model['A'] == 'dirty':
            return 'Left'
        if self.environment_model['B'] == 'dirty':
            return 'Right'
        if location == 'A':
            return 'Right'
        return 'Left'

    def act(self, action):
        if action == 'Suck':
            self.status[self.location] = 'clean'
        elif action == 'Right':
            self.location = 'B'
        elif action == 'Left':
            self.location = 'A'
        self.update_model(self.location, self.status[self.location])

    def run(self):
        for _ in range(10):
            location, status = self.perceive()
            self.update_model(location, status)
            action = self.decide(location, status)
            self.act(action)
            print(f"Location: {location}, Action: {action}, Status: {self.status}, Model: {self.environment_model}")

# Create and run the model-based vacuum agent
agent = ModelBasedVacuumAgent()
agent.status['A'] = 'dirty'
agent.run()
