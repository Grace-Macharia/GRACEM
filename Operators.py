# arithmetic_operators
# +,-,*,/,%,**
a = 5
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
# assignment operators
c = 10
# c = c + 5
c+=5
print(c)

d = 7
d = d - 4
# d-=4
print(d)

c = 8
c*=2
print(c)

b = 30
b/=5
print(b)
#comparison operators
# ==,!=,<=,>=,<,>
a = 10
b = 20
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
# logical operators
# and,or,not
d = 10
f = 6
(d>f) and (d<f)
print((d>f) and (d<f))
print((d<f) and (d>f))
print((d>f) and (d==f))
print((d<f) and (d==f))
print((d>f) and (d<=f))
print((d>f) or (d<f))
print((d<f) or (d>f))
print((d>f) or (d==f))
print((d<f) or (d==f))
print(not((d>f) and (d<f)))
print(not((d>f) or (d<f)))
# identity operators //is, is not
x = 6
y = 3
print(x is y)
print(x is not y)
print(type(x) is type(y))
# membership operator
a = 'Welcome to Full Stack Development'
print('tack' in a)
print('Full' not in a)


number_of_cows = input('How many cows? ')
number_of_dogs = input('How many dogs? ')
print(number_of_cows>number_of_dogs)