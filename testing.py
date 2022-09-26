from re import L
import z3
import numpy as np
import pyautogui
import time


'''USrev=np.matrix([[1,2]
                ,[3,4]
                ,[5,6]])

multiply75= np.matrix([[4,8,5]
                      ,[5,2,5]])
'''
'''x=z3.Int('x')
y=z3.Int('y')
solve = z3.Solver()

solve.add(x+2*y==7)
solve.add(x > 7)
solve.add(y<6)
 

if solve.check() == z3.sat:
    print(solve.model)
    print(solve.model())

'''
'''
def binary_search(array,target):
    first = 0
    last = len(array)-1
    while first <= last:
        middle = (first + last)//2
        if array[middle]==target:
            print(middle)
            return middle
        elif array[middle] > target:
            last = middle-1
        else:
            first=middle + 1
    
    return None
#a = [1,2,3,4,5,6,7,8,9,10]
#binary_search(a,9)

def Greatest_Common_Divisor(a,b):
    
    while a !=b:
        if a > b:
            a = a-b
        else:
            b=b-a
    #print(a)
    return a

    
            
#Greatest_Common_Divisor(23,32)

def Friendly_or_not(c):
    d=str(c)[::-1]
    d=int(d)
    c=int(c)
    a=Greatest_Common_Divisor(c,d)
    if a==1:
        return True
    else:
        return False


    
list_num=[]


def Friendly_numbers(a,b):
    #n=abs(a-b)
    if a < b:
        while a < b:
            if Friendly_or_not(a) == True:
                list_num.append(a)
            a+=1
    elif a > b:
        while a > b:
            if Friendly_or_not(b) == True:
                list_num.append(b)
            b+=1
    else:
        print("No.")
    
    print(list_num)

Friendly_numbers(10,40)
def min_array(a):

    min = a[0]
    for i in range(0,len(a)):
        if (a[i]<min):
            min=a[i]
    return min

def max_array(a):
    max = a[0]
    for i in range(0,len(a)):
        if (a[i]>max):
            max=a[i]
    return max

def count_array(a,n):
    i=0
    s=0
    while i < len(a):
        if n==a[i]:
            s+=1
        i+=1
    return s

            


def FreqArray(a):
    min=min_array(a)
    max=max_array(a)
    #a=a.sort()
    #BasedArray=[]
    FreqArray=[]
    while min <= max:
        
        #i=0
        #num=0
        b=a.count(min)
        if b > 0:
            FreqArray.append(b)
        min+=1
    print(FreqArray)
    return FreqArray

def Remove_Repeated_Values(a):
    a.sort()
    result=[]
    for i in a:
        if i not in result:
            result.append(i)
    print(result)
    return result


def Group(a):
    sum_groups=0
    Freq=FreqArray(a)
    Based=Remove_Repeated_Values(a)
    i=0
    while i < len(Freq):
        sum_groups+=Freq[i]/Based[i]
        i+=1
    return sum_groups

       

ar=[1,1,1,2,2,3,3,3,3,3,3,2,2,2,2,4,4,4,4]
#print(a)
#print(FreqArray(ar))
#print(Remove_Repeated_Values(ar,3))

print(Group(ar))
    
'''
def AAAAAAAA(a,b,c,d):
    e=c-d
    if e < b:    
        l=0
        while a >= c:
            a=a-e
            l+=1
        while a >= b:
            a=a-b
            l+=1
    elif e >= b:
        l=a//b
    print(l)

def AAAAAAAA2(a,b,c,d):
    g=0
    l=0
    e=c-d
    if e <= b: 
        g+=(a-c)//e +1
        a=a-e*g
        l+=(a//b)+g
        print(g)

    elif e >= b:
        l=a//b
    print(l)


AAAAAAAA2(20,3,10,8)


