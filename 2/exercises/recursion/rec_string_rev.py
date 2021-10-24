# Solution
"""
RECURSIVE FUNCTION
Args: input(str): string to be reversed
Returns: a string that us reversed of input
"""
def reverse_string(input):
    
    # (Recursion) Termination condition / Base condition
    if len(input) == 0:
        return ""

    else:
        first_char = input[0]
        
        '''
        The `slice()` function can accept upto the following three arguments.
        - start: [OPTIONAL] starting index. Default value is 0.
        - stop: ending index (exclusive)
        - step_size: [OPTIONAL] the increment size. Default value is 1.
        
        The return type of `slice()` function is an object of class 'slice'. 
        '''
        the_rest = slice(1, None)     # `the_rest` is an object of type 'slice' class
        sub_string = input[the_rest]  # convert the `slice` object into a list
        
        # Recursive call
        reversed_substring = reverse_string(sub_string)
        
        return reversed_substring + first_char
#-------------------------------------------------#
'''
**Time and Space Complexity Analysis**
Each recursive call to the `reverse_string()` function will create 
a new set of local variables - first_char, the_rest, sub_string, and reversed_substring. 
Therefore, the space complexity of a recursive function would always be proportional to the 
maximum depth of recursion stack.  
The time complexity for this function will be  O(k*n), where k is a constant and n is the 
number of characters in the string (depth of recursion stack). 
'''