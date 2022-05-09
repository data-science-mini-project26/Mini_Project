#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import time 
rng = pd.date_range('2022/01/04','2022/01/27' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-data/proj-b/LOB_csv/2022-01-04-LOB.csv
        tmp = pd.read_csv("s3://project-b-data/proj-b/LOB_csv/{}-LOB.csv".format(date))[::1800]
        data_list.append(tmp)


# In[3]:


ans1=pd.concat(data_list)


# In[4]:


ans1


# In[5]:


ans1.to_csv(f"s3://project-b-data/11.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/01/28','2022/02/22' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_2 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-data/proj-b/LOB_csv/2022-01-04-LOB.csv
        tmp = pd.read_csv("s3://project-b-data/proj-b/LOB_csv/{}-LOB.csv".format(date))[::1800]
        data_list_2.append(tmp)


# In[2]:


ans2=pd.concat(data_list_2)


# In[3]:


ans2


# In[4]:


ans2.to_csv(f"s3://project-b-data/22.csv",index = False)


# In[3]:


import pandas as pd
import time 
rng = pd.date_range('2022/02/23','2022/04/29' ,freq='D').strftime('%Y-%m-%d').tolist()
rng.remove('2022-02-28')
rng.remove('2022-03-07')
rng.remove('2022-03-11')
rng.remove('2022-04-15')
rng.remove('2022-04-18')
data_list_2 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-data/proj-b/LOB_csv/2022-01-04-LOB.csv
        tmp = pd.read_csv("s3://project-b-data/proj-b/LOB_csv/{}-LOB.csv".format(date))[::1800]
        data_list_2.append(tmp)


# In[ ]:


import pandas as pd
tmp = pd.read_csv("s3://project-b-data/proj-b/LOB_csv/Full_LOB/New_Full_LOB1.csv")[::1800]


# In[2]:


import pandas as pd
import time 
rng = pd.date_range('2022/01/04','2022/01/14' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list.append(tmp)


# In[3]:


ans1=pd.concat(data_list)


# In[4]:


ans1


# In[5]:


ans1=pd.concat(data_list)


# In[6]:


ans1.to_csv(f"s3://project-b-data/11.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/01/15','2022/01/26' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_2 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_2.append(tmp)


# In[2]:


ans2=pd.concat(data_list_2)


# In[3]:


ans2


# In[4]:


ans2.to_csv(f"s3://project-b-data/22.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/01/27','2022/02/07' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_3 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_3.append(tmp)


# In[2]:


ans3=pd.concat(data_list_3)


# In[3]:


ans3


# In[4]:


ans3.to_csv(f"s3://project-b-data/33.csv",index = False)


# In[2]:


import pandas as pd
import time 
rng = pd.date_range('2022/02/08','2022/02/17' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_4 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_4.append(tmp)


# In[3]:


ans4=pd.concat(data_list_4)


# In[4]:


ans4


# In[5]:


ans4.to_csv(f"s3://project-b-data/44.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/02/18','2022/03/03' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-02-28')
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_5 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_5.append(tmp)


# In[2]:


ans5=pd.concat(data_list_5)


# In[3]:


ans5


# In[4]:


ans5.to_csv(f"s3://project-b-data/55.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/03/04','2022/03/16' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_6 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_6.append(tmp)


# In[2]:


ans6=pd.concat(data_list_6)


# In[3]:


ans6


# In[4]:


ans6.to_csv(f"s3://project-b-data/66.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/03/17','2022/03/30' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_7 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_7.append(tmp)


# In[2]:


ans7=pd.concat(data_list_7)


# In[3]:


ans7


# In[4]:


ans7.to_csv(f"s3://project-b-data/77.csv",index = False)


# In[2]:


import pandas as pd
import time 
rng = pd.date_range('2022/03/31','2022/04/14' ,freq='D').strftime('%Y-%m-%d').tolist()
# rng.remove('2022-04-15')
# rng.remove('2022-04-18')
data_list_8 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_8.append(tmp)


# In[3]:


ans8=pd.concat(data_list_8)


# In[4]:


ans8


# In[5]:


ans8.to_csv(f"s3://project-b-data/88.csv",index = False)


# In[1]:


import pandas as pd
import time 
rng = pd.date_range('2022/04/19','2022/04/29' ,freq='D').strftime('%Y-%m-%d').tolist()
data_list_9 = []
for date in rng:
    if time.strptime(date,'%Y-%m-%d').tm_wday<5:
        print(date)
        ##print('https://dsc-mp2022.s3.amazonaws.com/proj-b/dataset-b01/Tst{}tapes.csv'.format(date))

# s3://project-b-new/LOB_csv/LOB_csv3/2022-01-04-LOB-B03.csv
        tmp = pd.read_csv("s3://project-b-new/LOB_csv/LOB_csv3/{}-LOB-B03.csv".format(date))[::1800]
        data_list_9.append(tmp)


# In[2]:


ans9=pd.concat(data_list_9)


# In[3]:


ans9


# In[5]:


ans9.to_csv(f"s3://project-b-data/99.csv",index = False)


# In[16]:


a=pd.read_csv("s3://project-b-data/11.csv")


# In[17]:


b=pd.read_csv("s3://project-b-data/22.csv")


# In[18]:


c=pd.read_csv("s3://project-b-data/33.csv")


# In[19]:


d=pd.read_csv("s3://project-b-data/44.csv")


# In[20]:


e=pd.read_csv("s3://project-b-data/55.csv")


# In[21]:


f=pd.read_csv("s3://project-b-data/66.csv")


# In[22]:


g=pd.read_csv("s3://project-b-data/77.csv")


# In[23]:


h=pd.read_csv("s3://project-b-data/88.csv")


# In[24]:


i=pd.read_csv("s3://project-b-data/99.csv")


# In[25]:


z =[a,b,c,d,e,f,g,h,i]


# In[26]:


z = pd.concat(z)


# In[27]:


z.to_csv(f"s3://project-b-data/b03.csv",index = False)

