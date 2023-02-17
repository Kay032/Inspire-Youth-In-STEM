age = 16

gender = "male"

if (age < 18 ):
    print("You are still young ")
else:
    print("Get an id")
        
#compound / multiple condition
if((age > 30 ) & (gender == "male")):
    print("You might qualify for a loan")
else:
    print("No loan")


fav_color = "grey"
age = 22
if(fav_color == "grey") | (age <= 20):
    print("Happy birthday to you")
else:
    print("No birthday for you")  
