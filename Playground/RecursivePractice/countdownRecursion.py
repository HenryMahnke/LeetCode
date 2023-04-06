def countdown(n):
    print(n)
    if n == 1:
       return 1
    else:
        countdown(n-1)

countdown(5)