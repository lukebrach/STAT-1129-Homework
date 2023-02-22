#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n=0
while n<10:
    print(n)
    n+=1
    if n==5:
        break


# In[ ]:





# In[ ]:


n=0
while n<5:
    print(n)
    n+=1
else:
    print(str(n) +" is not less than 5")


# In[ ]:





# In[ ]:


n=0
fruits=["mango","orange","fortnite","apple","banana"]
for fruit in fruits:
    while n<4:
        if fruits[n]!="apple":
            print("I like " + fruits[n])
            n+=1
            if fruits[n]=="apple":
                print("I do not like "+fruits[n])
                break


# In[ ]:





# In[2]:


n=0
answer=0
while n<31:
    answer+=n
    n+=1
print("The Answer is "+str(answer))


# In[ ]:





# In[3]:


def grader(grade):
    if grade>=90:
        print("A")
    elif grade>=80:
        print("B")
    elif grade>=70:
        print("C")
    elif grade>=60:
        print("D")
    else:
        print("F")


# In[4]:


#proofs
grader(53)
grader(65)
grader(76)
grader(81)
grader(90)


# In[ ]:





# In[2]:


marks={'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}


# In[3]:


for student in marks:
    print(student, "has a grade of ",marks[student])


# In[13]:


grades=list(marks.values())
Mean=sum(grades)/len(grades)   #calculates and sets variable equal to the mean
print("The mean is",Mean)                    #prints mean equated variable
print("The max is", max(grades))             #calculates and prints the max
print("The min is",min(grades))             #calculates and prints the min


# In[16]:


for student in marks:
    if 'J' in student:
        break
    print(student)


# In[17]:


for student in marks:
    if 'J' in student:
        continue
    print(student)

