def count_evens(L):
    s = 0
    for num in L:
        if num % 2 == 0:
            s += 1
    return s

