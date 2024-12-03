import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

lines = data.splitlines()
tally = {}
for i in range(0, len(lines)):
    tally[i] = 1

for i, l in enumerate(lines):
    game, nums = l.split(":")
    winning_nums_str, got_nums_str = nums.split("|")
    winning_nums = list(map(int, winning_nums_str.strip().split()))
    got_nums = list(map(int, got_nums_str.strip().split()))
    hits = (set(winning_nums) & set(got_nums))
    num_hits = len(hits)
    if num_hits > 0:
        for x in range(i+1, i+num_hits+1):
            tally[x] = tally[x] + 1*tally[i]

print(sum(tally.values()))
