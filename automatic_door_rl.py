import numpy as np

states = [0, 1]  # 0: No person, 1: Person near
actions = [0, 1, 2]  # Open, Close, Wait

R = [
    [-5, 5, 1],
    [10, -10, 2]
]

gamma = 0.9
policy = [0, 0]

def next_state(s, a):
    if s == 0:
        return 0 if a != 0 else 1
    else:
        return 1 if a != 1 else 0

def policy_evaluation(policy):
    V = [0, 0]
    for _ in range(10):
        for s in states:
            a = policy[s]
            ns = next_state(s, a)
            V[s] = R[s][a] + gamma * V[ns]
    return V

def policy_improvement(V):
    new_policy = [0, 0]
    for s in states:
        values = []
        for a in actions:
            ns = next_state(s, a)
            values.append(R[s][a] + gamma * V[ns])
        new_policy[s] = np.argmax(values)
    return new_policy

for i in range(10):
    V = policy_evaluation(policy)
    new_policy = policy_improvement(V)
    if new_policy == policy:
        break
    policy = new_policy

print("Optimal Policy:")
print("No Person:", ["Open", "Close", "Wait"][policy[0]])
print("Person Near:", ["Open", "Close", "Wait"][policy[1]])