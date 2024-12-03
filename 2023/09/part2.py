import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()


def get_diff(digits):
    retval = []
    for i in range(0, len(digits)-1):
        retval.append(digits[i+1] - digits[i])
    return retval


def are_all_zeroes(digits):
    non_zeroes = filter(lambda x: x != 0, digits)
    return len(list(non_zeroes)) == 0


sum = 0
for l in data.splitlines():
    digits = list(map(int, l.split()))
    chain = []
    chain.append(digits[0])
    while are_all_zeroes(digits) is False:
        digits = get_diff(digits)
        chain.append(digits[0])

    chain.pop()
    chain.reverse()

    ret = 0
    for elem in chain:
        ret = elem - ret

    sum = sum+ret

print(sum)
