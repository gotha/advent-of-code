data = [
    [71530, 940200],
]

data = [
    [47986698, 400121310111540],
]

result = 1
for [time, distance] in data:

    wins = 0
    for hold_time in range(1, distance-1):
        move_time = time - hold_time
        if move_time <= 0:
            break
        trial_distance = hold_time*move_time
        if trial_distance > distance:
            wins += wins

    result *= wins
print(result)
