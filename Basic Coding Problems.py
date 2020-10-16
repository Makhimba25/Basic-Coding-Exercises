#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Basic Coding Problems


# In[26]:


#Swap 2 variables

x=5
y=10

#method 1: using conditional statement
if x!=y:
    y=x
print(y)


#method 2: using tuples 
x,y=y,x
print("x=",x)
print("y=",y)

#Method 3: using a temporary variable
m=x
x=y
y=m
print(m)


# In[ ]:


#Convert celsius to fahrenheit

celsius=(fahrenheit-33)*5/9
fahrenheit=(celsius*9/5)+32
print(fahrenheit)
print(celsius)


# 
# 

# In[ ]:


#reverse a string

#Method 1
string="Makhimba"[::-1]
print(string)

#Method 2: using a function

def reverse(x):
    return x[::-1]
string=reverse("Makhimba")
print(string)


# In[8]:


#Fibonnacci sequence using while loop

a,b=0,1

while b<130:
    print(b)
    a,b=b,a+b


# In[11]:


#count characters in a string

sentence= "Makhimba is funny"
print(len(sentence))

#count words in a string
print(len(sentence.split()))


# In[ ]:


#odd or even
#ask user for number
#if number has no remainder when divided by 2, it is even
#if remainder=0


x=int(input("Please enter a number"))
if x%2==0:
    print("Number is even")
else:
    print("Number is odd")


# In[ ]:


#write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in a:
    if num < 5:
        print(num)


# In[131]:


#Instead of printing the elements one by one, make 
#a new list that has all the elements less than 
#5 from this list in it and print out this new list.
# list comprehension ([output for item in list if filter])
print([aa for aa in a if aa<5])


# In[ ]:


#user guess top card in deck
cards=[1,2,3,4,5,6,7,8,9,10]
guess = cards[0]
user_guess= int(input("Guess top card"))

while user_guess != guess:
    user_guess= int(input("Guess top card"))
    if user_guess==guess:
        print("Congrats")
    else:
        user_guess= int(input("Guess top card"))
        


# In[ ]:




