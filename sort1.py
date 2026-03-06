import numpy as np
import matplotlib.pyplot as plt 

class Counter:
    def __init__(self):
        self.compares: int = 0
        self.exchanges: int = 0
    
    def reset(self):
        self.compares = 0; self.exchanges = 0

def less(a: int, b: int, counter: Counter):
    counter.compares += 1
    return a < b

def exchange(my_list: list, a, b, counter: Counter):
    counter.exchanges += 1
    my_list[a], my_list[b] = my_list[b], my_list[a]

def sort(my_list: list, counter: Counter):
    n = len(my_list)
    for i in range(1, n):
        j = i
        while j > 0 and less(my_list[j], my_list[j - 1], counter):
            exchange(my_list, j, j - 1, counter) 
            j -= 1

def plot_data(average_case: list):
    fig, ax = plt.subplots(1, 2)
    # plotting the compares
    ax[0].set_title("Compares")
    ax[0].set_xlabel("N"); ax[0].set_ylabel("Count")
    ax[0].grid(color='black', linestyle='-', linewidth=1)
    ax[0].plot([n[0] for n in average_case], [n[1] for n in average_case], color='orange', label="Measured average")
    ax[0].plot([n[0] for n in average_case], [(n[0] ** 2) / 4 for n in average_case], color='orange', linestyle="dotted", lw=5, label="Expected average")

    ax[0].legend()

    # plotting the exchanges
    ax[1].set_title("Exchanges") 
    ax[1].grid(color='black', linestyle='-', linewidth=1)
    ax[1].set_xlabel("N"); ax[1].set_ylabel("Count")
    ax[1].plot([n[0] for n in average_case], [n[2] for n in average_case], color='orange', label="Measured average")
    ax[1].plot([n[0] for n in average_case], [(n[0] ** 2) / 4 for n in average_case], color='orange', linestyle="dotted", lw=5, label="Expected average")
    
    ax[1].legend()

    plt.show()

if __name__ == "__main__":
    counter = Counter()

    # average case tests
    results_average_case = []
    for length in range(10, 1000, 10):
        sampl = list(np.random.uniform(low=0, high=length, size=(length,)))
        print("Before: ", sampl)
        sort(sampl, counter)
        print("After: ", sampl)
        results_average_case.append((length, counter.compares, counter.exchanges))
        counter.reset()

    plot_data(results_average_case)