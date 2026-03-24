from sorting.utils import less, exchange, Counter 

def sort(my_list: list, counter: Counter):
    n = len(my_list)
    for i in range(1, n):
        j = i
        while j > 0 and less(my_list[j], my_list[j - 1], counter):
            exchange(my_list, j, j - 1, counter) 
            j -= 1