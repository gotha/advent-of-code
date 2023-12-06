data = [
    [7, 9],
    [15, 40],
    [30, 200],
]

data = [
    [47, 400],
    [98, 1213],
    [66, 1011],
    [98, 1540],
]


result = 1
for [time, distance] in data:

    wins = []
    for hold_time in range(1, distance-1):
        move_time = time - hold_time
        if move_time <= 0:
            continue
        trial_distance = hold_time*move_time
        if trial_distance > distance:
            wins.append(hold_time)

    result *= len(wins)
print(result)
