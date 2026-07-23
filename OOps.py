"""class arithmetic_operations:
    '''Add,sub,mul,div'''
    def sum(self):
        a=int(input())
        b=int(input())
        print(a+b)
    def sub(self):
        a=int(input())
        b=int(input())
        print(a-b)
    def mul(self):
        a=5
        b=4
        print(a*b)
    def div(self):
        a=9
        b=3
        print(a/b)
obj1=arithmetic_operations()
obj1.sum()
obj1.sub()
obj2=arithmetic_operations()
obj2.mul()
obj2.div()
help(arithmetic_operations)
print(arithmetic_operations.__doc__)"""

# Constructor of class

"""class vmtw:
    def __init__(self):
        self.name="Harsha"
        self.cls = "Batch 5"
        self.a=10
    def display(self):
        print(self.name)
        print(self.cls)
        print(self.a)
    def show(self):
        print(self.a)
obj=vmtw()
obj.display()
obj.show()
"""
# Example
'''
class Mobile:
    def __init__(self,brand,storage,price):
        self.name=brand
        self.st=storage
        self.p=price
    def display(self):
        print(self.name)
        print(self.st)
        print(self.p)
m1=Mobile("Pixel","256GB",50000)
m1.display()
print()
m2=Mobile("Redmi","128GB",25000)
m2.display()
'''

# Example2
'''
class Employee:
    def __init__(self,em_name,em_location,em_salary,em_dept):
        self.name=em_name
        self.loc=em_location
        self.sal=em_salary
        self.dep=em_dept
    def display(self):
        print(self.name)
        print(self.loc)
        print(self.sal)
        print(self.dep)
e1 = Employee("Harsha","Hyd",25000,"CSE")
e1.display()
print()
e2 = Employee("Hari","Hyd",30000,"CS")
e2.display()
print()
e3 = Employee("Bhargav","Hyd",50000,"Robotics")
e3.display()
'''
#Example 3
'''
class Laptop:
    def __init__(self,brand,OS,Version,price,storage,size):
        self.br=brand
        self.os=OS
        self.vs=Version
        self.p=price
        self.si=size
    def show(self):
        print(self.br)
        print(self.os)
        print(self.vs)
        print(self.p)
        print(self.si)
l1=Laptop("Hp","Windows","i3",45000,"128GB","34x67")
l1.show()
l2=Laptop("Asus","Windows","i3",65000,"256GB","45x21")
l2.show()
'''
#Example3
'''
class Student:
    def __init__(self,n,r,m):
        self.name=n
        self.rollno=r
        self.marks=m
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)
s=Student("Harsha",524,7.2)
s.display()
print()
s1=Student("Hari",519,8.1)
s1.display()
print()
s2=Student("Bhargav",521,9.2)
s2.display()
print()
'''
#Instance variables
'''
class Movie:
    def __init__(self,hero,b,h,v):
        self.hero=hero
        self.b=b
        self.h=h
        self.v=v
    def show(self):
        print(self.hero)
        print(self.b)
        print(self.h)
        print(self.v)
    def mainlead(self):
        print(self.hero)
        print(self.h)
        print(self.v)
m1=Movie("Prabhas","420cr","Anushka","Rana")
m1.show()
print()
m1.mainlead()
print()
print(m1.hero)
print(m1.v)
print(m1.b)
'''
#Static variables
'''
class Bike:
    brand='Pulsar'
    def display(self):
        print(Bike.brand)
b=Bike()
b.display()

b1=Bike()
b1.display()
'''
#Local variables
'''
class A:
    def __init__(self):
        self.name="name"
        self.rollno=8976
    def display(self):
        print(self.name)
        a=10
        print(a)
    def show(self):
        print(a)
ob=A()
ob.display()#name,10
ob.show()

'''
#Types of methods in Python class

class cl:
    def __init__(self,n,r):
        self.name=n
        self.rn=r
    def m1(self):
        print(self.name)
        print(self.rn)
    def m2(self):
        self.m1()
ob=cl("Hari",524)
ob.m1()
ob.m2()

#Instance Method (Ex:1)
'''
class marks:
    def __init__(self,n,m,r,):
        self.name=n
        self.marks=m
        self.r=r
    def grade(self):
        if self.marks>95:
            print(self.name,self.marks,self.r,"Grade:A")
        elif self.marks>65:
            print(self.name,self.marks,self.r,"Grade:B")
        elif self.marks>45:
            print(self.name,self.marks,self.r,"Grade:C")
        else:
            print(self.name,self.marks,self.r,"Grade:Fail")
    def display(self):
        self.grade()
ob=marks("Harsha",89,524)
ob.display()
ob1=marks("Hari",45,567)
ob1.display()
ob2=marks("Bhargav",97,512)
ob2.display()
'''

