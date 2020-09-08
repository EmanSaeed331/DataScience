# -*- coding: utf-8 -*-
# part1 of python Crash course .
"""
Spyder Editor

This is a temporary script file.
@author: eman-saeed

"""
num = 12 
name = 'Eman'
print('My number is {num} and my name is {name}'.format(num=num,name=name))

s = 'hello'
#S is a sequance of charachter 
print(s[0])
B = 'EMANSAEEDMAHMOUDMOHAMED'
print(B[-5])

E = 'abcdEfghi'
#colon notation which is known as slice syntax 
print(B[0:])
#grap everything up to 3

print (E[0:3])
print(E[:3])
print(E[3:6])
"""First_List : is an example for lists,
   we can define list as : a sequance of elements in
   a square set of square brackets separeted by commas ","
   and it store any type of data .

 """

First_List  = [1,2,3,4]

First_List.append(4)
print(First_List)
First_List.append(0)

print(First_List)

First_List[0] = 00
First_List[1] = 145
print(First_List)
lis1 = [1,2,3,4,5,6,6,7,7]
lis1[3]="hello"
print(lis1)
# we can use the content of list inside of list 
# List elements can with a diffrent type , but we can merge a diffrent types of lists.
#nest_list = First_List 
nest_list =[1,24,64,22,First_List]
print(nest_list)
nest_2= [1,2,3,4,["Woow ","Hello"],[1.2,1.2,3.3]]
print(nest_2)
#--------------------------------------------------
# part2 of python Crash course .
"""we can use dictionary in python,
   we can creat dictionary with creating
   a curly brackets then you will have a
   key , colon , value ->  {'key1':'value'},
   value will be corrseponds with that key.
"""
"""dictionary behaves as key value pairs just like 
   hash table instead of holding elements in a sequance.
   
"""
"""
#REMEMBER : Hash table is a data structure that use a hash function 
            to map a particular value with a key.
"""

dic1 = {'key1':'value','key2':'value2'}
print(dic1['key1']+"  "+dic1['key2'])
dict2 = {'Name':'Eman-Saeed','Age':23,'Faculty':'engineering'}

"""
we can merge dictionary with lists , 
lists can be a value of a specific key.
"""
d = {'k1':[2,3,4,6]}
print(d['k1'][1])
test_list =[1,2,4,56,[12,2,45,67],[1,3,5,7]]
test_list1=[1,2,3,4,5,6]
test_list2 = [4,5,6,7,8,32,43]
test_list3 = [1,4,5,6,7,7,8]
test_dict = {'key1':test_list1,'key2':test_list2,'key3':test_list3}
print(test_dict)
print(test_dict['key1'])
print(test_dict['key2'])

"""
we can use an inner key in a general key -> 
the inner key represents a value for the general key.
we cannot  use multiple inner key .
"""
inner_key_dict = {'key1':{'innerkey':[12,42,20]}}
print(inner_key_dict['key1']['innerkey'])

"""
tuples and sets
#REMEMBER : list is a sequance of elements inside a square brackets separated by comma.
            list is using indexing -> it is mean that you write the index to have the value.
            list is a mutable (قابل للتغير)
tuple is very similar to list expect you use paentheses and you can grab items. 
"""
tuple1 = (1,2,3,4,5,5,6,7,7,8)
print(tuple1)
print(tuple1[0:4])
print(tuple1[:])
"""
in tuple we can't assign a new elemnt with a diffrent type
becouse tuples are immutable (غير قابل للتغير)and they do not support item assignment.
"""
#tuple1[1] = "help " #--.error 
print(tuple1)

"""
Sets in python 
Sets is a collectoion of a unique elements and 
it looks the same of curly brackets as dictionary except 
it doesnot have colons  and it just elements.
set is defined by onlu unique elements .
"""
 
