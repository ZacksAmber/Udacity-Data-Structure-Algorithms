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
def total_durations():
    """total_durations parses callings, receivings, and durations from .csv calls.

    Returns:
        dict: total duration for each phone number.
    """
    # Extract records
    # Time Complexity: O(1) -> zip
    # Time Complexity: O(n) -> zip to list
    callings = list(zip(*calls))[0]
    receivings = list(zip(*calls))[1]
    durations = list(zip(*calls))[3]

    # Convert durations from str to int
    # Time Complexity: O(n)
    durations = list(map(int, durations))

    total_durations = {}
    # Time Complexity: O(n)
    for i in range(len(durations)):
        # Time Complexity: O(1)
        calling = callings[i]
        receiving = receivings[i]
        duration = durations[i]
        phone_numbers = total_durations.keys()
        # Add calling number duration
        # Time Complexity: O(n)
        if calling in phone_numbers:
            # Time Complexity: O(1)
            total_durations[calling] += duration
        else:
            # Time Complexity: O(1)
            total_durations[calling] = duration
        # Add receiving number duration
        # Time Complexity: O(n)
        if receiving in phone_numbers:
            # Time Complexity: O(1)
            total_durations[receiving] += duration
        else:
            # Time Complexity: O(1)
            total_durations[receiving] = duration

    return total_durations

# Time Complexity: O(n)
max_duration = max(total_durations().values())
# Time Complexity: O(n)
max_duration_number = max(total_durations(), key=total_durations().get)

print(f"{max_duration_number} spent the longest time, {max_duration} seconds, on the phone during September 2016.")


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
