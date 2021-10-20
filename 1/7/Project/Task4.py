"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
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
    receiving_calls= list(zip(*calls))[1]
    sendings = list(zip(*texts))[0]
    receiving_texts = list(zip(*texts))[1]
    # Time Complexity: O(n)
    no_callings = list(set(receiving_texts + sendings + receiving_calls))
    telemarketers = []
    # Time Complexity: O(n)
    for phone_number in list(set(callings)):
        # Time Complexity: O(n)
        if phone_number not in no_callings:
            telemarketers.append(phone_number)

    # Time Complexity: O(n log n)
    telemarketers.sort() # len 43
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
>>> no_callings = df_texts.sending.to_list() + df_texts.receiving.to_list() + df_calls.receiving.to_list()
>>> no_callings = list(set(no_callings))
>>> filter = df_calls.calling.isin(no_callings)
>>> telemarketers = df_calls[~filter].calling.sort_values().unique() # len 43
>>> telemarketers
"""
