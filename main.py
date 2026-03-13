from simulation import run_simulation


def print_q_table(agent):
    print("Learned Q-table:")
    for state, actions in agent.q_table.items():
        print(f"\nState: {state}")
        for action, value in actions.items():
            print(f"  {action}: {value:.3f}")


def print_summary(rewards_history):
    print("\nTraining Summary")
    print("-" * 30)
    print(f"Total episodes: {len(rewards_history)}")
    print(f"Average reward: {sum(rewards_history) / len(rewards_history):.2f}")
    print(f"Max reward: {max(rewards_history):.2f}")
    print(f"Min reward: {min(rewards_history):.2f}")


if __name__ == "__main__":
    agent, rewards_history = run_simulation(episodes=300)
    print_q_table(agent)
    print_summary(rewards_history)
