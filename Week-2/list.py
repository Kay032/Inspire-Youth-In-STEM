name=['john','Hum','Ian','Rick','Sabi']

#Accessing items on a list

print(name)

print(name[0])
print(name[-1])
print(name[-3])
print(name[0-3])

fruits=['pineapples','oranges','lemons','passions','guava','kiwi','apples']
print(fruits[0:-1])
print(fruits[3])
print(f"My favourite fruit is:",fruits[2].upper())

#Adding two lists 
vegetables =["kales","spinsch","cabbage","managu","carrots","brocoli"]
stationary =["pens","ink","paper","glue","scissors","stapler"]
shopping = vegetables + stationary
print(shopping)
print(shopping[6])


for vegetable in vegetables:
    print(vegetable)
for shopping in shopping:
    print(shopping)

print("My name is ", + name[4]+ "and my favourite fruit is " +fruits[3])