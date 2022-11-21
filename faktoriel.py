n = int(input("Въведете число: "))
f = n
print("Факториел на числото: ")
while n > 1:
    f *= (n-1)
    print(f"{n} x", end=" ")
    n -= 1
print("1 =", f)