"""
a = 20
b=5
a,b = b, a

print (a)

def add(base, *args):
    total = base
    for num in args:
        total += num   
    print (total)

add (5,20)

"""
def multiply (base,*args):
    total = base
    previous = ()
    for num in args:
        previous = num
        total += num
    print(total)
multiply (5,5,7)