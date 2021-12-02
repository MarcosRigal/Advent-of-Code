def readFile():
    with open('2021/Day1/input.txt', 'r') as file:
        numbers = [number for number in file]
    return numbers


def filterList():
    numbers = readFile()
    return [True for previousNumber, actualNumber in zip(numbers, numbers[1:]) if int(previousNumber) < int(actualNumber)]


print(len(filterList()))
