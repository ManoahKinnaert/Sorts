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
