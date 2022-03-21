#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data = [1.1,1.3,1.3,1.7,1.7,2.0,2.0,2.2,2.4,
        2.4,2.6,2.6,2.6,3.1,3.4,3.5,3.7,3.7]


# In[76]:


plt.hist(data, range=(1,3), bins=50)
plt.show()


# In[77]:


plt.hist(data, density=True)


# In[78]:


counts, bins = np.histogram(data)
plt.hist(bins[:-1], bins, weights=counts)


# In[ ]:


#Kesimpulan
#Mempermudah dalam menganalisis
#membuat beberapa variabel memiliki rentang nilai yang sama, tidak ada yang terlalu besar maupun terlalu kecil