#Ex:2
'''
class marks:
    def __init__(self,n,m1,m2,r):
        self.name=n
        self.marks1=m1
        self.marks=m2
        self.r=r
        self.avg=(m1+m2)//2
    def grade(self):
        if self.marks>95:
            print(self.name,self.marks,self.r,"Grade:A","  Avg:",self.avg)
        elif self.marks>65:
            print(self.name,self.marks,self.r,"Grade:B","  Avg:",self.avg)
        elif self.marks>45:
            print(self.name,self.marks,self.r,"Grade:C","  Avg:",self.avg)
        else:
            print(self.name,self.marks,self.r,"Grade:Fail"," Avg:",self.avg)
    def display(self):
        self.grade()
ob=marks("Harsha",89,45,524)
ob.display()
ob1=marks("Hari",45,45,567)
ob1.display()
ob2=marks("Bhargav",90,90,512)
ob2.display()
'''
#Static Method
'''
class A:
    def m1(self):
        print("Hi")
    @staticmethod
    def m2():
        print("Hello")
    def m3(self):
        A.m2()
ob=A()
ob.m2()
ob.m3()
'''
#Decorators
'''
def f1(func):
    def f2():
        print("Hello World")
        func()
    return f2
@f1
def f3():
    print("Sai")
f3()'''

#
'''
class vmtw:
    def __init__(self):
        pass
    def m1(self):
        print("Hello welcome to hyd")
class A:
    def m2(self):
        print("Hello")
ob=vmtw()
ob.m1()
s1=A.m2(ob)#class parameter(ob),code reusability
'''
'''
class vmtw:
    def __init__(self,n,b,s):
        self.name=n
        self.branch=b
        self.s=s
    def m1(self):
        print(self.name)
class A:
    def m2(self):
        print(self.name)
        print(self.branch)
    def m3(self):
        print(self.s)
ob=vmtw("Harsha","CSE","A")
ob.m1()
ob2=vmtw("Hari","ECE","B")
s1=A.m2(ob2)
s2=A.m3(ob)
'''
#Inner class in python
'''
class Car:
    def m1(self):
        print("this is m1() from class car")
    class Engine:
        def m2(self):
            print("this is m2() from class Engine")
ob=Car()
ob.m1()
s=Car().Engine().m2()'''
    
#PILLARS OF OOPS

###Inheritance
'''
class parent:
    def __init__(self):
        self.name="Nithya"
        self.branch="CSE"
    def display(self):
        print(self.name,self.branch)
    def m1(self):
        print("m1()")
class Child(parent):
    def show(self):
        print(self.name,self.branch)
ob=Child()
ob.show()
ob.display()
'''
#Example 2(Using variables)
'''
class parent:
    c=10
    d=20
    def __init__(self):
        self.name="hari"
        self.branch="CSE"
    def display(self):
        print(self.name,self.branch)
    def show(self):
        print(self.name,self.branch)
class child(parent):
    pass
ob=child()
print(ob.c)
print(ob.d)
ob.display()
ob.show()
'''
#PARENT ClASS - CHILD CLASS constructors

'''purpose of self,init
how many constructors?/
diff b/w constructor and method
class nd obj difference(properties...with code)
Diff b/w OOps and structured prog'''

#case1:
'''
class parent:
    def __init__(self):
        self.name="Nithya"
        self.branch="CSE"
    def display(self):
        print(self.name,self.branch)
class Child(parent):
    def __init__(self):
        self.addr="Hyd"
        self.mobile=8977876
    def show(self):
        print(self.name,self.branch)
ob=Child()
ob.show()
ob.display()
'''
#constructor with super method
'''
class emp1:
    def __init__(self,n,d):
        self.n=n
        self.d=d
    def display(self):
        print(self.n,self.d)
class emp(emp1):
    def __init__(self,sal,loc,n,d):
        super().__init__(n,d)
        self.sal=sal
        self.loc=loc
    def show(self):
        print(self.sal,self.loc)
a=emp(45000,"Hyd","Harsha","CSE")
a.show()
a.display()
b=emp(35900,"Blr","Kittu","Blr")
b.show()
b.display()'''

#recursion
'''
def m1():
    print("heloo")
m1()
'''
'''
def m1(a):
    if a>30:
        return
    else:
        print(a)
        a=a+3
    m1(a)
a=3
m1(a)
'''
#Recursion types
#Direct recursion
# Tail recursion
'''
def fun(n):
    if n>=1:
        print(n)
        fun(n-1)
    else:
        return 0
n=9
fun(n)
print()
'''
#Head recursion
'''
def fun(n):
    if n>=1:
        fun(n-1)
        print(n)
    else:
        return 0
n=9
fun(n)
print()
'''
#Tree Recursion
'''
def fun(n):
    if n>0:
        print(n,end=" ")
        fun(n-1)
        fun(n-1)
        fun(n-1)
fun(3)
'''
#Nested recursion''
'''f
def fun(n):
    if(n>100):
        return n-10
    return fun(fun(n+11))
r=fun(95)
print(r)
'''
# Indirect recursion
'''
def funA(n):
    if n>0: 
        print(n,end=" ")
        funB(n-1)
def funB(n):
    if n>1:
        print(n,end="")
        funA(n//2)
funA(20)
'''

