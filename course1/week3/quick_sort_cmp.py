from numpy.random import randint
from numpy import loadtxt
import numpy

def choose_pivot(L, l, r, mode):
    #choose the pivot randomly
    #p = randint(l, r)
    #print(p)

    p1 = l
    p3 = r - 1
    p2 = (l + r - 1)//2
    
    if mode == "first":
        return l
    elif mode == "last":
        return r - 1
    else: # median of three
        med = int(numpy.median([L[p1], L[p2], L[p3]]))
        for i in [p1, p2, p3]:
            if L[i] == med:
                break
        return i


def partition(L, p, l, r):
    L[p], L[l] = L[l], L[p]
    i = l + 1
    for j in range(l + 1, r):
        # c[0] += 1

        if L[j] < L[l]:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[i - 1], L[l] = L[l], L[i - 1]
    #return the new position of pivot
    return i - 1

def quick_sort(L, l, r, mode):
    #print(l, r)
    count_comp = 0
    if r - l <= 1: # base case, only 0 or 1 element
        return 0
    else:
        count_comp += r - l - 1 # number of elements - 1
        # p is the position of the pivot
        p = choose_pivot(L, l, r, mode)
        # update p
        p = partition(L, p, l, r)
        count_comp += quick_sort(L, l, p, mode)
        count_comp += quick_sort(L, p + 1, r, mode)
        return count_comp

if __name__ == "__main__":
    data = loadtxt("./course1/week3/QuickSort.txt")
    L = data.tolist()

    c1 = quick_sort(L.copy(), 0, len(L), mode="first")
    print(c1)
    
    c2 = quick_sort(L.copy(), 0, len(L), mode="last")
    print(c2)
    
    c3 = quick_sort(L.copy(), 0, len(L), mode="median")
    print(c3)
    
