def solution(s):
    result = []
    cnt = 0     
    zero_cnt = 0
    
    while True:
        if s == "1":
            break;
            
        zero_cnt += s.count("0")
        s = s.replace("0",'')
        s = bin(len(s))[2:]
        
        cnt +=1
        
    result = [cnt, zero_cnt]    
    return result