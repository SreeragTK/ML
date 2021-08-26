#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import random
import matplotlib.pyplot as plt
X= np.random.randint(0,50,(150))
C= np.random.randint(-30,30,(150))
Y=[]
for i in range(150):
    k=6*X[i] + C[i]
    Y.append(k)
plt.scatter(X,Y)


# In[ ]:




