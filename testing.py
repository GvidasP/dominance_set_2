from tqdm import tqdm
import time

from queens_final import Queens
from bishops_final import Bishops


def solve(n_from, n_to):
    queens_time = []
    bishops_time = []
    for i in tqdm(range(n_from, n_to + 1), desc='Valdoves'):
        start = time.perf_counter()
        q = Queens(i)
        q.placeQueen(0)
        end = time.perf_counter()

        queens_time.append((end-start))

    for i in tqdm(range(n_from, n_to + 1), desc='Rikiai'):
        start = time.perf_counter()
        b = Bishops(i)
        b.place(0, 0, 0)
        end = time.perf_counter()

        bishops_time.append((end-start))

    print("Valdoves: {}\nRikiai: {}".format(queens_time, bishops_time))


def solve_single(n):
    q = Queens(n, output=True)
    q.placeQueen(0)

    b = Bishops(n, output=True)
    b.place(0, 0, 0)