# Dynamic Programming
    ##merge sort
'''
def mergeSort(a,n):
    if n==1:
        return
    l=[]
    r=[]
    mid=n//2
    for i in range(mid):
        l.append(a[i])
    for i in range(mid,n):
        r.append(a[i])
    mergeSort(l,mid)
    mergeSort(r,n-mid)
    min(a,l,r,mid,n-mid)
    
def merge(a,l,r,left,right):
    i=0
    j=0
    k=0
    while i<left and j<right:
        if l[i]<r[j]:
            a[k]=l[i]
            i+=1
            k+=1
        else:
            a[k]=r[j]
            j+=1
            k+=1
    while i<left:
        a[k]=l[i]
        i+=1
        j+=1
        k+=1
    while i<right:
        a[k]=r[j]
        j+=1
        k+=1
n=int(input())
a=list(map(int,input().split()))
print("BS")
print(*a)
mergeSort(a,n)
print("AS")
print(*a)
'''

##Quick sort
'''
def quicksort(a,lindex,rindex):
    if lindex>=rindex:
        return
    lp=lindex
    rp=rindex
    pivot=a[rindex]
    while lp<rp:
        while a[lp]<=pivot and lp<rp:
            lp=lp+1
        while a[rp]>=pivot and lp<rp:
            rp=rp-1
        a[lp],a[rindex]=a[rindex],a[lp]
        quicksort(a,lindex,lp-1)
        quicksort(a,lp+1,rindex)
n=int(input())
a=list(map(int,input().split()))
print("BS")
print(*a)
quicksort(a,0,n-1)
print("AS")
print(*a)  
'''
#Stack using list
'''
class Stack:
    def __init__(self):
        self.a=[]
    def push(self,x):
        if len(self.a)==n:
            print("Stack is overflow")
            return
        self.a.append(x)
    def pop(self):
        if len(self.a)==0:
            print("Stack is underflow")
            return
        print(self.a[-1],"is deleted")
        self.a.pop()
    def show(self):
        if len(self.a)==0:
            print("Stack is empty")
            return
        for i in range(len(self.a)-1,-1,-1):
            print(self.a[i],end=" ")
        print()
n=int(input("Enter size of stack"))
s1=Stack()
while True:
    print("1.Push\n2.Pop\n3.print\n4.Exit")
    ch = int(input("Enter your choice"))
    if ch==1:
        x=int(input("Enter element"))
        s1.push(x)
    elif ch==2:
        s1.pop()
    elif ch==3:
        s1.show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#Implementation of stack using linked list
'''
class Stack:
    def __init__(self):
        self.top=None
    def push(self,x):
        n=Node(x)
        if self.top==None:
            self.top=n
        else:
            n.next=self.top
            self.top=n
    def pop(self):
        if self.top==None:
            print("Stack is underflow")
            return
        print(self.top.data,"is deleted")
        self.top=self.top.next
    def show(self):
        if self.top==None:
            print("Stack is empty")
            return
        tem=self.top
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
s1=Stack()
while True:
    print("1.Push\n2.Pop\n3.Print\n4.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        x=int(input("Enter element"))
        s1.push(x)
    elif ch==2:
        s1.pop()
    elif ch==3:
        s1.show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#Implementing of stack using dequeue class:
'''
from collections import deque
s1=deque()
while True:
    print("1.Push\n2.Pop\n3.Print\4.Exit")
    ch=int(input("enter element"))
    if ch==1:
           x=int(input("Enter element"))
           s1.append(x)
    elif ch==2:
        if s1:
            print(s1.pop(),"is deleted")
        else:
            print("Stack is underflow")
    elif ch==3:
        r=s1.copy()
        r.reverse()
        print(*r)
    elif ch==4:
        break
    else:
        print("Invalid choice")
        '''
#
'''
def checkBalanced(s):
    stack=[]
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            r=stack.pop()
            if r=='(':
                if ch!=')':
                    return False
            elif r=='[':
                if ch!=']':
                    return False
            elif r=='{':
                if ch!='}':
                    return False
    if stack:
        return False
    return True
s=input()
if checkBalanced(s):
    print("Balanced")
else:
    print("Unbalanced")
'''
'''
def pre(ch):
    if ch in "/*":
        return 2
    elif ch in "+-":
        return 1
    else:
        return 0
n=input()
post=""
op=[]
for i in s:
    if i .isalnum():
        post=post+i
    else:
        if len(op)==0:
            op.append(i)
        else:
            while op and pre(i)<=pre(op[-1]):
                pospost=top.pop()
                op.append(i)
while op:
    post=post+op.pop()
print(post)
'''
#stack using deque class
'''
def process(op1,op2,op):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2
    elif op=='/':
        return op1/op2
s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
    else:
        op2=int(a.pop())
        op1=int(a.pop())
        res=process(op1,op2,i)
        a.append(res)
print(a.pop())
'''
#Reverse string using stack
'''
s=input()
a=[]
for i in s:
    a.append(i)
while a:
    print(a.pop(),end=" ")
'''

##QUEUES
'''
"A Queue is an ordered list in which insertions are done at one end (rear) and deletions are done at other end(front).The ffirst element to be inserted is the first one to be deleted.Hence,it is called FIFO or LILO list"
"When an element is inserted in a queue,the concept is called Enqueue,and when an element is removed from the queue,the conecpts is called as Dequeue"
#APPLICATIONS
1. An imp app of queue is time sharing system of computer CPU
2.OS scheduled jobs(with equal priority)in the order of arrival
3.Simulation of real world queues such as lines at a ticket counter or any other first come first served scenario requires a queue
4.Asynchronous data transfer(file IO,pipes,sockets)
5.Queues are used in breadth first traversal (BFS) of graph
'''
#Implement queue operations using List
'''
class Queue:
    def __init__(self):
        self.a=[]
    def enqueue(self,x):
        if len(self.a)==n:
            print("Queue is full")
            return
        self.a.append(x)
    def dequeue(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        print(self.a.pop(0),"is deleted")
    def show(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        for i in self.a:
            print(i,end=" ")
        print()
n=int(input("Enter size of queue:"))
q1=Queue()
while True:
    print("1.Enqueue\n2.Dequeue\n3.Print\n4.Exit")
    ch = int(input("Enter choice:"))
    if ch==1:
        x=int(input("Enter element:"))
        q1.enqueue(x)
    elif ch==2:
        q1.dequeue(x)
    elif ch==3:
        q1.show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
# Implementation of queue using linked list
'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Queue:
    def __init__(self):
        self.root=self.tail=None
    def enqueue(self,x):
        n=Node(x)
        if self.root==None:
            self.root=self.tail=n
        else:
            self.tail.next=n
            self.tzil=n
    def dequeue(self):
        if self.root==None:
            print("Queue is empty")
            return
        self.root=self.root.next
    def show(self):
        if self.root==None:
            print("Queue is empty")
            return
        temp=self.root
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
n=int(input("Enter size of queue:"))
q1=Queue()
while True:
    print("1.Enqueue\n2.Dequeue\n3.Print\n4.Exit")
    ch = int(input("Enter choice:"))
    if ch==1:
        x=int(input("Enter element:"))
        q1.enqueue(x)
    elif ch==2:
        q1.dequeue()
    elif ch==3:
        q1.show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#Implementation of dequeue operations using list
'''
class Dequeue:
    def __init__(self):
        self.a=[]
    def enqueueFirst(self,x):
        if len(self.a)==n:
            print("Queue is full")
            return
        self.a.insert(0,x)
    def enqueueLast(self,x):
        if len(self.a)==n:
            print("Queue is full")
            return
        self.a.append(x)
    def dequeueFirst(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        print(self.a.pop(0),"is deleted")
    def dequeueLast(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        print(self.a.pop(),"is deleted")
    def show(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        for i in self.a:
            print(i,end=" ")
        print()
n=int(input("Enter size of queue:"))
q1=Dequeue()
while True:
    print("1.Enqueue First\n2.Enqueue Last\n3.Dequeue First\n4.Dequeue Last\n5.Print\n6.Exit")
    ch = int(input("Enter choice:"))
    if ch==1:
        x=int(input("Enter element:"))
        q1.enqueueFirst(x)
    elif ch==2:
        x=int(input("Enter element:"))
        q1.enqueueLast(x)
    elif ch==3:
        x=int(input("Enter element:"))
        q1.dequeueFirst()
    elif ch==4:
        x=int(input("Enter element:"))
        q1.dequeueLast()
    elif ch==5:
        q1.show()
    elif ch==6:
        break
    else:
        print("Invalid choice")
'''
#Implement dequeue operations using dequeue class in collections module:
'''
from collections import deque
q1=Dequeue()
while True:
    print("1.Enqueue First\n2.Enqueue Last\n3.Dequeue First\n4.Dequeue Last\n5.Print\n6.Exit")
    ch = int(input("Enter choice:"))
    if ch==1:
        x=int(input("Enter element:"))
        q1.enqueueFirst(x)
    elif ch==2:
        x=int(input("Enter element:"))
        q1.enqueueLast(x)
    elif ch==3:
        x=int(input("Enter element:"))
        q1.dequeueFirst()
    elif ch==4:
        x=int(input("Enter element:"))
        q1.dequeueLast()
    elif ch==5:
        q1.show()
    elif ch==6:
        break
    else:
        print("Invalid choice")
'''

#PRIORITY QUEUE
'''
class PriorityQueue:
    def __init__(self):
        self.a=[]
    def enqueue(self,x):
        if len(self.a)==n:
            print("Queue is full")
            return
        self.a.append(x)
    def dequeue(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        print(max(self.a),"is deleted")
        self.a.remove(max(self.a))
    def show(self):
        if len(self.a)==0:
            print("Queue is empty")
            return
        for i in self.a:
            print(i,end=" ")
        print()
n=int(input("Enter size of queue"))
q1=PriorityQueue()
while True:
    print("1.Enqueue\n2.Dequeue\n3.Print\n4.Exit")
    ch = int(input("Enter choice:"))
    if ch==1:
        x=int(input("Enter element:"))
        q1.enqueue(x)
    elif ch==2:
        q1.dequeue()
    elif ch==3:
        q1.show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
        '''
#Problem(SORT A STACK)
'''
n=int(input())
a=list(map(int,input().split()))
a.sort()
res=[]
for i in a:
    res.append(i)
while res:
    print(res.pop(),end=" ")
    '''
#REDUNDANT BRACES
'''
class Stack:
    def __init__(self):
        self.a=[]
        self.b=[]
    def s1(self,s):
        for ch in s:
            if ch=="(":
                self.a.append(ch)
            elif ch==")":
                self.b.append(ch)
            else:
                return
    def show(self):
        for ch in s:
            if len(self.a)==len(self.b):
                print("yes")
            else:
                print("no")
s=input()
ob=Stack()
ob.show()
'''
'''
n=int(input())
a=list(map(int,input().split()))
first=0
for second in range(1,n):
    if a[first]!=a[second]:
        first+=1
        a[first]=a[second]
for i in range(first+1):
    print(a[i],end=" ")
'''
# Move zeroes to last
'''
n= int(input())
a=list(map(int,input().split()))
r=[]
c=0
for i in range(n):
    if a[i]!=0:
        r.append(a[i])
    else:
        c=c+1
r.extend([0]*c)
print(r)
'''
#Input: nums = [3,2,2,3], val = 3
'''Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores)''

n =int(input())
arr = list(map(int,input().split()))
r=[]
for i in range(len(arr)-1):
    if i!=n:
        r.append(i)
print(r)
'''
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
'''Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].''
arr= list(map(int,input().split()))
a=[]
for i in arr:
    a.append(i**2)
a.sort()
print(a)
'''
#Leet code 349
'''
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
a=[]
for i in nums1:
    for j in nums2:
        if i==j:'''
#Sub array of size K with given sum
'''
n=int(input())
a=list(map(int,input().split()))
k=int(input())
target=int(input())
for i in range(n-k+1):
    s=0
    for j in range(i,i-1,k):
        s=s+a[j]
    if s==target:
        print("Yes")
        print(*a[i:i+k])
        break
else:
    print("No")
    '''
#Optimized Approach
'''
n=int(input())
a=list(map(int,input().split()))
k=int(input())
target=int(input())
s=sum(a[0:k])
if s==target:
    print("Yes")
    print(*a[0:k])
else:
    for i in range(k,n):
        s=s+a[i]-a[i-k]
        if s==target:
            print("Yes")
            print(*a[i:i+k])
            break
        else:
            print("No")
            '''
# To find maximum sum of all sub arrays of size k
'''given array of integers of size n,Our aim is to calaculate the maximum sum of 'k'
consecutive elements in the array
I/P: arr[]={100,200,300,400},k=2
O/P:ArithmeticError''
n=int(input())
a=list(map(int,input().split()))
k=int(input())
maxsum=s=sum(a[0:k])
for i in range(k,n):
    s=s+a[i]-a[i-k]
    if s>maxsum:
        maxsum=s
print(maxsum)
'''
#Split an array into two equal sum sub arrays
'Given an array of integers greater than zero,find if it is possible to split it in two subarrays'
'such that the sum of two subarrays is the same.Print the two subarrays'
'''
m=int(input())
a=list(map(int,input().split()))
lsum=0
for i in range(n-1):
    lsum+=a[i]
    rsum=0
    for j in range(i+1,n):
        rsum=rsum+a[j]
    if lsum==rsum:
        print(*a[:i+1])
        print(*a[i+1:n])
        break
else:
    print(-1)
'''
#Hashing maps data(keys)-->values using a hash function for fast access(O(1)average))
'''Common structures:
Hash Map(Java)
unordered_map(C++)
dictionary(python)
hashtable(c)
''
s="language"
r={}
for i in s:
    r[i]=r.get(i,0)+1
print(r)
for i in r:
    print(i,r.get(i),sep="",end="")
'''
#First non repating char in string
'''
s='aabcdbecdr'
r={}
for i in s:
     r[i]=r.get(i,0)+1
for i in r:
    if r[i]==1:
        print(i)
        break
else:
    print("No such char")
'''
#Check if two arrays are equal or not(Using hashing)
'''
def equal(a,b):
    if len(a)!=len(b):
        return False
    freq={}
    for i in a:
        freq[i]=freq.get(i,0)+1
    for i in b:
        if i not in freq:
            return False
        freq[i]-=1
        if freq[i]==0:
            del freq[i]
    return len(freq)==0
a=[1,3,4,2]
b=[4,2,1,3]
if equal(a,b):
    print("equal")
else:
    print("not")
'''
#Print string anagram or not
'''
s1="hello"
s2="heo"
if sorted(s1)==sorted(s2):
    print("Anagram")
else:
    print("not")

#Using Hashing
def Hash(a,b):
    if len(a)!=len(b):
        return False
    freq={}
    for i in s1:
        freq[i]
'''
#print list ele with ele and index
'''
a=[34,12,75,45]
for i in range(len(a)):
    print(i,a[i])
print()
#or
for i,val in enumerate(a):
    print(i,val)
'''
#BINARY TREE REPRESENTATION
'''
"Each node is sequentially arranged from left to right and top to bottom.The numbering starts"
"from root node and remaining node are given with increasing numbers in level wise direction if the nodes are in"
"same in level,then numbers will be assignes from left to right"
            left(n)-->2n+1
            right(n)-->2n+2

                    A
                   / \
                  B   C
                 /\   /\
                D  E  F G
''
class BinaryTree:
    def __init__(self,size):
        self.tree=[-1 for i in range(size)]
        self.size=0
    def insert(self,x):
        if self.size>len(self.tree):
            print("binary is full")
            return
        self.tree[self.size]=x
        self.size+=1
    def show(self):
        print(*self.tree)
b1=BinaryTree(10)
while True:
    print("1.Insert\n2.Print\n3.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        x=int(input("enterelement"))
        b1.insert(x)
    elif ch==2:
        b1.show()
    elif ch==3:
        break
    else:
        print("Invalid choice")
'''
#LINKED LIST REPRESENTATION
#In linked list rep each node will be having three feilds
#1.leftpointer pointing to left subtree
#2.data actual content
#3.rightpointer pointing to right sub tree
'''
class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
    def insert(self,root,x):
        if root==None:
            root=Node(x)
            return
        n=[]
        n.append(root)
        while len(n)!=0:
            temp=n.pop(0)
            if temp.left==None:
                temp.left=Node(x)
                break
            else:
                n.append(temp.left)
                if temp.right==None:
                    temp.right=Node(x)
                    break
                else:
                    n.append(temp.right)
    def show(self):
        if self.left!=None:
            self.left.show()
        print(self.data,end=" ")
        if self.right!=None:
            self.right.show()
x=int(input("enter root node element"))
root=Node(x)
while True:
    print()
    print("1.Insert\n2.Print\n3.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        x=int(input("enterelement"))
        root.insert(x)
    elif ch==2:
          root.show()
    elif ch==3:
        break
    else:
        print("Invalid choice")
'''
#GRAPHS
#Undirected unweighted graph
'''
def addNode(v):
    global nodecount
    if v in nodes:
        print("Node is alrady existed")
    else:
        nodecount+=1
        nodes.append(v)
        for  n in graph:
            n.append(0)
        temp=[]
        for i in range(nodecount):
            temp.append(0)
        graph.append(temp)
def addEdge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not availaable")
    elif v2 not in nodes:
        print(v2,"is not available")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1
def show():
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
nodecount=0
nodes=[]
graph=[]
while True:
    print()
    print("1.Add node\n2.Add edge\n3.Print\n4.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        v=input("enter node")
        addNode(v)
    elif ch==2:
        v1=int(input("enter node1"))
        v1=int(input("enter node1"))
        addEdge(v1,v2)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid cboice")
        '''
#Directed Unweighted graph
'''
def addNode(v):
    global nodecount
    if v in nodes:
        print("Node is already existed")
    else:
        nodecount+=1
        nodes.append(v)
        for  n in graph:
            n.append(0)
        temp=[]
        for i in range(nodecount):
            temp.append(0)
        graph.append(temp)
def addEdge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not availaable")
    elif v2 not in nodes:
        print(v2,"is not available")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
def show():
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
nodecount=0
nodes=[]
graph=[]
while True:
    print()
    print("1.Add node\n2.Add edge\n3.Print\n4.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        v=input("enter node")
        addNode(v)
    elif ch==2:
        v1=int(input("enter node1"))
        v2=int(input("enter node2"))
        addEdge(v1,v2)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
        '''
#Undirected Weighted graph
'''
def addNode(v):
    global nodecount
    if v in nodes:
        print("Node is already existed")
    else:
        nodecount+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(nodecount):
            temp.append(0)
        graph.append(temp)
def addEdge(v1,v2,w):
    if v1 not in nodes:
        print(v1,"is not availaable")
    elif v2 not in nodes:
        print(v2,"is not available")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=w
        graph[index2][index1]=w
def show():
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
nodecount=0
nodes=[]
graph=[]
while True:
    print()
    print("1.Add node\n2.Add edge\n3.Print\n4.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        v=input("enter node")
        addNode(v)
    elif ch==2:
        v1=int(input("enter node1"))
        v2=int(input("enter node2"))
        w=int(input("Enter weight"))
        addEdge(v1,v2,w)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#Directed Weighted graph
'''
def addNode(v):
    global nodecount
    if v in nodes:
        print("Node is already existed")
    else:
        nodecount+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(nodecount):
            temp.append(0)
        graph.append(temp)
def addEdge(v1,v2,w):
    if v1 not in nodes:
        print(v1,"is not availaable")
    elif v2 not in nodes:
        print(v2,"is not available")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=w
def show():
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
nodecount=0
nodes=[]
graph=[]
while True:
    print()
    print("1.Add node\n2.Add edge\n3.Print\n4.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        v=input("enter node")
        addNode(v)
    elif ch==2:
        v1=int(input("enter node1"))
        v2=int(input("enter node2"))
        w=int(input("Enter weight"))
        addEdge(v1,v2,w)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#Undirected unweighted graph
'''
def addNode(v):
    global nodecount
    if v in nodes:
        print("Node is already existed")
    else:
        nodecount+=1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(nodecount):
            temp.append(0)
        graph.append(temp)
def addEdge(v1,v2):
    if v1 not in nodes:
        print(v1, "is not available")
    elif v2 not in nodes:
        print(v2,"is not available")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1
def show():
    for i in range(nodecount):
        for j in range(nodecount):
            print(graph[i][j],end=" ")
        print()
def deleteEdge(v1,v2):
    if v1 not in nodes:
        print(v1,"is not present")
    elif v2 not in nodes:
        print(v2,"is not present")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index]=0
        graph[index2][index1]=0
def deleteNode(v):
    global nodecount
    if v not in nodes:
        print(v,"is not present")
    else:
        ind=nodes.index(v)
        nodes.remove(v)
        nodecount-=1
        graph.pop(ind)
        for i in graph:
            i.pop(ind)
nodecount=0
nodes=[]
graph=[]
while True:
    print()
    print("1.Add Node\n2.Add Edge\n3.Print\n4.Delete Edge\n5.Delete Node\n6.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        v=input("enter node")
        addNode(v)
    elif ch==2:
        v1=int(input("enter node1"))
        v2=int(input("enter node2"))
        w=int(input("Enter weight"))
        addEdge(v1,v2,w)
    elif ch==3:
        show()
    elif ch==4:
        v1=input("Enter node1")
        v2=input("enter node2")
        deleteEdge(v1,v2)
    elif ch==5:
        v=input("enter node")
        deleteNode(v)
    elif ch==6:
        break
    else:
        print("Invalid Choice")
'''
#Adjaceny list
#Undirected unweighted graph
'''
def addNode(v):
    if v in graph:
        print(v,"is present in graph")
    else:
        graph[v]=[]
def addEdge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    elif v2 not in graph:
        print(v2,"is not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def show():
    for i in graph:
        print(i,":",graph[i])
graph={}
while True:
    print()
    print("1.Add Node\n2.Add Edge\n3.Print\n4.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        v=input("Enter node")
        addNode(v)
    elif ch==2:
        v1=input("Enter node1")
        v2=input("enter node2")
        addEdge(v1,v2)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#directed unweighted graph
'''
    def addNode(v):
    if v in graph:
        print(v,"is present in graph")
    else:
        graph[v]=[]
def addEdge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    elif v2 not in graph:
        print(v2,"is not present")
    else:
        graph[v1].append(v2)
def show():
    for i in graph:
        print(i,":",graph[i])
graph={}
while True:
    print()
    print("1.Add Node\n2.Add Edge\n3.Print\n4.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        v=input("Enter node")
        addNode(v)
    elif ch==2:
        v1=input("Enter node1")
        v2=input("enter node2")
        addEdge(v1,v2)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
#Undirected weighted graph
'''
def addNode(v):
    if v in graph:
        print(v,"is present in graph")
    else:
        graph[v]=[]
def addEdge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    elif v2 not in graph:
        print(v2,"is not present")
    else:
        r1=(v2,w)
        r2=(v1,w)
        graph[v1].append(r1)
        graph[v2].append(r2)
def show():
    for i in graph:
        print(i,":",graph[i])
graph={}
while True:
    print()
    print("1.Add Node\n2.Add Edge\n3.Print\n4.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        v=input("Enter node")
        addNode(v)
    elif ch==2:
        v1=input("Enter node1")
        v2=input("enter node2")
        addEdge(v1,v2)
    elif ch==3:
        show()
    elif ch==4:
        break
    else:
        print("Invalid choice")
'''
'''
n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
arr=[]
for i in arr1:
    if i!=0:
        arr.append(i)
for j in arr2:
    if j!=0:
        arr.append(j)
arr.sort()
print(arr)
'''
#Solution 1(TOP DOWN DP)
'''
def fib(n,memo={}):
    if n<=1:
        return n
    if n in memo:
        return memo[n]
    memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
n=int(input())
print(fib(n))
'''
#Solution 2(BOTTOM UP DP)
'''
def fib(n):
    if n<=1:
        return n
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=int(input())
print(fib(n))
'''
#Solution 3(Space Optimized DP)
'''
def fib(n):
    if n<=1:
        return n
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
    return b
n=int(input())
print(fib(n))
'''
#Leetcode 1137(Bruteforce approach)
'''
def trib(n):
    if n<=1:
        return n
    if n==2:
        return 1
    return trib(n-1)+trib(n-2)+trib(n-3)
n=int(input())
print(trib(n))
'''
#1137(DP approach)
'''
def trib(n):
    if n<=1:
        return n
    if n==2:
        return 1
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]+d[i-3]
    return dp[n]
n=int(input())
print(fib(n))
'''
#leetcode(70)Normal approach
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        if n==0:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
'''
#Brute force approach
'''
def ways(n,k):
    if n<0:
        return 0
    if n==0:
        return 1
    res=0
    for i in range(1,k+1):
        res+=ways(n-i,k)
    return res
n=int(input())
k=int(input())
print(ways(n,k))
'''
#Normal approach
'''
def ways(n,k):
    if n<0:
        return 0
    if n==0:
        return 1
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,k+1):
        dp[n]+=ways(n-i,k)
    return dp[n]
n=int(input())
k=int(input())
print(ways(n,k))
'''
#Normal approach
'''
def ways(coins, amount, ind):
    if amount<0:
        return 0
    if amount==0:
        return 1
    if ind==len(coins):
        return 0
    return ways(coins,amount-coins[ind],ind)+ways(coins,amount,ind+1)
coins = list(map(int, input().split()))
amount = int(input())
print(ways(coins, amount,0))
'''
# Bruteforce approach
'''
def ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]
coins =list(map(int,input().split()))
amount = int(input())

print(ways(coins, amount))
'''
#Coin change Problem -Statement
#Given a list of coin denominations and a total amount,find thr minimum number of coins needed
#to make that amount,return -1.
#coins=[1,2,5]
#Amount =11  O/P=3 -->11=5+5+1
'''
def coinChange(coins,amount):
    if amount==0:
        return 0
    if amount<0:
        return float('inf')
    res=float('inf')
    for i in coins:
        subres=coinChange(coins,amount-i)
        if subres!=float('inf'):
            res=min(res,1+subres)
    return res if res!=float('inf') else -1

coins =list(map(int,input().split()))
amount = int(input())
print(coinChange(coins, amount))
'''
'''
def coinChange(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for j in coins:
            if i-j>=0:
                dp[i]=min(dp[i],1+dp[i-j])
    return dp[amount] if dp[amount]!=float('inf') else -1
coins=list(map(int,input().split()))
amount=int(input())
print(coinChange(coins,amount))
'''
#0/1Knapsack problem
'Given weights and values of n items,and a maximum weight capacity W of a knapsasck,find the maximum total value'
'you can put into the knapsack'
'Each item can be picked at most once(hence the name"0/1")'
'''
def knapsack(val,wt,W,n):
    if W==0 or n==0:
        return 0
    if wt[n-1]>W:
        return knapsack(val,wt,W,n-1)
    else:
        return max(val[n-1]+knapsack(val,wt,W-wt[n-1],n-1),knapsack(val,wt,W,n-1))
values=list(map(int,input().split()))
weights=list(map(int,input().split()))
W=int(input())
n=len(weights)
print(knapsack(values,weights,W,n))
'''
#Backtrack
'''
def changeArray(a,ind,val):
    if ind==len(a):
        return
    a[ind]=val
    changeArray(a,ind+1,val+1)
    a[ind]=val-2
a=[i for i in range(5)]
print(a)
changeArray(a,0,1)
print(a)
'''
#Find subsets of a string
'''
"a"--->"",a-->2^1--->2
"ab"---->"",a,b,,ab--->2^2--->4
"abc"--->"",a,b,c,ab,ac,bc,abc--->2^3--->8'''
#BaseException
'''
def subsets(s):
    result = []
    def solve(index, current):
        if index == len(s):
            result.append(current)
            return
        solve(index + 1, current + s[index])
        solve(index + 1, current)
    solve(0, "")
    return result
s = input()
ans = subsets(s)
for i in ans:
    print(i)
    '''
#normal
'''
def subsets(s):
    res=[]
    for i in s:
        n=[]
        for r in res:
            n.append(r+i)
        res.extend(n)
    return res
s=input()
print(subsets(s))
'''
#Find permutations of a string
'''
abc-->abc,acb,bac,bca,cab,cba--->6
3!=6
'''
'''
s = "abc"
for i in range(len(s)):
    for j in range(len(s)):
        for k in range(len(s)):
            if i != j and j != k and i != k:
                print(s[i] + s[j] + s[k])
#pred defined fun
from itertools import permutations
s=input()
p=permutations(s)
for i in p:
    print("".join(i))
'''