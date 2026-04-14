# RL Automatic Door

## Description
This project implements a Reinforcement Learning model using Policy Iteration to control an automatic door.

## Problem Statement
The door must decide whether to:
- Open
- Close
- Wait

based on the presence of a person.

## States
- 0: No Person
- 1: Person Near

## Actions
- Open
- Close
- Wait

## Rewards
- Open when person → +10
- Close when no person → +5
- Wrong action → Negative reward

## Algorithm Used
Policy Iteration:
1. Policy Evaluation
2. Policy Improvement

## Result
Optimal policy learned:
- Open when person is near
- Close when no person

## Author
Your Name
