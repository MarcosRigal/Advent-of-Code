def readFile():
    matrixes = []
    with open('2021/Day4/input.txt', 'r') as file:
        numbers = [int(number)
                   for number in file.readline().split('\n')[0].split(",")]
        for line in file:
            newMatrix = []
            row1 = {int(number): 0 for number in file.readline().split(
                '\n')[0].split(" ")}
            newMatrix.append(row1)
            row2 = {int(number): 0 for number in file.readline().split(
                '\n')[0].split(" ")}
            newMatrix.append(row2)
            row3 = {int(number): 0 for number in file.readline().split(
                '\n')[0].split(" ")}
            newMatrix.append(row3)
            row4 = {int(number): 0 for number in file.readline().split(
                '\n')[0].split(" ")}
            newMatrix.append(row4)
            row5 = {int(number): 0 for number in file.readline().split(
                '\n')[0].split(" ")}
            newMatrix.append(row5)
            matrixes.append(newMatrix)
        return [numbers, matrixes]


def checkMatrixes(matrixes):
    for matrix in matrixes:
        # CHECK ROW
        for i in range(5):
            if sum(matrix[i].values()) == 5:
                return matrix
        # CHECK COLUM
        row1 = list(matrix[0].values())
        row2 = list(matrix[1].values())
        row3 = list(matrix[2].values())
        row4 = list(matrix[3].values())
        row5 = list(matrix[4].values())
        for i in range(5):
            if (row1[i]+row2[i]+row3[i]+row4[i]+row5[i]) == 5:
                return matrix

    return None


def getUnmarkedSum(matrix):
    sum = 0
    for row in matrix:
        for key in row:
            if row[key] == 0:
                sum += key
    return sum


fileInput = readFile()
numbers = fileInput[0]
matrixes = fileInput[1]
answer = None
num = 0
for number in numbers:
    for matrix in matrixes:
        for row in matrix:
            for key in row:
                if key == number:
                    row[key] = 1
    answer = checkMatrixes(matrixes)
    if answer != None:
        num = number
        break

print(num*getUnmarkedSum(answer))
