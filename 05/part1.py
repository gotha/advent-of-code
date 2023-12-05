import sys
import json


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
    maps[curr_map_id].append({
        "src": [src, src+count],
        "dst": [dst, dst+count]
    })

locations = []
for seed in seeds:
    res = {}
    for k in maps.keys():
        # print("map:" + str(k))
        # print(maps[k])
        seek = seed if k == 0 else res[k-1]
        # print("seek:" + str(seek))
        found = False
        for i in maps[k]:
            if found is False:
                res[k] = seek
            src_start, src_end = i["src"]
            dst_start, dst_end = i["dst"]
            if seek >= src_start and seek < src_end:
                offset = seek-src_start
                res[k] = dst_start + offset
                found = True

    locations.append(res[len(maps)-1])
    print(str(seed) + ": " + str(res))

print(locations)
print(min(locations))
