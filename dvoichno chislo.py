num = int(input("Въведете число: "))
n = int(input("Индекс от двоичното число: "))
bi = []
while num > 0:
    f = num % 2
    num = num // 2
    bi.append(f)
bi.reverse()
print("Двоичният вид на числото е: ", bi)
if bi[n] == 0:
    print("Двоичното число има нула на индекс", n)
else:
    print("Двоичното число има единица на индекс", n)