def readFile():
    # It is interesting to have a method that reads the configuration of the cube from a file
    filename = '2021/Day4/input.txt'
    matrixes = []
    i = 0
    with open(filename, 'r') as file:
        numbers = [int(number) for number in file.readline().split('\n')[0].split(",")]
        print(numbers)
        for line in file:
            newMatrix = []
            row1 = [int(number) for number in file.readline().split('\n')[0].split(" ")]
            newMatrix.append(row1)
            row2 = [int(number) for number in file.readline().split('\n')[0].split(" ")]
            newMatrix.append(row2)
            row3 = [int(number) for number in file.readline().split('\n')[0].split(" ")]
            newMatrix.append(row3)
            row4 = [int(number) for number in file.readline().split('\n')[0].split(" ")]
            newMatrix.append(row4)
            row5 = [int(number) for number in file.readline().split('\n')[0].split(" ")]
            newMatrix.append(row5)
            matrixes.append(newMatrix)
        print(matrixes)


readFile()
