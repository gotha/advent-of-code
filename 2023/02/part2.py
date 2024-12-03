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
    line = line.split(":")[1]

    lineMaxColours = {}
    for c in colours:
        lineMaxColours[c] = 0

    for set in line.split(";"):
        for colour in colours:
            res = re.findall("([0-9]+) " + colour, set)
            if len(res) > 0:
                val = int(res[0])
                if val > lineMaxColours[colour]:
                    lineMaxColours[colour] = val

    setPower = 1
    for c in colours:
        setPower *= lineMaxColours[c]

    total += setPower

print(total)
