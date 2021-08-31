#!/usr/bin/env python
# coding: utf-8

# In[26]:


fs = open("SRR072893.sam")
n = 0
for line in fs:
    if line.startswith("@"):
        pass
    else:    
        n += 1
print(n)


# In[28]:


fs = open("SRR072893.sam")
m = 0
for line in fs:
    if line.startswith("@"):
        pass
    else:    
        field = line.split()
        if field[5] == "40M":
            m+=1
print(n)


# In[38]:


fs = open("SRR072893.sam")
a = 0
t = 0
for line in fs:
    if line.startswith("@"):
        pass
    else:    
        field = line.split()
        a = a + int(field[4])
        t += 1
print(a)
print(t)
print(a/t)


# In[50]:


fs = open("SRR072893.sam")
z = 0
for line in fs:
    if line.startswith("@"):
        pass
    else:    
        field = line.split()
        if int("10000" <= field[3] <= "20000") & int(field[2] == "2L"):
            z += 1
print(z)


# In[48]:


if 4<3 and 4>2:
    print("Yes")


# In[51]:


a_list = [1,1,2,2,3]
a_set = set(a_list)
print(a_set)


# In[54]:


fs = open("SRR072893.sam")
q = []
for line in fs:
    if line.startswith("@"):
        pass
    else:    
        field = line.split()
        q.append(field[5])
print(q)
print(len(q))


# In[58]:


u = set(q)
print(u)
print(len(u))


# In[ ]:




