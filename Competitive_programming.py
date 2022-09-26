import math
from re import A


# Tích Bốn Số (Product of 4 numbers)
'''with open('TBS.inp', 'r') as fileInp:
    inp = fileInp.read()
File=inp.splitlines()
numbers =' '.join(File)
a,b,c,d=map(float,numbers.split())

g=a*b*c*d
e=0

if g==0:
    e=0
elif g > 0:
    e=1
else:
    e=-1


print(e)
with open('TBS.out', 'w') as fileOut:
       fileOut.write(str(e))

fileInp.close()
fileOut.close()
'''
#Incomplete

'''with open('TBS.inp', 'r') as fileInp:
    inp = fileInp.read()
File=inp.splitlines()
File.sort()
numbers =' '.join(File)
a,b,c=map(float,numbers.split())

if a==b or b==c:
     with open('TBS.out', 'w') as fileOut:
       fileOut.write("NO")

if b/a == c/b:
    with open('TBS.out', 'w') as fileOut:
       fileOut.write("YES")
else:
    with open('TBS.out', 'w') as fileOut:
       fileOut.write("NO")

fileInp.close()
fileOut.close()
'''
#Find2LargestNumber

'''def print2largest(arr, arr_size):
 
    # There should be atleast
    # two elements
    if (arr_size < 2):
        print(" Invalid Input ");
        return;
 
    largest = second = -2454635434;
 
    # Find the largest element
    for i in range(0, arr_size):
        largest = max(largest, arr[i]);
 
    # Find the second largest element
    for i in range(0, arr_size):
        if (arr[i] != largest):
            second = max(second, arr[i]);
 
    if (second == -2454635434):
        return;
    else:
        return largest,second
#arr=[1,2,3,4,5,19,19]
#n=len(arr)
#rint(print2largest(arr,len(arr)))
'''
#better find 2 largest elements
'''
def Largest_And_Second_largest(ar):
    Largest=0
    Second_largest=0
    if len(ar)<2:
        print("Invalid Input ");
        return;
 
    Largest=max(ar)
    ar.remove(Largest)
    Second_largest=max(ar)

    return(Largest,Second_largest)
 '''

#Tích Lớn nhất (Largest Product)
'''with open('TBS.inp', 'r') as fileInp:
    inp = fileInp.read()
File=inp.splitlines()
#File.sort()
numbers =' '.join(File)
a,b,c, M=map(int,numbers.split())

numbers = [a*b,b*c,c*a]

d=max(numbers)
f=d % M
f=int(f)
with open('TBS.out', 'w') as fileOut:
       fileOut.write(str(f))
 
# create a list
'''

#Dãy Kí Tự(List of symbols)
'''with open('TBS.inp', 'r') as fileInp:
    inp = fileInp.read()
a=int(inp)
Alphabet = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z"
}

n=a*(a+1)/2
d=n%26

out=Alphabet[d]

with open ('TBS.out', 'w') as fileOut:
    fileOut.write(out)

'''
#Way too unoptimized to use this function.
'''
n=input()
n=int(n)
d = {}
for x in range(0,n):
    d["var{0}".format(x)] = input()

def Find(n):
    # Initialize answer variable
    ans=0
    # Iterate over all possible values of y
    y = n + 1
    while(y <= n * n + n):
 
        # For valid x and y,
        # (n*n)%(y - n) has to be 0
        if ((n * n) % (y - n) == 0):
             
            # Increment count of ordered pairs
            ans += 1
 
        y += 1
 
    # Print the answer
    print(str(ans))

i=0
while i <n:
    Find(int(d["var"+str(i)]))
    i=i+1
'''
'''
with open('TBS.inp', 'r') as fileInp:
    inp = fileInp.read()
a=str(inp)

def toString(List): 
    return ''.join(List) 
  
# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def Remove_Repeated_Values(a):
    #a.sort()
    result=[]
    for i in a:
        if i not in result:
            result.append(i)
    #print(result)
    return result
def Remove_Non_Divisible_by_30_Values(a):
    #a.sort()
    result=[]
    for i in a:
        
        if i%30 ==0:
            result.append(i)
    #print(result)
    return result

def Return_to_int(test_list):
    for i in range(0, len(test_list)):
        test_list[i] = int(test_list[i])
arr=[]
def permute(a, l, r): 
    if l==r: 
        arr.append(toString(a))
    else: 
        for i in range(l,r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]

permute(list(a), 0, len(a))
b=Remove_Repeated_Values(arr)
b = [int(i) for i in b]

b=Remove_Non_Divisible_by_30_Values(b)
if len(b)==0:
    with open ('TBS.out', 'w') as fileOut:
        fileOut.write("-1")
else:
    out=max(b)
    with open ('TBS.out', 'w') as fileOut:
         fileOut.write(str(out))
'''
'''
n=9
x=1
y=0
sum=0
while x <= n:
    while y< x:
        a=(x+y)*(x-y+1)
        if a == n:
            sum+=1
            y+=1
        else:
            y+=1
    x+=1

print(y,x)
#print(x)
'''
'''
with open('TBS.inp', 'r') as fileInp:
    inp = fileInp.read()
File=inp.splitlines()
#File.sort()
numbers =' '.join(File)
s1,v1,s2,v2=map(int,numbers.split())
if v1==v2:
    out=-1
    with open ('TBS.out', 'w') as fileOut:
         fileOut.write(str(out))
if v1 !=v2:
    t=(-s1+s2)/(v1-v2)

    if t < 0:
        out=-1
    elif t >0:
        out=t
        out=int(out)
    with open ('TBS.out', 'w') as fileOut:
            fileOut.write(str(out))
'''
'''
a,b=input().split()
c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if a==c and b==d:
    print("Coincident")
elif a==c and b!=d:
    print("Parallel")
elif a!=c:
    x=(d-b)/(a-c)
    y=x*a+b
    x=str(x)
    y=str(y)
    print('Intersect', x, y) 
'''

'''
a,b=input().splitlines()
a=int(a)
b=int(b)

def gcd(a, b):
 
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)


if b == 0:
    print("INVALID")
if b !=0:
    if a%b ==0 :
        c=a/b
        c=int(c)
        print(c)

    if a%b !=0:

        e=gcd(a,b)
        #print(e)
        a = a/e
        b = b/e
        
        if b < 0:
            a = a*-1
            b = b*-1
        a=int(a)
        b=int(b)
        print(a,b)
'''
'''
a,b=input().split()

a=int(a)
b=int(b)
def getSum(n):
    
    sum = 0
    for digit in str(n): 
        sum += int(digit)      
    return sum

def isPrime(adg):
    for i in range(2, adg):
        if (adg % i) == 0:
            return False
    else:
         return True


ar=[]
def prime(l,v):
    for num in range(l, v + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                ar.append(num)

prime(a,b)
sum=0
for n in ar:
    
    a=getSum(str(n))
    if isPrime(a) == True:
        sum+=1
print(sum)
'''
def findLastNumber(n):
    n=str(n)
    a=n[-1]
    print(a)
    return a

A=input().splitlines()
print(A)