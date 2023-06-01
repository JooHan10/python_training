def solution(price, money, count):
    expense = 0
    
    for n in range(1, count+1):
        expense += price*n
    
    if expense-money > 0:
        return expense-money
    else:
        return 0