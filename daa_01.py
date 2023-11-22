def fiborecursive(n):
    if n<=1:
        return n
    else:
        return fiborecursive(n-1) + fiborecursive(n-2)
def fibononrecursive(n):
    a = 0
    print(a)
    b = 1
    print(b)
    for i in range(2,n):
        c = a+b
        print(c)
        a = b
        b = c

n = 10
print("recursive---------")
for i in range(n):
    print(fiborecursive(i))

print("non-recursive---------")
fibononrecursive(n) 