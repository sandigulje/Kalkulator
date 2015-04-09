a = raw_input("Povej prvo stevilo ")
print(a)
b = raw_input("Povej drugo stevilo ")
print(b)
operacija = raw_input("Izberi operacijo: +, -, /, *")
print(operacija)

a = float(a)
b = float (b)

if operacija == "+":
    print(a + b)
elif operacija == "-":
    print(a - b)
elif operacija == "/":
    print(a / b)
elif operacija == "*":
    print(a * b)
else:
    print("Neznana operacija")