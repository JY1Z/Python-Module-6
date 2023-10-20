import random
#1
def roll():
    dice = random.randint(1,6)
    return dice

a= roll()
while a != 6:
    print(a)
    a = roll()
else:
    print(a)


#2
def roll(num):
    dice = random.randint(1,num)
    return dice

num = int(input("Enter a int num:"))
a = roll(num)
i = 0
while a != num:
    i = i +1
    print(a)
    a = roll(num)
else:
    print(a)
    print("times:",i+1)


#3
def gallontoliters(gallons):
    litres = 0.2641720524 * gallons
    return litres
gal = float(input("Enter gallons:"))
while gal >= 0:
    lit = gallontoliters(gal)
    print("liters:",lit)
    gal = float(input("Enter gallons:"))
else:
    print("end")


#4
def list(items):
    sumall = 0
    for item in items:
        sumall = sumall + item
    return sumall
items = [1,2,3,4,5]
print(list(items))


#5
def list(ints):
    #uneven = 2
    print(ints)
    for int in ints:
        if int % 2 != 0:
            ints.remove(int)
    print(ints)
    return
list([2,11,4,6,9,10,9,14,15,16])


#6
import math
def price(diameter, money):
    r = diameter/200
    s = r**2 * math.pi
    cal = money / s
    return cal

d1 = float(input("diameter："))
m1 = float(input("money"))
d2 = float(input("2d"))
m2 = float(input("2m"))

if price(d1,m1) > price(d2,m2):
    print("2 is lower")
if price(d1,m1) < price(d2,m2):
    print("1 is lower")
if price(d1,m1) == price(d2,m2):
    print("1=2")

