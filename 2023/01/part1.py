import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()


total = 0
for line in data.splitlines():
    firstDigit = None
    lastDigit = None

    for char in line:
        if char.isdigit():
            if firstDigit is None:
                firstDigit = char
                continue

            lastDigit = char

    if lastDigit is None:
        lastDigit = firstDigit

    num = int(str(firstDigit) + str(lastDigit))
    print("line: " + line + "; num:" + str(num))

    total = total + num

print("total:" + str(total))
