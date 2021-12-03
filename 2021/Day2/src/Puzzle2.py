def readFile():
    moves = {}
    aim = 0
    with open('2021/Day2/input.txt', 'r') as file:
        for line in file:
            for (k, v) in [line.strip().split(None, 1)]:
                if k == 'forward':
                    moves['horizontal-position'] = moves.get('horizontal-position', 0) + int(v)
                    moves['depth'] = moves.get('depth', 0) + (aim * int(v))
                elif k == 'down':
                    aim += int(v)
                elif k == 'up':
                    aim -= int(v)
    return moves


def calculeResult():
    moves = readFile()
    return moves['horizontal-position'] * (moves['depth'])


print(calculeResult())
