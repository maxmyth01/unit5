#Max Low
#11-29-17
#quick sort -- pick a piviot point then move all smaller values to left and all larger values to right then repeat with one of the two subsets

#Max Low
#11-27-17
#cocktailSort.py -- implementaio of cocktail Sort

#Sam Smedinghoff
#11/15/17
#sorting.py - code to test a sorting function

from random import randint
from time import time

N = 100 #how many numbers will be sorted
"""
algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p - 1 )
        quicksort(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo - 1    
    for j := lo to hi - 1 do
        if A[j] < pivot then
            i := i + 1
            swap A[i] with A[j]
    if A[hi] < A[i + 1] then
        swap A[i + 1] with A[hi]
    return i + 1
"""
def mySort(A):
    def quicksort(A, lo, hi):
        if lo < hi:
            p = partition(A, lo, hi)
            quicksort(A, lo, p - 1)
            quicksort(A, p+1, hi)

    def partition(A, lo, hi):
        pivot = A[hi]
        i = lo - 1
        for j in range(lo,hi):
            if A[j] < pivot:
                i = i+=1
                A[i], A[j] = A[j],A[i]
            if A[hi] < A[i+1]:
                A[i+1], A[hi] = A[hi],A[i+1]
            return i+1
        
"""
    swapped = True
    while swapped:
        swapped = False
        for i in range(0,len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1],A[i] # swap in Python
            swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(len(A)-2,-1,-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1],A[i] # swap in Python
                swapped = True
    return A
"""

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
        

