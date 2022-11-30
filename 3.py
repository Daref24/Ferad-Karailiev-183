def input_nums(n):
    vallist = []
    if type(n) != int:
        return vallist
    for i in range(n):
        f = input("Въведете стойност: ")
        if f.isnumeric() == True:
            vallist.append(f)
    return vallist
print(input_nums(5))
print(input_nums('a'))

def sum_list(lst):
    sum = 0
    for i in lst:
        if type(i) == float:
            sum += i
        elif str(i).isnumeric() == True or type(i) == int:
            i = int(i)
            sum += i
    return sum

print(sum_list(["a","s","f"]))
print(sum_list(["3",5,7.6,12,'22']))


def max_of_two(a,b):
    x = type(a)
    y = type(b)
    if (x == int or x == float) and (y == float or y == int):
        if a > b:
            return print(a)
        if a < b:
            return print(b)
        if a == b:
            return print(a)
    elif (x == int or x == float) and (y != float or y != int):
        return print(a)
    elif (x != int or x != float) and (y == float or y == int):
        return print(b)
    else:
        return

max_of_two("a","b")
max_of_two(5,10)
max_of_two(20,15)
max_of_two(3,"b")
max_of_two("asd",22)

max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3)))