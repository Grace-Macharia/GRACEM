my_tuple = (123, 256, 378, 444, 557)
print(my_tuple)
print(my_tuple[4])
print(my_tuple[2:4])
print(len(my_tuple))
del my_tuple
my_tuple2 = (123, 256, 378, 444, 378, 789, 567)
print(my_tuple2)
my_tuple2.count(378)
print(my_tuple2.count(378))
print(max(my_tuple2))
print(min(my_tuple2))
print(sum(my_tuple2))
print(sum(my_tuple2)/len(my_tuple2))
print(my_tuple2.index(378))
if 378 in my_tuple2:
    print('378 is present in my_tuple2')
else:
    print('378 is not present in my_tuple2')
