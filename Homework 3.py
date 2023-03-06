#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Question 1 Part 1
marks = {"Andy":88, "Amy":66, "James":90, "Jules":55, "Arthur":77}


# In[25]:


def gradefinder(studentname):
    cantfind=0
    for name,grade in marks.items():
        if studentname==name:
            return marks[studentname]
        else:
            cantfind=1
    if cantfind==1:
        print(studentname + " Cannot Be Found")
        


# In[ ]:





# In[ ]:





# In[37]:


#Question 1 Part 2
def averager(dictionary):
    summation=0
    for grade in dictionary.values():
        summation+=grade
    average=summation/len(dictionary.values())
    return average
    


# In[38]:


averager(marks)


# In[ ]:





# In[42]:


#Question 2
def square(num):
    n=0
    while n<num:
        print(n,n**2)
        n+=1
    else:
        print("greater than ",num)
        


# In[44]:


square(8)


# In[ ]:





# In[46]:


#Question 3
def summation(num):
    n=0
    total=0
    while n<=num:
        total+=n
        n+=1
    print(total)


# In[49]:


summation(4)


# In[ ]:





# In[51]:


#Question 4
def summation2(num):
    n=0
    total=0
    while n<=num:
        total+=n
        n+=1
        print(total)


# In[52]:


summation2(4)


# In[ ]:





# In[96]:


#Question 5
def diagnostics(list):
    std=0
    numerator=0
    for i in list:
        mean2=sum(list)/len(list)
        sum2=sum(list)
        numerator+=(i-mean2)**2
    std=(numerator/len(list))**(1/2)
    print(mean2," ",sum2," ",std," ")


# In[98]:


diagnostics(range(1,100))


# In[ ]:





# In[102]:


#Question 6
def minimal(v1,v2,v3,v4):
    minval=v1
    if v2<minval:
        minval=v2
    if v3<minval:
        minval=v3
    if v4<minval:
        minval=v4
    return minval


# In[105]:


minimal(5,2,9,3)


# In[ ]:





# In[160]:


#Question 7
def concatenator(*args):
    output=[]
    for i in args:
            if type(i)==list:
                for e in i:
                    output.append(e)
            else:
                output+i
    return output


# In[163]:


#proof
happy=["fortnite","amogus","ha"]
sad=["bk, have it your way","no","France"]
meh=[1]
mega=happy+sad+meh

concatenator(mega)


# In[ ]:





# In[154]:




