num = int(input("Въведете брой на числата: "))
numlist = []
for i in range(num):
    numlist.append(int(input("Въведете число: ")))
print("Списък:",numlist)
f = int(input("Въведете 0 или 1: "))
if f == 0:
    for i in range(0,len(numlist),2):
        numlist[i] += 5
elif f == 1:
    for i in range(1,len(numlist),2):
        numlist[i] += 10
else:
    print("Невалидно число!")
print("Списък след преобразуване:",numlist)