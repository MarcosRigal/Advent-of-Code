def readFile():
    with open('2021/Day3/input.txt', 'r') as file:
        numbers = [[int(bit) for bit in number.split('\n')[0]]
                   for number in file]
    return numbers


def countNumbers(numbers):
    frecuencies = {0: {0: 0, 1: 0}, 1: {0: 0, 1: 0}, 2: {0: 0, 1: 0}, 3: {0: 0, 1: 0}, 4: {0: 0, 1: 0}, 5: {
        0: 0, 1: 0}, 6: {0: 0, 1: 0}, 7: {0: 0, 1: 0}, 8: {0: 0, 1: 0}, 9: {0: 0, 1: 0}, 10: {0: 0, 1: 0}, 11: {0: 0, 1: 0}}
    for i in range(12):
        for number in numbers:
            if number[i] == 0:
                frecuencies[i][0] += 1
            else:
                frecuencies[i][1] += 1
    return frecuencies


def getOxigen():
    numbers = readFile()
    frecuencies = countNumbers(numbers)
    number = ""
    for i in range(12):
        if not(frecuencies[i][0] == 0 and frecuencies[i][1] == 1 or frecuencies[i][0] == 1 and frecuencies[i][1] == 0):
            if frecuencies[i][0] > frecuencies[i][1]:
                number += "0"
                numbers = [number for number in numbers if number[i] != 1]
            else:
                number += "1"
                numbers = [number for number in numbers if number[i] != 0]
            frecuencies = countNumbers(numbers)
        if (frecuencies[i][0] == 0 and frecuencies[i][1] == 1 or frecuencies[i][0] == 1 and frecuencies[i][1] == 0):
            return numbers

    return numbers


def getCO2():
    numbers = readFile()
    frecuencies = countNumbers(numbers)
    for i in range(12):
        if frecuencies[i][1] < frecuencies[i][0]:
            numbers = [number for number in numbers if number[i] != 0]
        else:
            numbers = [number for number in numbers if number[i] != 1]
        frecuencies = countNumbers(numbers)
        if (frecuencies[i][0] == 0 and frecuencies[i][1] == 1 or frecuencies[i][0] == 1 and frecuencies[i][1] == 0):
            return numbers

    return numbers


oxigen = "".join(str(bit) for bit in getOxigen()[0])
co2 = "".join(str(bit) for bit in getCO2()[0])
print(int(oxigen,2) * int(co2,2))
