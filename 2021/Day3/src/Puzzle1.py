def readFile():
    with open('2021/Day3/input.txt', 'r') as file:
        numbers = [[int(bit) for bit in number.split('\n')[0]]
                   for number in file]
    return numbers


def countNumbers():
    numbers = readFile()
    frecuencies = {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}, 2: {0: 0, 1: 0}, 3: {0: 0, 1: 0}, 4: {0: 0, 1: 0}, 5: {
        0: 0, 1: 0}, 6: {0: 0, 1: 0}, 7: {0: 0, 1: 0}, 8: {0: 0, 1: 0}, 9: {0: 0, 1: 0}, 10: {0: 0, 1: 0}, 11: {0: 0, 1: 0}}
    for i in range(12):
        for number in numbers:
            if number[i] == 0:
                frecuencies[i][0] += 1
            else:
                frecuencies[i][1] += 1
    return frecuencies

def getNumbers():
    frecuencies = countNumbers()
    number = ""
    opositeNumber = ""
    for i in range(12):
        if frecuencies[i][0] > frecuencies[i][1]:
            number += "0"
            opositeNumber += "1"
        else:
            number += "1"
            opositeNumber += "0"

    return [number,opositeNumber]

numbers = getNumbers()
print(int(numbers[0],2) * int(numbers[1],2))
