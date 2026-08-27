import random

def simulate(seed, trials, treatment):
    rng = random.Random(seed)
    outcomes = []
    for _ in range(trials):
        draw = rng.random()
        if treatment == "a":
            outcomes.append(draw < 0.4)
        elif treatment == "b":
            outcomes.append(draw < 0.6)
        else:
            if rng.random() < 0.5:
                outcomes.append(draw < 0.4)
            else:
                outcomes.append(draw < 0.6)
    return outcomes
