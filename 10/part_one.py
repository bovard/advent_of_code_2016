
with open('input.txt') as f:
    instructions = f.readlines()

bots = {}
holding = {}
outputs = {}


def set_holding(h, b, val, p=False):
    if p:
        print "giving {} to {}".format(val, b)
    if not h.get(b):
        h[b] = [val]
    else:
        if len(h[bot]) > 2:
            print "error!"
        h[b].append(val)
    if p:
        print "{} now has {}".format(b, h[b])

for line in instructions:
    line = line.strip()
    if line.startswith("bot") and len(line.split(' ')) == 12:
        bot_id = int(line.split(' ')[1])
        low_bot = line.split(" ")[5] == 'bot'
        low = int(line.split(" ")[6])
        high_bot = line.split(" ")[-2] == 'bot'
        high = int(line.split(" ")[-1])
        bots[bot_id] = {
            "low_bot": low_bot,
            "low": low,
            "high": high,
            "high_bot": high_bot
        }
    elif line.startswith("value"):
        v = int(line.split(' ')[1])
        bot = int(line.split(' ')[-1])
        set_holding(holding, bot, v)
    else:
        print "OH NO"


done = False
while not done:
    for key, values in holding.copy().items():
        # print key, values
        if len(values) == 2:
            print key, values
            values = sorted(values)
            print values
            low_id = bots[key]["low"]
            high_id = bots[key]["high"]
            if bots[key]["low_bot"]:
                set_holding(holding, low_id, values[0], True)
            else:
                outputs[low_id] = values[0]
            if bots[key]["high_bot"]:
                set_holding(holding, high_id, values[1], True)
            else:
                outputs[high_id] = values[1]

            holding[key] = values[2:]

            if outputs.get(0) is not None and outputs.get(1) is not None and outputs.get(2) is not None:
                print outputs.get(0), outputs.get(1), outputs.get(2)
                print outputs.get(0) * outputs.get(1) * outputs.get(2)
                exit()

