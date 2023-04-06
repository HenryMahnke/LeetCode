def Fibonnaci(n):
    if n<=1:
        return n
    else:
        return Fibonnaci(n-1) + Fibonnaci(n- 2)
    
    

print(Fibonnaci(5))