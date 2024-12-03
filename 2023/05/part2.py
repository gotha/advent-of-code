import sys
import json
from multiprocessing.dummy import Pool as ThreadPool


def pprint(x):
    print(json.dumps(x, sort_keys=False, indent=2))


if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

seeds = []

maps = {}
maps_keys = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light",
             "light-to-temperature", "temperature-to-humidity", "humidity-to-location"]
for i in range(0, len(maps_keys)):
    maps[i] = []

curr_map_id = None
for i, l in enumerate(data.splitlines()):
    print("parsing line:" + str(i+1))
    if l == "":
        buff = None
        continue
    if l.find("seeds:") == 0:
        _, seeds_str = l.strip().split(":")
        seeds = list(map(int, seeds_str.strip().split()))
        continue

    key_found = False
    for map_id, map_key in enumerate(maps_keys):
        if l.find(map_key) == 0:
            curr_map_id = map_id
            key_found = True
            break
    if key_found is True:
        continue
    if curr_map_id is None:
        continue

    dst, src, count = list(map(int, l.strip().split()))
    maps[curr_map_id].append([
        range(src, src+count),
        dst-src
    ])

"""
# first part re-implemented
min_loc = sys.maxsize
for seed in seeds:
    res = {}
    for k in maps.keys():
        # print("map:" + str(maps[k]))
        # print(maps[k])
        seek = seed if k == 0 else res[k-1]
        res[k] = seek
        for [r, offset] in maps[k]:
            if seek in r:
                res[k] = seek+offset
                break
    loc = res[len(maps)-1]
    if loc < min_loc:
        min_loc = loc

print(min_loc)
"""

seed_pairs = []
for i in range(0, len(seeds), 2):
    seed_pairs.append([seeds[i], seeds[i] + seeds[i+1]])


def calc_min_loc(pair):
    min_loc = sys.maxsize
    seed_start, seed_end = pair
    for seed in range(seed_start, seed_end+1):
        print(".", end="")
        res = {}
        for k in maps.keys():
            # print("start:" + str(seed_start) + "; end:" + str(seed_end) + "; map:" + str(k) + "; seed:" + str(seed) + " start")
            seek = seed if k == 0 else res[k-1]
            res[k] = seek
            for [r, offset] in maps[k]:
                if seek in r:
                    res[k] = seek+offset
                    break
        loc = res[len(maps)-1]
        if loc < min_loc:
            min_loc = loc
    return min_loc


pool = ThreadPool(len(seed_pairs))
res = pool.map(calc_min_loc, seed_pairs)
print(res)
print("==========================")
print(min(res))
print("==========================")
