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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
from utils.iloc import iloc

# Combine all phone numbers from csv texts and calls
allPhoneNumbers = iloc(texts, ':', 0) + iloc(texts, ':', 1) + iloc(calls, ':', 0) + iloc(calls, ':', 1)
print(f"There are {len(set(allPhoneNumbers))} different telephone numbers in the records.")

""" # Validation
>>> import pandas as pd
>>> df_texts = pd.read_csv('texts.csv', header=None)
>>> df_texts.columns = ['sending', 'receiving', 'timestamp']
>>> df_calls = pd.read_csv('calls.csv', header=None)
>>> df_calls.columns = ['calling', 'receiving', 'timestamp', 'duration']
>>> all_numbers = list(df_texts.sending) + list(df_texts.receiving) + list(df_calls.calling) + list(df_calls.receiving)
>>> print(len(set(all_numbers)))
570
"""