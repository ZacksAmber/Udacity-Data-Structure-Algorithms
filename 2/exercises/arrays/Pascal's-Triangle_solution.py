# Solution

'''
Points to note:
1. We have to return a list.
2. The elements of n^th row are made up of elements of (n-1)^th row. This comes up till the 1^st row. We will follow a top-down approach. 
3. Except for the first and last element, any other element at position `j` in the current row is the sum of elements at position `j` and `j-1` in the previous row. 
4. Be careful about the edge cases, example, an index should never be a NEGATIVE at any point of time. 
'''

def nth_row_pascal(n):
    
    if n == 0:
        return [1]
    
    current_row = [1] # First row
    
    ''' Loop from 1 to n; `i` denotes the row number'''
    for i in range(1, n + 1):
        # Set the `current_row` from previous iteration as the `previous_row`
        previous_row = current_row
        
        # Let's build the fresh current_row gradually
        current_row = [1] # add the default first element at the 0^th index of the `i^th` row
        
        '''Loop from 1 to (i-1); `j` denotes the index of an element with in the `i^th` row'''
        # Example, for 5th row we have considered n=4, 
        # we will iterate index from 1 to 3, because 
        # the default element at the 0^th index has already been added
        for j in range(1, i):
            
            # An element at position `j` in the current row is the 
            # sum of elements at position `j` and `j-1` in the previous row.
            next_number = previous_row[j] + previous_row[j - 1]
            
            # Append the new element to the current_row
            current_row.append(next_number)
            
        current_row.append(1) # append the default last element
    return current_row