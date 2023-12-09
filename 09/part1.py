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


def calc_inferred_nums(digits):
    tmp = digits[0]
    new = [digits[0]]
    for i in range(1, len(digits)):
        tmp = tmp + digits[i]
        new.append(tmp)
    return new


sum = 0
for l in data.splitlines():
    digits = list(map(int, l.split()))
    chain = []
    chain.append(digits[len(digits)-1])
    while are_all_zeroes(digits) is False:
        digits = get_diff(digits)
        chain.append(digits[len(digits)-1])

    chain.reverse()
    inferred = calc_inferred_nums(chain)

    sum = sum+inferred[len(inferred)-1]

print(sum)
