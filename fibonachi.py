length = int(input("Въведете бой числа на Фибоначи: "))
a, b = 0, 1
fib = [a, b]
for i in range(length):
    a, b = b, b+a
    fib.append(b)
print(fib)