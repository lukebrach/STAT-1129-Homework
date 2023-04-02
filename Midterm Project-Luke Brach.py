#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Part 1 Midterm
#Luke Brach


# In[7]:


#In this step I import all necessary libraries and convert the file from a txt file to a readable list in Python

import re
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np


numdata=open("C:/STAT 1129/numbers.txt","r")
numstring=numdata.read()
numlist=re.split(r',|\n',numstring)
print(numlist)


# In[6]:


#In this step, I convert the newly created list into a dictionary to count frequency

d = {}
for item in numlist:
    if item not in d.keys():
        d[item]=1
    else:
        d[item]+=1
d


# In[ ]:


#In this step, I upload the file to its designated folder as a json file. Since this folder and pathway wouldn't work on any other computer, it will come as an error on other devices, but uploads properly on mine


path = r"C:/Users/lbrac/OneDrive/Desktop/STAT 1129/output.json"
with open(path,"w") as out:
    json.dump(d,out)
f=open("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/output.json","r")
f


# In[ ]:


#Question 2 Midterm
#Luke Brach


# In[9]:


#Using data from Premier League Fixtures up until 3/31/23, I downloaded a csv file of various match statistics
#The first step, as is done here, is to read the csv file and store it as a dataframe using pandas

df= pd.read_csv("C:/Users/lbrac/OneDrive/Desktop/STAT 1129/Premier League Statistics - 2022-23 Matchweek 28 Stats.csv")
df


# In[10]:


#In this step I Create a Pie Chart of the Premier League Based off of goals scored by each team. The larger the slice, the higher the total goals scored
#Optional: to mark colors=prem_colors but it looks pretty ugly

my_explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,]
plt.pie(df['G'], labels=df['Team Name'],explode=my_explode)
#prem_colors=['red','cyan','red','white','black','red','blue','red','black','blue','purple','blue','yellow','cyan','blue','red','blue','brown','red','pink']
plt.show()


# In[11]:


#In this step, a bar graph is made showing every team's Goals minus Expected Goals

df.plot(kind= 'bar', x= 'Team Name', y='G-xG')


# In[12]:


#In this step, a similar bar graph is made depicting every team's Points Tally minus their expected Points Tally

df.plot(kind= 'bar', x= 'Team Name', y='PTS-xPTS')


# In[13]:


#In this step, multiple lines depict every team's Goals Scored (Orange), Goals Against/Conceded (Green), and Goal Difference (Blue)

x1 = df['League Position']
y1=df['GD']
x2=df['League Position']
y2=df['G']
x3=df['League Position']
y3=df['GA']

font1={'family':'serif','color':'blue','size':20}
font2= {'family':'serif','color':'darkred','size':15}

plt.plot(x1,y1,x2,y2,x3,y3)
plt.xlabel("League Position", fontdict = font2)
plt.ylabel("Goals", fontdict = font2)
plt.title("xG,G & GA vs League Position", fontdict = font1)


# In[16]:


#In this step, multiple lines depict every team's Points Tally (Blue), expected Points Tally (Orange), and the difference between the two (green)

x1 = df['League Position']
y1=df['Pts']
x2=df['League Position']
y2=df['xPTS']
x3=df['League Position']
y3=df['PTS-xPTS']

font1={'family':'serif','color':'blue','size':20}
font2= {'family':'serif','color':'darkred','size':15}

plt.plot(x1,y1,x2,y2,x3,y3)
plt.xlabel("League Position", fontdict = font2)
plt.ylabel("Points", fontdict = font2)
plt.title("Pts,xPts & Pts-xPts vs League Position", fontdict = font1)


# In[ ]:


#all data was gathered either directly from the premier league website (https://www.premierleague.com/stats) or from various databases working in conglomeration with the premier league (https://understat.com/league/EPL)
#All data is open for public use and was gathered and organized by Luke Brach

