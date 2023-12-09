import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
lines = f.read().splitlines()
f.close()

instructions = lines[0]
equasions = lines[2:len(lines)]

data = {}
for i in equasions:
    key, vals = i.split("=")
    key = key.strip()
    vals = vals.strip(" ()")
    v1, v2 = vals.split(", ")
    data[key] = {
        "L": v1,
        "R": v2,
    }

num_steps = 0
instruction_i = 0
curr_val = "AAA"
while curr_val != "ZZZ":
    num_steps = num_steps + 1
    print("step:" + str(num_steps) + ") ", end="")
    print("From:" + curr_val, end="")
    curr_instruction = instructions[instruction_i]
    print(" going: " + str(curr_instruction), end="")
    curr_val = data[curr_val][curr_instruction]
    print("; got:" + str(curr_val))

    instruction_i = instruction_i + 1
    if instruction_i >= len(instructions):
        instruction_i = 0

print(num_steps)
