import matplotlib.pyplot as plt
from simulation import run_simulation


def plot_rewards(rewards):
    plt.figure(figsize=(8,5))
    plt.plot(rewards, label="Episode reward")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.title("RL Training Reward Curve")
    plt.legend()
    plt.grid(True)
    plt.savefig("reward_curve.png")
    plt.show()


if __name__ == "__main__":
    agent, rewards = run_simulation(episodes=300)
    plot_rewards(rewards)
