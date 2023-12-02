import re
import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

colour_max = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
colours = list(colour_max.keys())

games = {}

sumOfValids = 0
for line in data.splitlines():
    res = re.findall('^Game ([0-9]+):', line)
    if len(res) < 1:
        raise Exception("Cannot determine game number")
    gameNumber = res[0]
    line = line[len("Game " + gameNumber) + 2:]

    isLineValid = True
    for set in line.split(";"):
        isSetValid = True
        for colour in colours:
            res = re.findall("([0-9]+) " + colour, set)
            if len(res) > 0:
                if int(res[0]) > colour_max[colour]:
                    isSetValid = False
        if isSetValid is False:
            isLineValid = False

    if isLineValid:
        sumOfValids += int(gameNumber)
    print("num " + gameNumber + ": " + str(isLineValid))

print(sumOfValids)
