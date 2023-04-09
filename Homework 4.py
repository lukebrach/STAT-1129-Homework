#!/usr/bin/env python
# coding: utf-8

# In[43]:


#Question 1


# In[42]:


import numpy as np

array=np.arange(1,13).reshape((3,4))
print(array)
print( )
print(array*2)
print(array.ndim)
print(array.shape)


# In[ ]:


for row in array:
    for column in row:
        print(column,end = ' ')
    print()


# In[41]:


for i in array.flat:
    print(i,end=' ')


# In[ ]:


#Question 2


# In[47]:


import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6])
y=np.array([5,6,7,8,9,10])

plt.plot(x,y)


# In[53]:


x2=np.array([3,6,9,12])
y2=np.array([2,8,1,10])

plt.plot(x2,y2,marker='D')


# In[ ]:


#Question 3


# In[56]:


x3=np.array([0,1,2,3,4,5])
y3=np.array([2,4,6,14,10,12])

plt.plot(x3,y3,'--r',marker='D',markersize=10,markerfacecolor='g')


# In[ ]:


#Question 4


# In[57]:


x4=np.array([0,4])
y4a=np.array([1,5])
y4b=np.array([5,9])
y4c=np.array([9,13])

plt.plot(x4,y4a)
plt.plot(x4,y4b)
plt.plot(x4,y4c)

plt.show()


# In[ ]:


#Question 5


# In[64]:


marks={'Andy':88,'Amy':66,'James':90,'Jules':55,'Arthur':77}

for student in marks:
    print(student, "has a grade of ",marks[student])
    
names=marks.keys()
grades=marks.values()

plt.bar(names,grades)
plt.xlabel('Student')
plt.ylabel('Grade')
plt.title('Grades of Students')
plt.show()

plt.pie(grades,labels=names)
plt.title('Grades of Students')
plt.legend()

plt.show()


# In[ ]:


#Question 6


# In[70]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = [10, 20, 30, 40, 50]
labels = ['A', 'B', 'C', 'D', 'E']
y4 = [25, 30, 10, 20, 15]
y5 = np.random.randn(1000)

fig, axs = plt.subplots(nrows=2, ncols=3)

axs[0, 0].plot(x, y1, label='sin(x)')
axs[0, 0].plot(x, y2, label='cos(x)')
axs[0, 0].set_title('Multiple Lines')
axs[0, 0].legend()

axs[0, 1].bar(labels, y3)
axs[0, 1].set_title('Bar Chart')

axs[0, 2].pie(y3, labels=labels)
axs[0, 2].set_title('Pie Chart')

axs[1, 0].plot(x, y1, label='sin(x)')
axs[1, 0].plot(x, y2, label='cos(x)')
axs[1, 0].grid()
axs[1, 0].set_title('Grid')
axs[1, 0].legend()

axs[1, 1].scatter(labels, y4)
axs[1, 1].set_title('Scatter Plot')

axs[1, 2].hist(y5, bins=30)
axs[1, 2].set_title('Histogram')

fig.suptitle('Subplots Example')

plt.subplots_adjust(hspace=0.7, wspace=0.4)

plt.show()

