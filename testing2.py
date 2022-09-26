import math
from weakref import ref



def fib(n):
    a=0
    c=0
    b=1
    i=1
    while i <= n:
        c=b
        b=b+a
        a=c
        i+=1
    print(a)

    
def fub(n,memo={}):
    if n in memo: return memo[n]
    if n<=2:
        return 1    
    memo[n]= fub(n-1, memo) + fub(n-2, memo)
    return memo[n]

def re_factorial(n):
    if n <= 1:
        return 1
    
    return re_factorial(n-1) * n

def factorial(a):
    i=1
    ans=1
    while i <= a:
        
        ans*=i
        i=i+1
        #print(i)
    print(ans)

import sys

locate_python = sys.exec_prefix

print(locate_python)

#print(re_factorial(4))




tuổi = 16
x=20