set1 = {1,2,3,4,56,98,23}
print(set1)
"""
we can use SET ,
SET is a function and  we use a list with set function to grap the unique elements .
SET function does not repeat any value of the listed values .
"""
print(set([1,2,3,4,5,6,7,0,1,3,5,5]))

test_set = {1,2,3,4,5,4,6,7,1}
test_set.add(0)
print(test_set)

#if conditions

list_1 = [8,0,1,4,6,20,59,20]
list_2 = [0,1,4,2,8,1,9.2,12]
 
if list_2 > list_1:
   list_1.insert(3,20000)
   print(list_1)
else:
    list_2.extend(list_1)
    print(list_2)
#-----------------------------------------------------
# part3 of python Crash course .
seq  = [1,2,3,4,5,6,7,8,9]
for item in seq:
    print(item)
    
    
seq1 =['a','e','c','k']
for item in seq1:
    print(seq1)

#i = 1
#while i<50:
 #   print(i) #infinit loop 
    
example = 2 
while example<30:
    print('my age is {}'.format(example))
    example+=1


for x in seq: 
    print(x)

#RANGE FUNCTION 
    """
    Range is a function and it is going to be generator of numberical value,
    Range(the number you start with , the number you end with )
    range (0,19) -> is a range object.
    we can convert the rang function into a list.
    
    """

range(0,1000)


for x in range(0,1000):
    print(x)

list(range(0,1000))
list(range(10))


#List comprehension
"""
    list comprehension allows you to save a bunch of writing ,
    when you trying to creat a for loop to create a for loop to create a list.
     
    """
    
x = [1,2,3,4,5,6,0]
out=[]
for item in x:
    out.append(num**2)
print(out)

[num**2 for num in x]   
out = [num**2 for num in x ]


#Funcions
"""
functions allow you basically not to have to continually 
write code over again you can just write it inside og a function and then call that function..
the keyword of function is DEF -> def 
""" 
def func1(param1):
    print('hello  '+param1)

func1( "Eman")
    
def square(num):
    return(num**2)

result = square(20)
print(result)

#------------------------------------------------------------------
# part4 of python Crash course .
"""
we will learn lambda expressions , the map and filter functions as well as just
as well jsut various methods you can use on diffrent data type in python.
 (map) and filter functions
"""
def times2(var):
    return var*2

t = times2(500)
print(t)
#map function .

"""
if we want to apply the function-> times2 to a single element in list
and the output is a list.
map is a built-in function , map will applied the given function to each single element in the list.

"""

seq = [1,2,3,4,5,6,7,9,10]

print(list(map(times2,seq)))




"""
lambda expressions.
we can write a function  in one line .
we can rewrite def times3(var): 
                    return(var**3)
    -> lambda var:var**2
"""

t = lambda var:var**3
print(t(3))
 

print(list(map(lambda num:num*3,seq)))
"""
the filter function 
filter function is a built-in function , it has a very similar structure to map 
but instead of mapping a function to every element in a sequance we will filter out elements out of the sequance.

the below function return the even numbers in a sequance .
it use some sort conditional operation , it return a boolean value(true or false)
"""
print(list(filter(lambda num: num%2 == 0 , seq)))

#Methods 
"""
methods are essentially just cause you can make off an object that will affect the object or return a result in some manner 
"""
s = 'Hello my name EMAN '
print(s.lower())
print(s.upper())
print(s.split())

dic = {'K1':1,'K2':2,'K3':3}
print(d.keys())


print(dic.values())
print(dic.items())
lst = [1,2,3,4,5,6]
item = lst.pop()
lst.append('item')
print(lst)

print('x' in['x','1','2','4','5'])
print('R' in [1,2,3,4,5,6,7,8])


"""
tuple unpacking
 
"""

x = [(1,2),(3,4),(5,6),[(2,3),(1,4),(1,6)],[(1,4),(6,1),(0,1)]]
print(x[0][1])

for item in x:
    print(item)

unpack = [(1,2),(3,4),(5,6)]

for (a,b) in x:
    print(a)

