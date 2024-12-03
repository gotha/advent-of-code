import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

special_chars = ["*", "+", "-", "%", "$", "&", "@"]

matrix = []
curr_row = 0
for l in data.splitlines():
    matrix.append([])
    buff = ""
    for c in l:
        if c.isdigit():
            buff += c
            continue
        if c == "." or c in special_chars:
            for p in range(len(buff)):
                matrix[curr_row].append(int(buff))
            val = None if c not in special_chars else c
            matrix[curr_row].append(val)
            buff = ""
            continue

        matrix[curr_row].append(c)
        continue

    if len(buff) > 0:
        for p in range(len(buff)):
            matrix[curr_row].append(int(buff))
        buff = ""

    curr_row += 1

found_numbers = []
for y, row in enumerate(matrix):
    for x, c in enumerate(row):
        if isinstance(c, int) or c == "." or c is None:
            continue

        for fx in range(x-1, x+2):
            for fy in range(y-1, y+2):
                if fx == x and fy == y:
                    continue  # skip current position
                if fx < 0 or fy < 0 or fx >= len(row) or fy >= len(matrix):
                    continue  # out of bound

                val = matrix[fy][fx]
                if val is not None and isinstance(val, int):
                    found_numbers.append(val)

                    matrix[fy][fx] = None  # clean current pos
                    tx = fx+1
                    # clean the number forward in the row
                    while tx < len(row) and matrix[fy][tx] is not None and isinstance(matrix[fy][tx], int):
                        matrix[fy][tx] = None
                        tx += 1
                    tx = fx-1
                    # clean the number backwards in the row
                    while tx >= 0 and matrix[fy][tx] is not None and isinstance(matrix[fy][tx], int):
                        matrix[fy][tx] = None
                        tx -= 1

print(found_numbers)
print(sum(found_numbers))
