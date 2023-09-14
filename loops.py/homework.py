a = input("Enter a number: ")
a = int(a)
b = input("Enter b number: ")
b = float(b)
c = a + b

if a == b:
    print("equal")
else:
    print("Different")

print("El tipo de dato de a: ", type(a))
print("El tipo de dato de b: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a y b son de igual tipo")
else:
    print("a y b son de diferente tipo")
