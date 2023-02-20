#!/usr/bin/env python3
#This is a single line comment
#Name : Bonface Kerosi
# Email : kerosionc@gmail.com
# 20th Feb,2023
# File : assignment-1.py



#create an empty list
#using for loop add 5 musicians 
#copy your new list called "celebs"
#sort the list 
#pop out 2 celebs
#count the number of remaining 

musicians = []
n =int(input("enter number of names required"))
for i in range (0,n):
    elem =str (input("Enter musician names :"))
    musicians.append(elem)
print("the created list of names:",musicians) 
celebs = musicians.copy()
print(celebs)
celebs.sort()
print(celebs)
celebs.pop(2)
print(celebs)
print(len(celebs))
