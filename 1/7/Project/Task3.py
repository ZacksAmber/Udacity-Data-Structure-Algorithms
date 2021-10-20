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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""


def called_from_Bangalore():
    """called_from_Bangalore prints the unique phone numbers called from Bangalore. 
    """
    # Extract records
    # Time Complexity: O(1) -> zip
    # Time Complexity: O(n) -> zip to list
    callings = list(zip(*calls))[0]
    receivings = list(zip(*calls))[1]

    # Extract all of the Bangalore phone number index from callings
    # Time Complexity: O(n)
    idx = []
    for i in range(len(callings)):
        if '(080)' in callings[i]:
            # Time Complexity: O(1)
            idx.append(i)

    # Extract all phone numbers from receivings match the index in idx
    # Time Complexity: O(n)
    called_from_Bangalore = [receivings[i] for i in idx]
    # Extract the prefix or area code.
    # Time Complexity: O(n)
    all_prefix_or_area_code = []
    for phone_number in called_from_Bangalore:
        prefix_or_area_code = re.findall(
            r'\(0\d.+\)|[789]\d+\s|^140', phone_number)[0]
        # The prefix is the first 4 digits of a phone_number.
        # Time Complexity: O(3)
        if re.match('^[789]', prefix_or_area_code):
            # Time Complexity: O(4)
            prefix_or_area_code = prefix_or_area_code[:4]
        all_prefix_or_area_code.append(prefix_or_area_code)
    # Use set to output unique phone numbers
    # Time Complexity: O(n)
    uniques = list(set(all_prefix_or_area_code))
    # Sort
    # Time Complexity: O(n log n)
    uniques.sort()
    # Output
    # Time Complexity: O(n)
    print("The numbers called by people in Bangalore have codes:")
    for i in uniques:
        print(i)

called_from_Bangalore()


"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def called_to_Bangalore():
    """called_from_Bangalore prints the unique phone numbers called from Bangalore. 
    """
    # Extract records
    # Time Complexity: O(1) -> zip
    # Time Complexity: O(n) -> zip to list
    callings = list(zip(*calls))[0]
    receivings = list(zip(*calls))[1]

    # Extract all of the Bangalore phone number index from callings
    # Time Complexity: O(n)
    idx = []
    for i in range(len(callings)):
        if '(080)' in callings[i]:
            # Time Complexity: O(1)
            idx.append(i)

    # Extract all phone numbers from receivings match the index in idx
    # Time Complexity: O(n)
    called_from_Bangalore = [receivings[i] for i in idx]
    # Use set to output unique phone numbers
    # Time Complexity: O(n)
    count = 0
    for phone_number in called_from_Bangalore:
        if '(080)' in phone_number:
            count += 1

    # Sort
    # Time Complexity: O(nlogn)
    called_from_Bangalore.sort()
    # Output
    # O(1)
    percentage = round(count / len(called_from_Bangalore) * 100, 2)
    print(f"{percentage}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


called_to_Bangalore()


"""Validation
>>> import pandas as pd
>>> df_calls = pd.read_csv('calls.csv', header=None)
>>> df_calls.columns = ['calling', 'receiving', 'timestamp', 'duration']
>>> filter = df_calls.calling.str.contains('(080)', regex=False)
>>> all_prefix_or_area_code = df_calls[filter].receiving.str.findall(r'\(0\d.+\)|[789]\d+\s|^140')
>>> all_prefix_or_area_code = all_prefix_or_area_code.apply(
    lambda x: x[0])  # Remove the list bracket
>>> uniques = all_prefix_or_area_code.apply(lambda x: x[:4] if re.match('^[789]', x) else x).sort_values().unique()
>>> for i in uniques:
            print(i)
>>> filter1 = df_calls.calling.str.contains('(080)', regex=False)
>>> filter2 = df_calls.receiving.str.contains('(080)', regex=False)
>>> called_to_Bangalore = df_calls[filter1 & filter2].receiving
>>> called_from_Bangalore = list(df_calls[filter].receiving)
>>> percentage = round(len(called_to_Bangalore) / len(called_from_Bangalore)*100, 2)
>>> print(f'{percentage}%')
"""
