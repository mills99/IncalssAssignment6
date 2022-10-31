#!/usr/bin/env python
# coding: utf-8

# In[65]:


#Does being female mean that the average exam score will be higher or lower? Does doing a test prep course get you a higher score
import pandas
df = pd.read_csv("exams.csv")
df["combined scores"] = ((df["math score"] + df["reading score"] + df["writing score"])/300)*100
df.head(5)


# In[69]:


'''
The data above shows exam scores of students allong with their parent's level of education, test prep, gender race/ethnicity
and lunch status. In the first graph we want to see the mean test scores of students who have completed
a test prep course compared to a student who has not completed one.
We see that the students who have completed a test prep course have a higher mean compared to the students who have not.

'''

import seaborn as sns
import matplotlib.pyplot as plt

df1 = df.groupby('test preparation course')[['combined scores']].mean()
df1.values[0,0:2]
df1

sns.barplot(data=df1,y=df1.values[0:2,0],x=df1.index)
plt.ylabel('combined scores')


# In[62]:


'''
In the second graph we want to see the mean test scores of each subject based on gender. First we group by gender.
We then want to see the mean score of each exam so we combine gender with each score of the exams. 
The graph shows Malestudents have a higher math score while females have higher reading and writing scores
'''

df4=df.groupby('gender')[['math score','reading score','writing score']].mean()
print(df4)
df4.plot(kind='bar',grid=True)


# In[ ]:




