import sys

n, m = [int(item) for item in sys.stdin.readline().split()]
tree_heights = [int(item) for item in sys.stdin.readline().split()]

def solution(m, tree_heights):
    left, right = 0, max(tree_heights)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        total_length = 0
        
        for h in tree_heights:
            if h > mid:
                total_length += h - mid
        
        if total_length >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(solution(m, tree_heights))