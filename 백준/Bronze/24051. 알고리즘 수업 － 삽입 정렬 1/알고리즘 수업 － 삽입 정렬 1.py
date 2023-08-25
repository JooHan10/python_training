import sys

n, k = [int(item) for item in sys.stdin.readline().split()]
arr_A = [int(item) for item in sys.stdin.readline().split()]

def insertion_sort(n, k, arr_A):
    count = 0
    
    for i in range(1, n):
        loc = i-1
        newItem = arr_A[i]

        while loc >= 0 and newItem < arr_A[loc]:
            count += 1
            arr_A[loc+1] = arr_A[loc]
            loc -= 1
            if count == k:
                return arr_A[loc+1]
            
        if loc+1 != i:
            arr_A[loc+1] = newItem
            count += 1
            if count == k:
                return arr_A[loc+1]
            
    return -1

print(insertion_sort(n, k, arr_A))