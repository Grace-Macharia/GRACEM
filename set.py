my_set = {1,2,3,4,5}
print(my_set)
var1 = 2
if var1 in my_set:
    print(var1)
    var2 =5
if var2 in my_set:
    print(var2)
my_set.add(9)
print(my_set)
my_set.update([5,7,9,4])
print(my_set)
my_set2 = my_set.copy()
print(my_set2)
print(my_set)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))
my_set.discard(7)
my_set.clear()
del my_set
if 32 in my_set2:
    print(32 in my_set2)
else:
    print("32 not in my_set2")