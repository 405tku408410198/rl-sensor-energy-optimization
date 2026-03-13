from environment import SensorEnvironment
from q_learning import QLearningAgent


def run_simulation(episodes=300):
    env = SensorEnvironment()
    agent = QLearningAgent(
        states=env.states,
        actions=env.actions,
        alpha=0.1,
        gamma=0.9,
        epsilon=0.2
    )

    rewards_history = []

    for episode in range(episodes):
        state = env.reset()
        done = False
        total_reward = 0.0

        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state)

            state = next_state
            total_reward += reward

        rewards_history.append(total_reward)

    return agent, rewards_history
