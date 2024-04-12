if __name__ == '__main__':
    M = 9

    def openTxt():
        matrix = []
        with open('input.txt', 'r') as f:
            data = [line.strip() for line in f]
            for i in data:
                el = i.split(' ')
                matrix.append(el)
        return matrix


    def matrix(a):
        f = open('output.txt', 'w')
        for i in range(M):
            for j in range(M):
                f.write(str(a[i][j]) + ' ')
                print(a[i][j], end=" ")
            f.write("\n")
            print()


    def solve(grid, row, col, num):
        for x in range(9):
            if int(grid[row][x]) == num:
                return False

        for x in range(9):
            if int(grid[x][col]) == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if int(grid[i + startRow][j + startCol]) == num:
                    return False
        return True


    def result(grid, row, col):

        if row == M - 1 and col == M:
            return True
        if col == M:
            row += 1
            col = 0
        if int(grid[row][col]) > 0:
            return result(grid, row, col + 1)
        for num in range(1, M + 1, 1):

            if solve(grid, row, col, num):

                grid[row][col] = num
                if result(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    grid = openTxt()

    if result(grid, 0, 0):
        matrix(grid)
    else:
        print("Impossible")