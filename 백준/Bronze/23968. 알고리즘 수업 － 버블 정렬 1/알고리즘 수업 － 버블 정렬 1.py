import sys

n, k = [int(item) for item in sys.stdin.readline().split()]
arr_A = [int(item) for item in sys.stdin.readline().split()]

def bubble_sort(n, k, arr_A):
    count = 0
    
    if n*(n+1)//2 < k:
        return -1

    for last in range(n, 1, -1):
        for i in range(1, last):
            if arr_A[i-1] > arr_A[i]:
                arr_A[i-1], arr_A[i] = arr_A[i], arr_A[i-1]
                count += 1
                if count == k:
                    return f'{arr_A[i-1]} {arr_A[i]}'
            
    return -1

print(bubble_sort(n, k, arr_A))