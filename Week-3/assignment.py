
#Write a program to calculate simple interest 

def simple_interest(principal, rate, time):

    return (principal * rate * time) / 100

p = 100000.0
r = 8.5
t = 3.0
interest = simple_interest(p, r, t)
print("Simple interest is:", interest)

