import random


class SensorEnvironment:
    def __init__(self):
        self.states = ["stable", "moderate", "large"]
        self.actions = ["sleep_short", "sleep_long", "wake_transmit"]
        self.max_steps = 200
        self.reset()

    def reset(self):
        self.current_step = 0
        self.state = random.choice(self.states)
        return self.state

    def step(self, action: str):
        self.current_step += 1

        next_state = random.choices(
            self.states,
            weights=[0.5, 0.3, 0.2],
            k=1
        )[0]

        reward = self._get_reward(self.state, action, next_state)
        done = self.current_step >= self.max_steps
        self.state = next_state

        return next_state, reward, done

    def _get_reward(self, current_state: str, action: str, next_state: str) -> float:
        # 簡化版 reward 邏輯
        if current_state == "stable":
            if action in ["sleep_short", "sleep_long"]:
                return 2.0
            return -1.0

        if current_state == "moderate":
            if action == "sleep_short":
                return 1.0
            if action == "wake_transmit":
                return 1.5
            return -1.0

        if current_state == "large":
            if action == "wake_transmit":
                return 3.0
            return -2.0

        return 0.0
