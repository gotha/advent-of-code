import re
import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

colours = ["red", "green", "blue"]

total = 0
for line in data.splitlines():
    res = re.findall('^Game ([0-9]+):', line)
    if len(res) < 1:
        raise Exception("Cannot determine game number")
    gameNumber = res[0]
    line = line[len("Game " + gameNumber) + 2:]
    print(line)

    lineMaxColours = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for set in line.split(";"):
        for colour in colours:
            res = re.findall("([0-9]+) " + colour, set)
            if len(res) > 0:
                val = int(res[0])
                if val > lineMaxColours[colour]:
                    lineMaxColours[colour] = val

    setPower = lineMaxColours["red"] * \
        lineMaxColours["blue"] * lineMaxColours["green"]

    total += setPower
    print("======================")

print(total)
