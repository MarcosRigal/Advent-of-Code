def readFile():
    moves = {}
    with open('2021/Day2/input.txt', 'r') as file:
        for line in file:
            for (k, v) in [line.strip().split(None, 1)]:
                moves[k] = moves.get(k, 0) + int(v)
    return moves


def calculeResult():
    moves = readFile()
    return moves['forward'] * (moves['down']-moves['up'])


print(calculeResult())
