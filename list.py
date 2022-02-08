# -*- coding: utf-8 -*-
"""


@author: sara
"""

#List 
print([5,2,7])
print([5,2,[7,6],4]) #List in List
print([]) #empty List 


#ex1 error string
fruit='Banana'
fruit[0]='b'
#error
#we should do ...
fruit='Banana'
x=fruit.lower()
print(x)

# but it is possible for list
list=[1,2,3,4]
list[2]=35
print(list)


#range
print(range(4)) #[1,2,3]
v=['a','b','c']
print(len(v)) #3
print(range(len(v))) #[1,2]


#ex 
a=['1','2','78','6','98','45']
print(a[1:3]) #['2','78']
print(a[2:]) #['78', '6', '98', '45']
print(a[:3]) #['1', '2', '78']
print(a[:]) #['1', '2', '78', '6', '98', '45']



#append add to list
w=list()
w.append('sara')
print(w)



#is there sth in the list
b=[1,2,3,4]
1 in b #true
5 in b #false
2 not in b #false


#ex build in func
b=[1,2,3,4]
print(max(b))
print(min(b))
print(len(b))
print(sum(b))
print(sum(b)/len(b)) #avg




#string to list
a='Hello Dear Sara'
b=a.split()
print(b)  #['Hello', 'Dear', 'Sara']



#ex2 with space
a='Hello Dear              Sara'
b=a.split()
print(b)  #['Hello', 'Dear', 'Sara']



#ex3 with ;
a='Hello;Dear;Sara'
b=a.split()
print(b)  #['Hello;Dear;Sara']
print(len(b)) #1


#ex4 
a='Hello;Dear;Sara'
b=a.split(';')
print(b) #['Hello', 'Dear', 'Sara']
print(len(b)) #3



#ex5
a=open(r'C:\Users\sara\Desktop\office 2021\sara2.txt')
for i in a:
    i=i.rstrip()
    if not i.startswith('From'):
        continue
    words=i.split()
    print(words[2]) #Sat Fri Mon




# double split
a=open(r'C:\Users\sara\Desktop\office 2021\sara2.txt')
for i in a:
    i=i.rstrip()
    if not i.startswith('From'):
        continue
    words=i.split()
    b=words[1]
    print(b) #sara@yahoo   Alex@yahoo   Med@yahoo
    c=b.split('@')
    print(c[0]) #sara Alex Med




#