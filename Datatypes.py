x = 10
print(type(x), x)

y = 0.5
print(type(y), y)

z = "Hanibal"
print(type(z), z)

# Number type conversions

x1 = 3.14
print(type(x1) , x1)
print(type(int(x1)), int(x1))

y1 = 'B'
c = ord(y1)
print(c)

tup1 = "Raphael"
x2 = tuple(tup1)
print(type(x2), x2)

tup2 = "Hanibal"
x3 = list(tup2)
print(type(x3), x3)

tup3 = "Hanibal"
x4 = set(tup3)
print(type(x4), x4)