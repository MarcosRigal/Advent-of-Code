def readFile():
    with open('2021/Day1/input.txt', 'r') as file:
        numbers = [number for number in file]
    return numbers


def filterList():
    numbers = readFile()
    return [True for number1A, number2AB, number3AB, number4B in zip(numbers, numbers[1:], numbers[2:], numbers[3:]) if ((int(number1A)+int(number2AB)+int(number3AB)) < (int(number2AB)+int(number3AB)+int(number4B)))]


print(len(filterList()))
