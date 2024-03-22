my_list = [113,123,456,789,659,284]
print(my_list)
print(my_list[5])
print(my_list[1:5])
my_list[1] = 345
print(my_list)
my_list[4] = 455
print(my_list)
# len(my_list)
print(len(my_list))
my_list.append(389) #adds values at the end
print(my_list)
my_list.insert(1,240) #positions the index at a certain point
print(my_list)
my_list.extend([265,678,575]) #continues to add values at the end
print(my_list)
my_list.remove(265) #removes a certain value
print(my_list)
del my_list[3] #deletes a certain index
print(my_list)
my_list.clear() #deletes the data
print(my_list)
# del my_list
# print(my_list)

my_list2 = [124,485,376,482,510,634,755,866,956]
print(max(my_list2)) #shows the max value
print(min(my_list2)) #shows the min value
print(sum(my_list2)) #adds the value
print(sum(my_list2)/len(my_list2)) #shows the average
print(my_list2)
if 482 in my_list2:
    print('Yes it is in my list')
else:
    print('Not in my list')


my_list3 = ['Mercy', 'Jannice', 'Roy', 'David', 'Jennifer']
print(my_list3)
if 'Roy' in my_list3:
    print('Present')
else:
    print('Not present')