#!/usr/bin/env python
# coding: utf-8

# In[12]:


from pprint import pprint
import csv
from collections import defaultdict 


# In[13]:


f = open('input.csv', 'r')
rows = csv.DictReader(f)


# In[45]:


params = [0.1,0.07,0.11,0.08]


# In[21]:


stationwise = defaultdict(lambda : [])
for row in rows:
    stationwise[row['Station']].append([row['TEMP'], row['TDS'], row['pH'], row['TURB'], row['WQI']])


# In[94]:


# alpha denotes the decay rate
# num_neigh denote the number of previous observations we are going to consider

def weighted_decay(station, alpha, num_neigh):
    error = 0
    for i, entry in enumerate(stationwise[station]):
        
#       Getting the current WQI according to weights
       
        curr_wqi = 0
        for j, vals in enumerate(entry[:-1]):
            curr_wqi += float(vals) * params[j]
        curr_wqi = curr_wqi / sum(params)
        
#       Getting the WQI dependency on previous values
        
        m = num_neigh
        if num_neigh > i:
            m = i
        denm = (1 - pow(alpha, m))/(pow(alpha, m) * (1 - alpha))
        denm += 1
        num = 0
        for j in range(1, m+1):
            num += (1/pow(alpha,j)) * float(stationwise[station][i-j][4])
        predicted_wqi = (curr_wqi + num)/denm
#         print(predicted_wqi, entry[4])
        error += abs(predicted_wqi - float(entry[4]))
    return error/len(stationwise[station])
        
        
        


# In[71]:


station_lists = []
for i in range(1, 10):
    station_lists.append("IND0000" + str(i))
for i in range(10, 71):
    station_lists.append("IND000" + str(i))
print(station_lists)


# In[83]:


for station in station_lists:
    print(station, weighted_decay(station, 1.5, 4))


# In[86]:


rate = 1.01
while rate < 3.01:
    error = 0
    for station in station_lists:
        error += weighted_decay(station, rate, 10)
    print(rate, error)
    rate += 0.01


# In[100]:


# alpha denotes the decay rate
# num_neigh denote the number of previous observations we are going to consider

def weighted_decay_train(station, alpha, num_neigh):
    error = 0
    for i, entry in enumerate(stationwise[station]):
        
#       Getting the WQI dependency on previous values
        if i == 0:
            continue
        m = num_neigh
        if num_neigh > i:
            m = i
        denm = ((1 - pow(alpha, m)) * alpha)/(pow(alpha, m) * (1 - alpha))
        num = 0
        for j in range(0, m):
            num += (1/pow(alpha,j)) * float(stationwise[station][i-j][4])
        predicted_wqi = num/denm
#         print(predicted_wqi, entry[4])
        error += abs(predicted_wqi - float(entry[4]))
    return error/len(stationwise[station])


# In[102]:


weighted_decay_train("IND00004", 2, 4)


# In[101]:


weighted_decay("IND00004", 2, 4)


# In[106]:


rate = 1.01
ys= []
while rate < 3.01:
    error = 0
    for station in station_lists:
        error += weighted_decay_train(station, rate, 100)
    ys.append(error)
    rate += 0.01


# In[107]:


print(ys)


# In[108]:


import matplotlib.pyplot as plt


# In[109]:


plt.plot(ys)


# In[111]:


import csv
from collections import defaultdict

def weighted_decay_wqi(stationwise, station, alpha, num_neig):
    error = 0
    for i, entry in enumerate(stationwise[station]):
#       Getting the WQI dependency on previous values
        if i == 0:
            continue
        m = num_neigh
        if num_neigh > i:
            m = i
        denm = ((1 - pow(alpha, m)) * alpha)/(pow(alpha, m) * (1 - alpha))
        num = 0
        for j in range(0, m):
            num += (1/pow(alpha,j)) * float(stationwise[station][i-j][4])
        predicted_wqi = num/denm
        error += abs(predicted_wqi - float(entry[4]))
    return predicted_wqi

def findWQI(filename):
    f = open(filename, 'r')
    rows = csv.DictReader(f)
    stationwise = defaultdict(lambda : [])
    stations = set()
    for row in rows:
        stationwise[row['Station']].append([row['TEMP'], row['TDS'], row['pH'], row['TURB'], row['WQI']])
        stations.add(row['Station'])
    ans = dict()
    for station in stations:
        val = weighted_decay_wqi(station, 2.03, 25)
        ans[station] = val
    out_f = open("output.csv", "w")
    for station in stations:
        out_f.write(str(station) + "," + str(ans[station]) + "\n")
    out_f.close()


# In[112]:


x = [1,2,3,4]
print(x[-1], x[-2])


# In[ ]:




