import numpy as np
import time


class Queens():
    def __init__(self, size, output=False):
        self.size = size
        self.board = np.full((size, size), False, dtype=bool)
        self.minCount = 5000
        self.output = output
        self.start = time.perf_counter()

    def placeQueen(self, countSoFar):
        i, j = 0, 0

        if(countSoFar >= self.minCount):
            return

        self.findUnattackedCell(countSoFar)

        for i in range(self.size):
            for j in range(self.size):
                if(not self.isAttacked(i, j)):
                    self.board[i][j] = True

                    self.placeQueen(countSoFar + 1)

                    self.board[i][j] = False

    def findUnattackedCell(self, countSoFar):
        for i in range(self.size):
            for j in range(self.size):
                if(not self.isAttacked(i, j)):
                    return

        self.minCount = countSoFar
        if(self.output):
            self.storeLayout()

        return

    def isAttacked(self, row, col):
        for i in range(self.size):
            if(self.board[i][col]):
                return True

        for i in range(self.size):
            if(self.board[row][i]):
                return True

        for i in range(self.size):
            if(row - i >= 0 and col - i >= 0 and self.board[row - i][col - i]):
                return True
            elif(row - i >= 0 and col + i < self.size and
                 self.board[row - i][col + i]):
                return True
            elif(row + i < self.size and col - i >= 0 and
                 self.board[row + i][col - i]):
                return True
            elif(row + i < self.size and col + i < self.size and
                 self.board[row + i][col + i]):
                return True

        return False

    def storeLayout(self):
        end = time.perf_counter()

        solution = ""
        layout = ""

        for row in self.board:
            line = ""
            for cell in row:
                if cell:
                    line += "Q "
                else:
                    line += ". "
            solution += line + '\n'
        layout += '\n{}\nUztruko laiko: {}\nSkaicius valdoviu: {}\n'.format(
            solution, end - self.start, self.minCount)

        file = open('solution_queens.txt', 'w')
        file.write(layout)
        file.close()
