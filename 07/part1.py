import sys

if len(sys.argv) < 2:
    print("please specify input file")
    sys.exit(1)

f = open(sys.argv[1], 'r')
data = f.read()
f.close()

cards_strength = ["A", "K", "Q", "J", "T",
                  "9", "8", "7", "6", "5", "4", "3", "2"]
cards_strength_pos = {}
for i, c in enumerate(cards_strength):
    cards_strength_pos[c] = i

types = {
    "high": 7,
    "pair": 6,
    "two_pair": 5,
    "three_of_a_kind": 4,
    "full_house": 3,
    "four_of_a_kind": 2,
    "five_of_a_kind": 1,
}
types_map = {}
for k in types:
    types_map[types[k]] = k


def get_type(cards_set):
    cards = list(cards_set)
    count = {x: cards.count(x) for x in cards}
    num_keys = len(count.keys())
    if num_keys == len(cards):
        return types["high"]  # all different
    if num_keys == 1:
        return types["five_of_a_kind"]

    values = list(count.values())
    if num_keys == 2:
        if 4 in values:
            return types["four_of_a_kind"]
        if 3 in values and 2 in values:
            return types["full_house"]
    if num_keys == 3:
        if 3 in values and 1 in values:
            return types["three_of_a_kind"]

    num_pairs = 0
    num_threes = 0
    for k in count.keys():
        if count[k] == 2:
            num_pairs += 1
            continue
        if count[k] == 3:
            num_threes += 1
            continue
    if num_threes == 1 and num_pairs == 1:
        return types["full_house"]
    if num_threes == 1 and len(count) == 3:
        return types["three_of_a_kind"]
    if num_pairs == 2:
        return types["two_pair"]
    if num_pairs == 1 and len(count) == 4:
        return types["pair"]

    raise Exception("unknown card_set type: " +
                    str(cards_set) + "; " + str(count))


res = []
for i, l in enumerate(data.splitlines()):
    cards, bid = l.strip().split()
    type = get_type(cards)
    cards_arr = list(cards)
    res.append({
        "cards": cards,
        "bid": bid,
        "type": type,
        "c1str": cards_strength_pos[cards_arr[0]],
        "c2str": cards_strength_pos[cards_arr[1]],
        "c3str": cards_strength_pos[cards_arr[2]],
        "c4str": cards_strength_pos[cards_arr[3]],
        "c5str": cards_strength_pos[cards_arr[4]],
    })

total = 0
res = sorted(res, key=lambda x: (
    x["type"], x["c1str"], x["c2str"], x["c3str"], x["c4str"], x["c5str"]), reverse=True)
num_items = len(res)
for i in range(0, num_items):

    rank = i+1
    total += rank*int(res[i]["bid"])
    print("rank:" + str(rank) + "; " +
          str(res[i]["cards"]) + "; type: " + str(types_map[res[i]["type"]]) + "; nums:" + str(res[i]["c1str"]) + "," + str(res[i]["c2str"]) + "," + str(res[i]["c3str"]) + "," + str(res[i]["c4str"]) + "," + str(res[i]["c5str"]) + "; bid:" + res[i]["bid"])


print(total)
