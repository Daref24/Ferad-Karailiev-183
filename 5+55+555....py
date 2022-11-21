n = int(input("Въведете число: "))
m = 0
for i in range(1,n+1):
    f = str(n)*i
    if i < n:
        print(f"{f} +",end = " ")
    else:
        print(f,end=" ")
    m += int(f)
print("=", m)