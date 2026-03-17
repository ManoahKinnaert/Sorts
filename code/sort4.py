import numpy as np
import matplotlib.pyplot as plt 

from utils import Counter, less, exchange

# Hoare partitioning
def partition_hoare(a: list, lo: int, hi: int, counter: Counter):
    i, j = lo, hi + 1
    v = a[lo]
    while True:

        i += 1
        while less(a[i], v, counter):
            i += 1
            if i == hi: break
        j -= 1 

        while less(v, a[j], counter): 
            j -= 1
            if j == lo: break 

        if i >= j: break
        exchange(a, i, j, counter)

    exchange(a, lo, j, counter)
    return j

# Lomuto partitioning
def partition_lomuto(a: list, lo: int, hi: int, counter: Counter):
    i = lo - 1
    v = a[hi]
    j = lo 
    while j <= hi - 1:
        if less(a[j], v, counter):
            i += 1
            exchange(a, i, j, counter)
        j += 1
    exchange(a, i + 1, hi, counter)
    return i + 1

def sort(a: list, lo: int, hi: int, counter: Counter, lomuto: bool=False):
    if (hi <= lo): return 
    j = partition_lomuto(a, lo, hi, counter) if lomuto else partition_hoare(a, lo, hi, counter)
    sort(a, lo, j - 1, counter)
    sort(a, j + 1, hi, counter)


def plot_data(average_case: list, worst_case: list=None, best_case: list=None):
    fig, ax = plt.subplots(1, 2)
    compares, exchanges = ax 
    # plot compares 
    compares.set_title("Compares")

    compares.legend()
    # plot exchanges
    exchanges.set_title("Exchanges")

    exchanges.legend()

def test_average_case(length: int, results: list, counter: Counter):
    # repeat 'length' times to get a real idea of the average case
    for _ in range(length):
        sampl = list(np.random.uniform(low=0, high=length, size=(length,)))
        print("Before: ", sampl)
        sort(sampl, lo=0, hi=len(sampl - 1), counter=counter)
        results.append((length, counter.compares, counter.exchanges))
        counter.reset()
        print("After: ", sampl)

def test_worst_case(length: int, results: list, counter: Counter):
    pass 

def test_best_case(results, counter):
    pass 

def test_sorts():
    pass 

if __name__ == "__main__":
    counter = Counter()
    b = 10
    a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort(a, 0, len(a) - 1, counter)
    print(a)