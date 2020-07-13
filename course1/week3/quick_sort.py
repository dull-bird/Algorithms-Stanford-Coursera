from numpy.random import randint
from numpy import loadtxt
import numpy


def choose_pivot(L, l, r):
    # choose the pivot randomly
    p = randint(l, r)
    return p


def partition(L, p, l, r):
    L[p], L[l] = L[l], L[p]
    i = l + 1
    for j in range(l + 1, r):
        # c[0] += 1

        if L[j] < L[l]:
            L[i], L[j] = L[j], L[i]
            i += 1
    L[i - 1], L[l] = L[l], L[i - 1]
    # return the new position of pivot
    return i - 1


def quick_sort(L, l, r, mode):
    #print(l, r)
    # count_comp = 0
    if r - l <= 1:  # base case, only 0 or 1 element
        return
    else:
        # count_comp += r - l - 1 # number of elements - 1
        # p is the position of the pivot
        p = choose_pivot(L, l, r, mode)
        # update p
        p = partition(L, p, l, r)
        quick_sort(L, l, p, mode)
        quick_sort(L, p + 1, r, mode)
        return


if __name__ == "__main__":
    data = loadtxt("./course1/week3/QuickSort.txt")
    L = data.tolist()
    quick_sort(L, 0, len(L))
    [print(i) for i in L]
