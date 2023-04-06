def factorial(n):
    if(n ==1):
        return 1
    else: 
        return n* factorial(n-1)
    
# this works by first saying, for exmaple starting at 4
# 4* factorial 3
# which results in 4* [3* factorial 2] - unresolved
# 4*[3*2*1]
# is will then resolve and do 1*2
# 3*2
# and finally 4*6 once it gets back through the call stack
print(factorial(4))