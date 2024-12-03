import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

num_names = list(numbers.keys())

total = 0
for line in data.splitlines():
    firstDigit = None
    lastDigit = None

    buff = ""
    for char in line:
        if char.isalpha():
            buff = buff+char

            # exact match
            if buff in num_names:
                val = numbers[buff]
                if firstDigit is None:
                    firstDigit = val
                    buff = ""
                lastDigit = val
                continue

            # matching part of str (works but I am not really confident it is the best way to do it)
            num_chars = len(buff)
            for i in range(1, num_chars):
                substr = buff[i:]
                if substr in num_names:
                    val = numbers[substr]
                    if firstDigit is None:
                        firstDigit = val
                        buff = ""
                    lastDigit = val
                    continue

        if char.isdigit():
            if firstDigit is None:
                firstDigit = char
            lastDigit = char

    if lastDigit is None:
        lastDigit = firstDigit

    num = int(str(firstDigit) + str(lastDigit))
    print("line: " + line + "; num:" + str(num))

    total = total + num

print("total:" + str(total))
