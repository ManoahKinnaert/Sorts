"""
This file contains all the code related to the SORT1 experiment where we try to determine
the time complexity of the Insertionsort algorithm.
"""
from utils import Counter, less, exchange
import numpy as np
import matplotlib.pyplot as plt 


def sort(my_list: list, counter: Counter):
    n = len(my_list)
    for i in range(1, n):
        j = i
        while j > 0 and less(my_list[j], my_list[j - 1], counter):
            exchange(my_list, j, j - 1, counter) 
            j -= 1

"""
Plot our findings
"""
def plot_data(average_case: list, worst_case: list=None, best_case: list=None):
    fig, ax = plt.subplots(1, 2)
    # plotting the compares
    ax[0].set_title("Compares")
    ax[0].set_xlabel("N"); ax[0].set_ylabel("Count")
    ax[0].grid(color='black', linestyle='-', linewidth=1)
    ax[0].plot([n[0] for n in average_case], [n[1] for n in average_case], color='orange', label="Measured average")
    ax[0].plot([n[0] for n in average_case], [(n[0] ** 2) / 4 for n in average_case], color='orange', linestyle="dotted", lw=5, label="Expected average")

    
    ax[0].plot([n[0] for n in worst_case], [n[1] for n in worst_case], color='red', label="Measured worst")
    ax[0].plot([n[0] for n in worst_case], [(n[0] ** 2) / 2 for n in worst_case], color='red', linestyle="dotted", lw=5, label="Expected worst")

    ax[0].plot([n[0] for n in best_case], [n[1] for n in best_case], color='lime', label="Measured best")
    ax[0].plot([n[0] for n in best_case], [n[0] - 1 for n in best_case], color='lime', linestyle="dotted", lw=5, label="Expected best")
    
    ax[0].legend()

    # plotting the exchanges
    ax[1].set_title("Exchanges") 
    ax[1].grid(color='black', linestyle='-', linewidth=1)
    ax[1].set_xlabel("N"); ax[1].set_ylabel("Count")
    ax[1].plot([n[0] for n in average_case], [n[2] for n in average_case], color='orange', label="Measured average")
    ax[1].plot([n[0] for n in average_case], [(n[0] ** 2) / 4 for n in average_case], color='orange', linestyle="dotted", lw=5, label="Expected average")
    
    
    ax[1].plot([n[0] for n in worst_case], [n[2] for n in worst_case], color='red', label="Measured worst")
    ax[1].plot([n[0] for n in worst_case], [(n[0] ** 2) / 2 for n in worst_case], color='red', linestyle="dotted", lw=5, label="Expected worst")
    
    ax[1].plot([n[0] for n in best_case], [n[2] for n in best_case], color='lime', label="Measured best")
    ax[1].plot([n[0] for n in best_case], [0 for _ in best_case], color='lime', linestyle="dotted", lw=5, label="Expected best")
    
    ax[1].legend()

    plt.show()

if __name__ == "__main__":
    counter = Counter()
    results_average_case = []
    results_worst_case = []
    results_best_case = []

    # average case tests
    for length in range(10, 1000, 10):
        sampl = list(np.random.uniform(low=0, high=length, size=(length,)))
        print("Before: ", sampl)
        sort(sampl, counter)
        print("After: ", sampl)
        results_average_case.append((length, counter.compares, counter.exchanges))
        counter.reset()
    
    # worst case tests
    for length in range(10, 1000, 10):
        sampl = list(np.sort(np.random.uniform(0, length, length))[::-1])
        print("Before: ", sampl)
        sort(sampl, counter)
        print("After: ", sampl)
        results_worst_case.append((length, counter.compares, counter.exchanges))
        counter.reset()
    
    # best case tests
    for length in range(10, 1000, 10):
        sampl = list(np.sort(np.random.uniform(0, length, length)))
        print("Before: ", sampl)
        sort(sampl, counter)
        print("After: ", sampl)
        results_best_case.append((length, counter.compares, counter.exchanges))
        counter.reset()
    
    plot_data(results_average_case, results_worst_case, results_best_case)