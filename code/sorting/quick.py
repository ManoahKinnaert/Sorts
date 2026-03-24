from sorting.utils import exchange, less, Counter

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