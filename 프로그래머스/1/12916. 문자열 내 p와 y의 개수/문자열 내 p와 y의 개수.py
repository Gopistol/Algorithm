def solution(s):
    answer = True
    
    p = 0
    y = 0
    s = s.lower()
    
    for i in range(len(s)):
        v = s[i]
        
        if v == "p":
            p = p + 1
        if v == "y":
            y = y + 1

    return p == y