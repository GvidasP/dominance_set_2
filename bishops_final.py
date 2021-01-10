import numpy as np
import time


class Bishops():
    def __init__(self, size, output=False):
        self.size = size
        self.minCount = 14
        self.bishops = np.full((size, size), 0, dtype=int)
        self.layouts = []
        self.output = output
        self.start = time.perf_counter()

    def place(self, countSoFar, i, j):
        if(countSoFar >= self.minCount):
            return

        self.bishops[i][j] = 2

        self.check_for_solution(countSoFar)

        next_i, next_j = self.calculate_next_coordinates(i, j)

        if(not next_i and not next_j):
            return

        self.place(countSoFar + 1, next_i, next_j)

        self.bishops[i][j] = 0

        self.place(countSoFar, next_i, next_j)

    def calculate_next_coordinates(self, i, j):
        next_i, next_j = i, j

        if(next_j >= self.size - 1 and next_i < self.size - 1):
            next_j = 0
            return next_i + 1, next_j

        if(next_i >= self.size - 1):
            return False, False

        else:
            return next_i, next_j + 1

    def check_for_solution(self, countSoFar):
        board = self.convert_to_board()

        if 0 in board:
            return

        self.minCount = countSoFar

        if(self.output):
            self.storeLayout()

        return

    def convert_to_board(self):
        board = np.copy(self.bishops)

        bishops = np.where(board == 2)
        bishops_positions = list(zip(bishops[0], bishops[1]))

        for count, (row, column) in enumerate(bishops_positions):
            for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
                board[i][j] = 1
            for i, j in zip(range(row, self.size, 1), range(column, -1, -1)):
                board[i][j] = 1
            for i, j in zip(range(row, self.size, 1), range(column, self.size, 1)):
                board[i][j] = 1
            for i, j in zip(range(row, -1, -1), range(column, self.size, 1)):
                board[i][j] = 1

        return board

    def storeLayout(self):
        end = time.perf_counter()

        solution = ""
        layout = ""

        for row in self.bishops:
            line = ""
            for cell in row:
                if cell:
                    line += "B "
                else:
                    line += ". "
            solution += line + '\n'
        layout += '\n{}\nUztruko laiko: {}\nSkaicius rikiu: {}\n'.format(
            solution, end - self.start, self.minCount)

        file = open('solution_bishops.txt', 'w')
        file.write(layout)
        file.close()
