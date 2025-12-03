import re
import sys


class Bot:
    def __init__(self, id, value_in=None):
        self.id = id
        self.values = [value_in] if value_in is not None else []
        self.low_out = None
        self.high_out = None

    def __repr__(self):

        return "bot %s (%s in, low -> %s, high -> %s)" % (
            self.id,
            self.values,
            (
                "Bot %s" % self.low_out.id
                if type(self.low_out) == Bot
                else "Output %s" % self.low_out
            ),
            (
                "Bot %s" % self.high_out.id
                if type(self.high_out) == Bot
                else "Output %s" % self.high_out
            ),
        )


class Output:
    def __init__(self, id, v=None):
        self.id = id
        self.value = v

    def __repr__(self):
        return "Output %s=%s" % (self.id, self.value)


input_re = re.compile(r"value (\d+) goes to bot (\d+)")
bot_re = re.compile(
    r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
)

with open("input_10.txt") as description:
    connections = [c.strip() for c in description.readlines()]

bots = {}
outputs = {}

for connection in connections:
    m = input_re.match(connection)

    if m:
        value = m.group(1)
        bot_id = m.group(2)

        if bot_id in bots:
            bots[bot_id].values.append(int(value))
            if 61 in bots[bot_id].values and 17 in bots[bot_id].values:
                print("HEY BOT %s IS THE ANSWER" % bot_id)
        else:
            bots[bot_id] = Bot(bot_id, int(value))

    m = bot_re.match(connection)

    if m:
        bot_input_id = m.group(1)
        low_bot_or_output = m.group(2)
        low_out_id = m.group(3)
        high_bot_or_output = m.group(4)
        high_out_id = m.group(5)

        if bot_input_id in bots:
            bot = bots[bot_input_id]
        else:
            bot = Bot(bot_input_id)
            bots[bot_input_id] = bot

        if low_bot_or_output == "output":
            bot.low_out = Output(low_out_id)
            outputs[low_out_id] = bot.low_out
        else:
            if low_out_id in bots:
                bot.low_out = bots[low_out_id]
            else:
                bot.low_out = Bot(low_out_id)
                bots[low_out_id] = bot.low_out

        if high_bot_or_output == "output":
            bot.high_out = Output(high_out_id)
            outputs[high_out_id] = bot.low_out
        else:
            if high_out_id in bots:
                bot.high_out = bots[high_out_id]
            else:
                bot.high_out = Bot(high_out_id)
                bots[high_out_id] = bot.high_out

while True:
    # iterate until a bot has both 61 and 17
    for _, bot in bots.items():
        if len(bot.values) == 2:
            bot.values.sort()

            if type(bot.low_out) == Bot:
                bot.low_out.values.append(bot.values[0])
            else:
                bot.low_out.value = bot.values[0]

            if type(bot.high_out) == Bot:
                bot.high_out.values.append(bot.values[1])
            else:
                bot.high_out.value = bot.values[1]

            bot.values = []

    if outputs["0"].value and outputs["1"].value and outputs["2"].value:
        print(outputs["0"].value * outputs["1"].value * outputs["2"].value)
        print(outputs.values())
        print(bots.values())
        sys.exit(0)

    # for _, bot in bots.items():
    #     if 61 in bot.values and 17 in bot.values:
    #         print('HEY BOT %s IS THE ANSWER' % bot.id)
    #         sys.exit(0)
