"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from utils.iloc import iloc

def total_time():
    durations = iloc(calls, ':', 3)
    durations = [int(i) for i in durations]
    callings = iloc(calls, ':', 0)
    receivings = iloc(calls, ':', 1)
    
    nRecords = len(durations)
    totalTime = {}
    for i in range(nRecords):
        '''
        totalTime[callings[i]] += durations[i]
        totalTime[receivings[i]] += durations[i]
        '''
        if callings[i] not in totalTime.keys():
            totalTime[callings[i]] = durations[i]
        else:
            totalTime[callings[i]] += durations[i]
        if receivings[i] not in totalTime.keys():
            totalTime[receivings[i]] = durations[i]
        else:
            totalTime[receivings[i]] += durations[i]
    return totalTime
    
totalTime = total_time()
phone = max(totalTime, key=totalTime.get)
duration = max(totalTime.values())

print(f"{phone} spent the longest time, {duration} seconds, on the phone during September 2016.")

"""Validation
>>> import pandas as pd
>>> df_calls = pd.read_csv('calls.csv', header=None)
>>> df_calls.columns = ['calling', 'receiving', 'timestamp', 'duration']
>>> calling_sum = df_calls.groupby('calling')['duration'].sum().reset_index(name='duration1')
>>> receiving_sum = df_calls.groupby('receiving')['duration'].sum().reset_index(name='duration2')
>>> totalTime = calling_sum.set_index('calling').join(receiving_sum.set_index('receiving')).reset_index()
>>> totalTime.rename(columns = {'calling': 'phone'}, inplace=True)
>>> totalTime['durations'] = totalTime['duration1'] + totalTime['duration2']
>>> print(totalTime.durations.max())
90456.0
>>> print(totalTime[totalTime.durations == totalTime.durations.max()].phone)
91    (080)33251027
Name: phone, dtype: object
"""
