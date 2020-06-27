#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# upload the data
url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"
#read the data from an excel file 
properties=pd.read_excel(url_LondonHousePrices,sheet_name='Average price',index_col=None)
print(properties.head())
properties.info() # examine the data


# In[ ]:







# In[16]:


# Switch columns and rows
properties=properties.transpose()


# In[81]:


print(properties.head())
print(properties.tail())


# In[88]:


properties.reset_index()


# In[92]:


properties_z=properties.transpose()
print (properties_z.head())


# In[95]:


properties.reset_index()


# In[97]:


properties.rename(columns={'Unnamed: 0':'Date'}, inplace=True) 
print (properties.head())


# In[100]:


#remove Unnamed cols
properties=properties.dropna(axis=1,how='all')
print (properties.head())


# In[ ]:





# In[ ]:





# In[98]:





# In[ ]:





# In[29]:


# to pullout the main 33 districts from the dataframe

properties33D=properties_z.iloc[:,0:34] 
print(properties33D)


# In[31]:


properties33Dtranspose=properties33D.transpose()
#Del NaT
del properties33Dtranspose[0]
properties33Dfinal=properties33Dtranspose.transpose()
# Remove City of London from columns
properties32Dfinal=properties33Dfinal.drop(properties33Dfinal.columns[1], axis =1)
print(properties32Dfinal)


# In[32]:


properties32Dfinal.info()


# In[148]:


# set Date as Index
properties32Dfinal.set_index("Date") # final Data frame after cleaning, filtering and reindexing


# In[149]:


London_Borough=list (properties32Dfinal.columns.values)
del London_Borough[0]
print(London_Borough)


# In[150]:


# visualize two distrcits growth
plot= properties32Dfinal.plot(x='Date',y=['Haringey', 'Kingston upon Thames'] )
plot.set_ylabel('Ave Price')


# In[151]:


# visualize all distrcits growth

plot= properties32Dfinal.plot(x='Date',y=London_Borough)
plot.set_ylabel('Ave Price')


# In[ ]:





# In[37]:



# Changing the data type to float
cols = properties32Dfinal.select_dtypes(exclude=['datetime']).columns

properties32Dfinal[cols] = properties32Dfinal[cols].apply(pd.to_numeric, downcast='float', errors='coerce')

properties32Dfinal.info()


# In[140]:



#seperate the Year from the Date
# didnot need this just to try this command
year=properties32Dfinal['Date'].dt.year
print (year)


# In[64]:


# add year to data frame
properties32Dfinal['Year'] = pd.DatetimeIndex(properties32Dfinal['Date']).year

print (properties32Dfinal.tail())


# In[112]:


# Change the Index to Year
properties32Dfinal.set_index('Year', drop=True, append=False, inplace=False, verify_integrity=False)   


# In[147]:


properties32Dfinal.info()


# In[141]:


mean1995=properties32Dfinal[London_Borough].loc[properties32Dfinal['Date'].dt.year==1995].mean(axis=0)
print (mean1995)


# In[139]:


mean2018=properties32Dfinal[London_Borough].loc[properties32Dfinal['Date'].dt.year==2018].mean(axis=0)
print(mean2018)


# In[146]:


growth=(mean2018-mean1995)*100/mean1995
print(growth)


# In[157]:


growthofboroughs={'Mean_1995': mean1995, 'Mean_2018': mean2018,'Growth':growth}
growthdf = pd.DataFrame(growthofboroughs)

print(growthdf)


# In[170]:


growthdf.reset_index()


# In[177]:


print (growthdf.index.name)


# In[180]:


growthdf.index.names = ['Boroughs']
print (growthdf)


# In[183]:


growthdf['Growth'].max()


# In[184]:


growthdf[growthdf['Growth'] == growthdf['Growth'].max()].index[0]


# In[ ]:





# In[227]:





# In[ ]:





# In[ ]:



 


# In[ ]:





# In[ ]:




