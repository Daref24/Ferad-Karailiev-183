def list_avg(lst,multiplier=1):
    sum = 0
    n = 0
    if type(multiplier) != int:
        return
    for i in range(len(lst)):
        if type(lst[i]) == int or type(lst[i]) == float:
            lst[i] *= multiplier
    for i in lst:
        if type(i) == int or type(i) == float:
            sum += i
            n += 1
    if n == 0:
        return 
    avg = sum/n
    print("Списък:", lst)
    print("Средно аритметично:", avg)


list_avg([1,2,3,4,"a","lalala",9.2])
list_avg([1,2,3,4,"a","amongus",9.2],2)
list_avg([1,2,3,4,"a","haha",9.2],2.3)
list_avg([3.3,2,"a","deded"],"asd")