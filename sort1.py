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

def plot_data(average_case: list, worst_case: list, best_case: list):
    fig, ax = plt.subplots(1, 2)
    # plotting the compares
    ax[0].set_title("Compares")
    ax[0].plot([n[0] for n in average_case], [n[1] for n in average_case], color='orange')
    ax[0].plot([n[0] for n in average_case], [(n[0] ** 2) / 4 for n in average_case], color='orange', linestyle="dotted", lw=5)
    
    ax[0].plot([n[0] for n in worst_case], [n[1] for n in worst_case], color='red')
    ax[0].plot([n[0] for n in worst_case], [(n[0] ** 2) / 2 for n in worst_case], color='red', linestyle="dotted", lw=5)

    ax[0].plot([n[0] for n in best_case], [n[1] for n in best_case], color='lime')
    ax[0].plot([n[0] for n in best_case], [n[0] - 1 for n in best_case], color='lime', linestyle="dotted", lw=5)

    # plotting the exchanges
    ax[1].set_title("Exchanges") 
    ax[1].plot([n[0] for n in average_case], [n[2] for n in average_case], color='orange')
    ax[1].plot([n[0] for n in average_case], [(n[0] ** 2) / 4 for n in average_case], color='orange', linestyle="dotted", lw=5)
    
    ax[1].plot([n[0] for n in worst_case], [n[2] for n in worst_case], color='red')
    ax[1].plot([n[0] for n in worst_case], [(n[0] ** 2) / 2 for n in worst_case], color='red', linestyle="dotted", lw=5)
    
    ax[1].plot([n[0] for n in best_case], [n[2] for n in best_case], color='lime')
    ax[1].plot([n[0] for n in best_case], [0 for _ in best_case], color='lime', linestyle="dotted", lw=5)

    plt.show()

if __name__ == "__main__":
    counter = Counter()

    # average case tests
    results_average_case = []
    for length in range(10, 200, 10):
        sampl = list(np.random.uniform(low=0.5, high=135.63, size=(length,)))
        sort(sampl, counter)
        results_average_case.append((length, counter.compares, counter.exchanges))
        counter.reset()
    
    # worst case tests
    results_worst_case = []
    for length in range(10, 200, 10):
        sampl = list(np.sort(np.random.uniform(0.5, 135.63, length))[::-1])
        sort(sampl, counter)
        results_worst_case.append((length, counter.compares, counter.exchanges))
        counter.reset()
    
    # best case tests
    results_best_case = []
    for length in range(10, 200, 10):
        sampl = list(np.sort(np.random.uniform(0.5, 135.63, length)))
        sort(sampl, counter)
        results_best_case.append((length, counter.compares, counter.exchanges))
        counter.reset()
    
    plot_data(results_average_case, results_worst_case, results_best_case)