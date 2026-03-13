# RL Sensor Energy Optimization

This project demonstrates a simple Q-learning based strategy for smart agriculture sensors to optimize wake-up and sleep scheduling.

## Project Motivation
In smart agriculture, sensor nodes often operate under limited energy budgets. A well-designed control strategy can reduce unnecessary wake-ups and improve overall energy efficiency.

This project implements a simplified reinforcement learning framework that allows a sensor node to select among:
- sleep_short
- sleep_long
- wake_transmit

based on environmental change states:
- stable
- moderate
- large

## Features
- Q-learning based decision-making
- Simple sensor energy optimization simulation
- Custom reward design for wake/sleep policy
- Easy-to-understand project structure for portfolio use

## Technologies
- Python
- Q-learning
- NumPy

## File Structure
```text
rl-sensor-energy-optimization/
├─ main.py
├─ environment.py
├─ q_learning.py
├─ simulation.py
├─ requirements.txt
└─ README.md
