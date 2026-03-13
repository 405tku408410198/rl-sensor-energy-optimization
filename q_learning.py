import random


class QLearningAgent:
    def __init__(self, states, actions, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.states = states
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        self.q_table = {
            state: {action: 0.0 for action in actions}
            for state in states
        }

    def choose_action(self, state: str) -> str:
        if random.random() < self.epsilon:
            return random.choice(self.actions)

        return max(self.q_table[state], key=self.q_table[state].get)

    def update(self, state: str, action: str, reward: float, next_state: str):
        current_q = self.q_table[state][action]
        next_max_q = max(self.q_table[next_state].values())

        new_q = current_q + self.alpha * (
            reward + self.gamma * next_max_q - current_q
        )
        self.q_table[state][action] = new_q
