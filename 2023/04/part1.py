import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

total_points = 0
for i, l in enumerate(data.splitlines()):
    game, nums = l.split(":")
    winning_nums_str, got_nums_str = nums.split("|")
    winning_nums = list(map(int, winning_nums_str.strip().split()))
    got_nums = list(map(int, got_nums_str.strip().split()))
    hits = (set(winning_nums) & set(got_nums))
    val = 0
    if len(hits) > 0:
        val = 1 * 2 ** (len(hits)-1)
    total_points += val

print(total_points)
