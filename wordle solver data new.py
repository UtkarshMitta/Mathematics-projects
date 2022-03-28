#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.read_csv('5_letters.csv')
temp=[]
for word in df['1']+df['2']+df['3']+df['4']+df['5']:
    temp.append(str(word))
print(temp)
attempts={}


# In[5]:


for test in temp[100:200]:
    df=pd.read_excel("Five_words.xlsx")
    word_list=[]
    for word in df["words"]:
        word_list.append(str(word))
    
    def unique(s):
        dic={}
        for i in range(len(s)):
            dic[s[i]]=dic.get(s[i],0)+1
        return len(dic)
    def frequency_score(word_list):
        dic={}
        for index in range(5):
            for word in word_list:
                dic[word[index]]=dic.get(word[index],0)+1
        ans_list=[]
        for word in word_list:
            score=0
            for letter in range(5):
                score+=dic[word[letter]]
            ans_list.append((score,word))
        ans_list=sorted(ans_list,reverse=True)
        fin=[]
        num=5
        while num>0:
            for tup in ans_list:
                if unique(tup[1])==num:
                    fin.append(tup[1])
            num=num-1
        return fin[0]
     
    inp=test
    guess=frequency_score(word_list)
    attempt=1
    valid=1
    while guess!=inp:
        if inp not in word_list:
            valid=0
            print("Invalid input")
            break
        attempt+=1
        undesirable=[]
        for letter in range(5):
            if guess[letter]==inp[letter]:
                for word in word_list:
                    if word[letter]!=guess[letter]:
                        undesirable.append(word)
        for letter in range(5):
            if guess[letter]!=inp[letter]:
                for word in word_list:
                    if word[letter]==guess[letter]:
                        undesirable.append(word)
                if guess[letter] in inp:
                    for word in word_list:
                        if guess[letter] not in word:
                            undesirable.append(word)
                else:
                    for word in word_list:
                        if guess[letter] in word:
                            undesirable.append(word)
        desirable=[]
        for word in word_list:
            if word not in undesirable:
                desirable.append(word)
        word_list=desirable
        if attempt<3:
            guess=frequency_score(word_list)
        else:
            guess=word_list[0]
    attempts[attempt]=attempts.get(attempt,0)+1
    print('done')
print(attempts)


# In[6]:


x=[]
y=[]
for key in attempts:
    x.append(key)
    y.append(attempts[key]/100)
from matplotlib import pyplot as plt
plt.bar(x,y)


# In[8]:


expectation=0
for key in attempts:
    expectation+=key*attempts[key]
print(expectation/100)


# In[ ]:




