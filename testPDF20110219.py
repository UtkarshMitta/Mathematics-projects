#!/usr/bin/env python
# coding: utf-8

# # Continuous random variable: Normal distribution

# In[14]:


# Normal distribution with mean=10 and standard deviation=4
import random
import numpy
import matplotlib.pyplot as plt
k=100000
a=[]
for i in range(k):
    n=numpy.random.normal(10,4)
    a.append(n)
k=len(a)
b=[]
ans_list=[]
isDiscrete=0 #flag variable. Goes high when distribution is discrete
di={}
for ite in a:
    di[ite]=di.get(ite,0)+1
for iteme in di:
    if di[iteme]/k>0.05:
        isDiscrete=1
print("isDiscrete: "+str(isDiscrete))
if isDiscrete==0:
    for ele in range(len(a)):
        c=round(a[ele],1)
        b.append(c)
    dic=dict()
    for item in b:
        dic[item]=dic.get(item,0)+1
    for item in dic:
        dic[item]=dic[item]/(k*0.1)
    lists=sorted(dic.items())
    x_axis,y_axis=zip(*lists)
    y_axis=list(y_axis)
    y_axis[0]*=2
    y_axis[len(y_axis)-1]*=2
    print("sample space:")
    print(x_axis)
    print("PDF values")
    print(y_axis)
    plt.plot(x_axis,y_axis)
    plt.show()
    print(" Continuous distribution. PDF plotted as shown")
    for ele in b:
        ans_list.append(dic[ele])
else:
    dic=dict()
    print("Sample space:")
    print(a)
    for item in a:
        dic[item]=dic.get(item,0)+1
    for item in dic:
        dic[item]=dic[item]/k
    print("PMF values")
    lists=sorted(dic.items())
    x_axis,y_axis=zip(*lists)
    print(y_axis)
    plt.bar(x_axis,y_axis,width=1,align='center')
    plt.show()
    print("Discrete random variable. PMF plotted as shown")
    for ele in a:
        ans_list.append(dic[ele])


# In[15]:


#verifying our graph by generatng a graph with pdf explicitly defined in accordance with normal distribution
import math
e=math.e
pi=math.pi
dicto={}
lis=[]
accuracy=0
for it in a:
    dicto[it]=dicto.get(it,0)+1
    lis.append((e**(-(((it-10)**2)/(2*16))))/((2*pi*16)**0.5))
for key in dicto:
    dicto[key]=(e**(-(((key-10)**2)/(2*16))))/((2*pi*16)**0.5)  #expression of pmf
lists=sorted(dicto.items())
x,y=zip(*lists)
plt.plot(x,y)
plt.show()
for val in range(len(lis)):
    accuracy+=abs(ans_list[val]-lis[val])/lis[val]
accuracy=(1-(accuracy/len(a)))*100
print("Accuracy: "+str(accuracy)+"%")


# # Continuous random variable: Uniform distribution

# In[16]:


# Uniform distribution over 0 and 1
a=[]
for i in range(100000):
    n=random.random()
    a.append(n)
k=len(a)
b=[]
ans_list=[]
isDiscrete=0 #flag variable. Goes high when distribution is discrete
di={}
for ite in a:
    di[ite]=di.get(ite,0)+1
for iteme in di:
    if di[iteme]/k>0.05:
        isDiscrete=1
print("isDiscrete: "+str(isDiscrete))
if isDiscrete==0:
    for ele in range(len(a)):
        c=round(a[ele],1)
        b.append(c)
    dic=dict()
    for item in b:
        dic[item]=dic.get(item,0)+1
    for item in dic:
        dic[item]=dic[item]/(k*0.1)
    lists=sorted(dic.items())
    x_axis,y_axis=zip(*lists)
    y_axis=list(y_axis)
    y_axis[0]*=2
    y_axis[len(y_axis)-1]*=2
    print("sample space:")
    print(x_axis)
    print("PDF values")
    print(y_axis)
    plt.plot(x_axis,y_axis)
    plt.show()
    print("Continuous distribution. PDF plotted as shown")
    for ele in b:
        ans_list.append(dic[ele])
else:
    dic=dict()
    print("Sample space:")
    print(a)
    for item in a:
        dic[item]=dic.get(item,0)+1
    for item in dic:
        dic[item]=dic[item]/k
    print("PMF values")
    lists=sorted(dic.items())
    x_axis,y_axis=zip(*lists)
    print(y_axis)
    plt.bar(x_axis,y_axis,width=1,align='center')
    plt.show()
    print("Discrete random variable. PMF plotted as shown")
    for ele in a:
        ans_list.append(dic[ele])


# In[17]:


#verifying our curve by plugging in the theoretical value of pdf
dicto={}
lis=[]
accuracy=0
for it in a:
    dicto[it]=dicto.get(it,0)+1
    lis.append(1)
for key in dicto:
    dicto[key]=1  #expression of pmf
lists=sorted(dicto.items())
x,y=zip(*lists)
plt.plot(x,y)
plt.show()
for val in range(len(lis)):
    accuracy+=abs(ans_list[val]-lis[val])/lis[val]
accuracy=(1-(accuracy/len(a)))*100
print("Accuracy: "+str(accuracy)+"%")


# # Discrete Random variable: Poisson's distribution

# In[18]:


#Poisson's distribution with mean 4
from scipy.stats import poisson
a=poisson.rvs(mu=4, size=100000)
a=list(a)
k=len(a)
b=[]
ans_list=[]
isDiscrete=0 #flag variable. Goes high when distribution is discrete
di={}
for ite in a:
    di[ite]=di.get(ite,0)+1
for iteme in di:
    if di[iteme]/k>0.05:
        isDiscrete=1
print("isDiscrete: "+str(isDiscrete))
if isDiscrete==0:
    for ele in range(len(a)):
        c=round(a[ele],1)
        b.append(c)
    dic=dict()
    for item in b:
        dic[item]=dic.get(item,0)+1
    for item in dic:
        dic[item]=dic[item]/(k*0.1)
    lists=sorted(dic.items())
    x_axis,y_axis=zip(*lists)
    y_axis=list(y_axis)
    y_axis[0]*=2
    y_axis[len(y_axis)-1]*=2
    print("sample space:")
    print(x_axis)
    print("PDF values")
    print(y_axis)
    plt.plot(x_axis,y_axis)
    plt.show()
    print("Continuous distribution. PDF plotted as shown")
    for ele in b:
        ans_list.append(dic[ele])
else:
    dic=dict()
    print("Sample space:")
    print(a)
    for item in a:
        dic[item]=dic.get(item,0)+1
    for item in dic:
        dic[item]=dic[item]/k
    print("PMF values")
    lists=sorted(dic.items())
    x_axis,y_axis=zip(*lists)
    print(y_axis)
    plt.bar(x_axis,y_axis,width=1,align='center')
    plt.show()
    print("Discrete random variable. PMF plotted as shown")
    for ele in a:
        ans_list.append(dic[ele])


# In[19]:


dicto={}
lis=[]
accuracy=0
for it in a:
    dicto[it]=dicto.get(it,0)+1
    lis.append(poisson.pmf(it,4))
for key in dicto:
    dicto[key]=poisson.pmf(key,4)  #expression of pmf
lists=sorted(dicto.items())
x,y=zip(*lists)
plt.bar(x,y,width=1,align='center')
plt.show()
for val in range(len(lis)):
    accuracy+=abs(ans_list[val]-lis[val])/lis[val]
accuracy=(1-(accuracy/len(a)))*100
print("Accuracy: "+str(accuracy)+"%")


# In[ ]:




