my_dictionary = {
    'Name': 'Grace',
    'Gender': 'Female',
    'Status': 'Single'
}
print(my_dictionary)
my_dictionary = dict(
    Name= 'Grace',
    Gender= 'Female',
    Status= 'Single'
)
print(my_dictionary)
print(my_dictionary['Gender']) #prints a specific value in the dictionary
print(my_dictionary.get('Status')) #prints a specific word to the dictionary
print(my_dictionary['Name'])
my_dictionary['Status'] = 'Complicated' #edits the dictionary
print(my_dictionary)
my_dictionary['BirthDate'] = '2005' #adds a key value to the dictionary
print(my_dictionary)
my_dictionary['Location'] = 'Nairobi'
print(my_dictionary)
my_dictionary['Phone'] = '0123456789'
print(my_dictionary)
my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary))
my_dictionary.pop('Phone') #removes a dictionary word
print(my_dictionary)
# del my_dictionary2['Phone'] #works as the pop
# my_dictionary.clear() #clears the whole content in the dictionary
# print(my_dictionary)
# del my_dictionary
# print(my_dictionary)
if 'Name' in my_dictionary:
    print('Name is in dictionary')
else:
    print('Name is not in dictionary')

for value in my_dictionary:
    print(my_dictionary[value]) #prints dictionary values
for key in my_dictionary:
    print(key)

for key, value in my_dictionary.items(): #prints the key and values
    print(key, value)


my_dict = {
    'Milk': 80,
    'Bread': 100,
    'Coffee': 200,
}
print(my_dict)
if 'Milk' in my_dict:
    print('milk available')
else:
    print('Not available')
my_dict['Soap'] = 40
print(my_dict)