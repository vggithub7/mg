# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:11:20 2020

@author: amma bau ji
"""

import praw
import sys
import pandas as pd
##reddit=praw.Reddit(client_id='Nc-Weg3_ZpmjpQ',
#                     client_secret="75dtQXd2_TDzVqIUxMtK6QNS6Fc", 
#                     user_agent='Testing1_api')
name='%s'%(sys.argv[1])
a="apple"
name=a
print(name)
"""

subNews=reddit.subreddit(name).hot(limit=10)
A=[]
d=0
for post in subNews:
    A.append([post.title,post.link_flair_text])
    d+=1	
A=pd.DataFrame(A,columns=['title','flare'])
#print(A)
c=""
dd=""
for i in range(d):
	dd=str(A[i+1:i+2]).ljust(280,'*')+'|'
	c=c+dd
name=c #str(A[1:2])+"              "+str(A[2:3])
print(name)

filename = "%s.csv" % name
A.to_csv(filename,index=False)
sd2=[]
s=[]
for i in A.flare:
    s.append(i)
import matplotlib.pyplot as plt
for i in set(A.flare):
    if type(i)==str:
        sd2.append([i, s.count(i)])
sd2=pd.DataFrame(sd2,columns=['title','count'])
x = sd2['title']
y= sd2['count']
'''['Photography', 'Scheduled', 'Policy/Economy', 'TIL','Official Announcement', 'CAA-NRC-NPR', 'AskIndia', 'Politics', 'Business/Finance', 'Sports', 'Food', 'Science/Technology',
 'Coronavirus',
 'Non-Political']
y = [13,9, 60, 1, 1, 6, 101, 123, 33, 4, 10, 13, 271, 118]
'''
labels = sd2['title']

plt.plot(x, y)
# You can specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(x, labels, rotation='vertical')
# Pad margins so that markers don't get clipped by the axes
plt.margins(0.2)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.15)
plt.grid()
plt.show()
"""