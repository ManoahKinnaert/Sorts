"""
This file contains all code concerning an experiment to determine the time complexity of the Quicksort algorithm.
"""
from utils import Counter, less, exchange
import numpy as np
import matplotlib.pyplot as plt 

# Hoare partitioning
def partition_hoare(a: list, lo: int, hi: int, counter: Counter):
    i, j = lo, hi + 1
    v = a[lo]
    while True:
        i += 1
        while i < hi and less(a[i], v, counter):
            i += 1

        j -= 1
        while j > lo and less(v, a[j], counter):
            j -= 1

        if i >= j: break
        exchange(a, i, j, counter)

    exchange(a, lo, j, counter)
    return j

# Lomuto partitioning
# Not used anywhere for now
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

def sort(a: list, lo: int, hi: int, counter: Counter):
    if (hi <= lo): return 
    j =  partition_hoare(a, lo, hi, counter)
    sort(a, lo, j - 1, counter)
    sort(a, j + 1, hi, counter)

"""
Helper for plotting findings.
"""
def plot_findings(case, compares, exchanges, label, color):
    compares.plot([n[0] for n in case], [n[1] for n in case], color=color, label=label) 
    exchanges.plot([n[0] for n in case], [n[2] for n in case], color=color, label=label)

"""
Plot the findings for the average case.
TODO: Include theoretical curve
"""
def plot_average_case(average_case: list, compares, exchanges):
    plot_findings(average_case, compares, exchanges, "Measured Average", "orange")

"""
Plot the findings for the best case.
TODO: Include theoretical curve
"""
def plot_best_case(best_case: list, compares, exchanges):
    plot_findings(best_case, compares, exchanges, "Measured Best", "green")

"""
Plot the findings for the worst case.
TODO: Include theoretical curve
"""
def plot_worst_case(worst_case: list, compares, exchanges):
    plot_findings(worst_case, compares, exchanges, "Measured Worst", "red")
    #compares.plot([n[0] for n in worst_case], [(n[0] ** 2) / 2 for n in worst_case], color="red", label="Expected Worst", linestyle="dashdot")

"""
Plot our findings.
"""
def plot_data(average_case: list=None, worst_case: list=None, best_case: list=None):
    fig, ax = plt.subplots(1, 2)
    compares, exchanges = ax 
    # compares 
    compares.set_title("Compares")
    compares.set_xlabel("N")
    compares.set_ylabel("Count")
    # set axis scaling for compares
    compares.set_yscale("log")
    compares.set_xscale("log")
    # exchanges
    exchanges.set_title("Exchanges")
    exchanges.set_xlabel("N")
    exchanges.set_ylabel("Count")
    # set axis scaling for exchanges
    exchanges.set_yscale("log")
    exchanges.set_xscale("log")
    # plot the date
    if best_case is not None: plot_best_case(best_case, compares, exchanges)
    if average_case is not None: plot_average_case(average_case, compares, exchanges)
    if worst_case is not None: plot_worst_case(worst_case, compares, exchanges)
    # generate legend
    compares.legend()
    exchanges.legend()
    # show the chart
    plt.show()

"""
Test the average case for Quicksort.
"""
def test_average_case(test_print: bool, length: int, results: list, counter: Counter):
    total_compares = 0
    total_exchanges = 0
    # repeat 'length' times to get a real idea of the average case
    for _ in range(length):
        sampl = list(np.random.uniform(low=0, high=length, size=(length,)))
        if test_print: print("Before: ", sampl)
        sort(sampl, lo=0, hi=len(sampl) - 1, counter=counter)
        total_compares += counter.compares
        total_exchanges += counter.exchanges
        counter.reset()
        if test_print: print("After: ", sampl)
    results.append((length, total_compares / length, total_exchanges / length))

"""
Worst case for Quick Sort is an array that is already sorted.
"""
def test_worst_case(test_print: bool, length: int, results: list, counter: Counter):
    sampl = list(range(length))
    if test_print: print("Before: ", sampl)
    sort(sampl, lo=0, hi=len(sampl) - 1, counter=counter)
    results.append((length, counter.compares, counter.exchanges))
    counter.reset()
    if test_print: print("After: ", sampl)

"""
Generates a best case starting list for Quicksort.
"""
def best_case_list(n: int):
    result = []

    def build(values):
        if not values:
            return
        mid = len(values) // 2
        # put median first
        result.append(values[mid])
        # recursively process left and right
        build(values[:mid])
        build(values[mid+1:])

    build(list(range(n)))
    return result

"""
Best case for Quicksort is an array where the pivot element is exactly in the middle (of the sorted array)
"""
def test_best_case(test_print: bool, length: int, results: list, counter: Counter):
    sampl = best_case_list(length)
    if test_print: print("Before: ", sampl)
    sort(sampl, lo=0, hi=len(sampl) - 1, counter=counter)
    results.append((length, counter.compares, counter.exchanges))
    counter.reset()
    if test_print: print("After: ", sampl)

"""
Test sorting algorithm over multiple array / list sizes.
"""
def test_sorts(test_print: bool, counter: Counter):
    best = []
    average = []
    worst = []
    for length in range(10, 1000, 10):
        test_best_case(test_print, length, best, counter)
        test_average_case(test_print, length, average, counter)
        test_worst_case(test_print, length, worst, counter)

    return best, average, worst


if __name__ == "__main__":
    counter = Counter()
    best, average, worst = test_sorts(False, counter)
    plot_data(average_case=average, best_case=best, worst_case=worst)
