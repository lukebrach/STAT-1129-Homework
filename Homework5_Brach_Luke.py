#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question 1
class Human:
    ishomosapien=True
    hasbody=True
    needsfood=True
    likesbacon=True
    def __init__(self,name,age,gender,height):
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
    def introduce(self):
        print("Hi, my name is ", self.name, " I am a ", self.age, " year old ", self.gender, " and I am ", self.height, " feet tall")
        
A=Human('Joe',30,'male','5.8')
B=Human('Sue',23,'female','5.5')

A.introduce()
B.introduce()


# In[14]:


#Question 2
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance(self):
        return (self.x ** 2 + self.y ** 2)**0.5
    
A=Point(3,4)
A.distance()


# In[ ]:


#Question 3
#A.) Class B inherits A, but the data field "i" is not inherited


# In[18]:


#Question 4
def main():
    print("hello", end="")
try:
    if __name__=="__main__":
        main()
except:
    print("name")
finally:
    print("world")
    
#Output is helloworld


# In[ ]:


#Question 5
#C.) 'self' is not needed in def namePrint(self)
#It is required, therefore the statement is incorrect


# In[19]:


#Question 6
x="hello"
if not type(x) is int:
    raise TypeError("Only Integers Are Allowed")
    
#Output is TypeError: Only Integers Are Allowed

