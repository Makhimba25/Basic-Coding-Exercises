#!/usr/bin/env python
# coding: utf-8

#Basic Coding Problems

#Swap 2 variables
x=5
y=10
#Method 1: using conditional statement
if x!=y:
    y=x
print(y)
#Method 2: using tuples 
x,y=y,x
print("x=",x)
print("y=",y)
#Method 3: using a temporary variable
m=x
x=y
y=m
print(m)


#Convert celsius to fahrenheit and vice versa
celsius=(fahrenheit-33)*5/9
fahrenheit=(celsius*9/5)+32
print(fahrenheit)
print(celsius)


#Reverse a string
#Method 1
string="Makhimba"[::-1]
print(string)
#Method 2: using a function
def reverse(x):
    return x[::-1]
string=reverse("Makhimba")
print(string)


#Fibonnacci sequence using while loop
a,b=0,1
while b<130:
    print(b)
    a,b=b,a+b

    
#Count characters in a string
sentence= "Makhimba is funny"
print(len(sentence))


#count words in a string
print(len(sentence.split()))

#Odd or Even
x=int(input("Please enter a number"))
if x%2==0:
    print("Number is even")
else:
    print("Number is odd")


#Write a program that prints out all the elements of a list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
    if num < 5:
        print(num)
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
print([aa for aa in a if aa<5])


#User guess top card in deck
cards=[1,2,3,4,5,6,7,8,9,10]
guess = cards[0]
user_guess= int(input("Guess top card"))

while user_guess != guess:
    user_guess= int(input("Guess top card"))
    if user_guess==guess:
        print("Congrats")
    else:
        user_guess= int(input("Guess top card"))
