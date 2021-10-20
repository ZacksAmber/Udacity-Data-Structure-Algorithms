"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import re
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def telemarketers():
    # Extract records
    # Time Complexity: O(1) -> zip
    # Time Complexity: O(n) -> zip to list
    callings = list(zip(*calls))[0]
    telemarketers = []
    # Time Complexity: O(n)
    for phone_number in callings:
        # Time Complexity: O(n)
        if re.findall('^140.+', phone_number) != []:
            telemarketers.append(phone_number)

    # Time Complexity: O(n)
    telemarketers = list(set(telemarketers))
    # Time Complexity: O(n log n)
    telemarketers.sort()
    print("These numbers could be telemarketers: ")
    # Time Complexity: O(n)
    for phone_number in telemarketers:
        print(phone_number)


telemarketers()


"""Validation
>>> import pandas as pd
>>> df_texts = pd.read_csv('texts.csv', header=None)
>>> df_texts.columns = ['sending', 'receiving', 'timestamp']
>>> df_calls = pd.read_csv('calls.csv', header=None)
>>> df_calls.columns = ['calling', 'receiving', 'timestamp', 'duration']
>>> filter = df_calls.calling.str.contains('[()\s]', regex=True) # len 100
>>> telemarketers = df_calls[~filter].calling.unique() # len 15
"""
