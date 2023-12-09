import sys
import math

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
lines = f.read().splitlines()
f.close()

instructions = lines[0]
equasions = lines[2:len(lines)]

data = {}
starts = []
for i in equasions:
    key, vals = i.split("=")
    key = key.strip()
    if key.endswith("A"):
        starts.append(key)
    vals = vals.strip(" ()")
    v1, v2 = vals.split(", ")
    data[key] = {
        "L": v1,
        "R": v2,
    }


num_steps_arr = []
for i in starts:
    curr_val = i

    num_steps = 0
    instruction_i = 0
    while curr_val.endswith("Z") is False:
        num_steps = num_steps + 1
        curr_instruction = instructions[instruction_i]
        curr_val = data[curr_val][curr_instruction]

        instruction_i = instruction_i + 1
        if instruction_i >= len(instructions):
            instruction_i = 0

    num_steps_arr.append(num_steps)

print(math.lcm(*num_steps_arr))
