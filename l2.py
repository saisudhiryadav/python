def append_to_list(value,lst = []):
    lst.append(value)
    return lst
print(append_to_list(1)) # [1]
print(append_to_list(2)) # [1, 2]
print(append_to_list(3)) # [1, 2, 3]

def func(a,b,c):
    return a+b+c

l = [10,20,30]
print(func(10,20,30)) # 60
print(func(*l)) # 60 unpacking

l1 = [lambda x: x + i for i in range(5)]
print(l1[0](5)) # 9

def factorial(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n)
        return n * factorial(n-1)
r = factorial(5)
print(r)    # 120 

def factorial(n):
    return 1 if n == 0 else n* factorial(n-1)
r1 = factorial(5)
print(r1) # 120


def func():
    return 1,2,3
a,b,c = func()
print(a,b,c)     # 1 2 3


