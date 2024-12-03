import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
colour_max = {"red": 12, "green": 13, "blue": 14}

sumOfValids = 0
for line in f.read().splitlines():
    res = line.split(":")
    gameNumber = res[0].replace("Game ", "")
    sets = res[1].split(";")
    invalidSet = False
    for s in sets:
        items = list(s.split(","))
        for i in items:
            [_, num, colour] = i.split(" ")
            if int(num) > colour_max[colour]:
                invalidSet = True
                break
    if invalidSet:
        continue

    sumOfValids += int(gameNumber)

print(sumOfValids)
f.close()
