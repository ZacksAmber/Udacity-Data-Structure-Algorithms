def longest_consecutive_subsequence(input_list):
    
    # Create a dictionary.
    # Each element of the input_list would become a "key", and
    # the corresponding index in the input_list would become the "value"
    element_dict = dict()

    # Traverse through the input_list, and populate the dictionary
    # Time complexity = O(n) 
    for index, element in enumerate(input_list):
        element_dict[element] = index

    # Represents the length of longest subsequence
    max_length = -1
    
    # Represents the index of smallest element in the longest subsequence
    starts_at = -1  

    # Traverse again - Time complexity = O(n) 
    for index, element in enumerate(input_list):

        current_starts = index
        element_dict[element] = -1         # Mark as visited

        current_count = 1                  # length of the current subsequence

        '''CHECK ONE ELEMENT FORWARD'''
        current = element + 1              # `current` is the expected number

        # check if the expected number is available (as a key) in the dictionary,
        # and it has not been visited yet (i.e., value > 0)
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        while current in element_dict and element_dict[current] > 0:
            current_count += 1             # increment the length of subsequence 
            element_dict[current] = -1     # Mark as visited
            current = current + 1          

            
        '''CHECK ONE ELEMENT BACKWARD'''
        # Time complexity: Constant time for checking a key and retrieving the value = O(1)
        current = element - 1             # `current` is the expected number

        while current in element_dict and element_dict[current] > 0:    
            current_starts = element_dict[current]         # index of smallest element in the current subsequence
            current_count += 1                             # increment the length of subsequence 
            element_dict[current] = -1
            current = current - 1

        '''If length of current subsequence >= max length of previously visited subsequence'''
        if current_count >= max_length:
            if current_count == max_length and current_starts > starts_at:
                continue
            starts_at = current_starts            # index of smallest element in the current (longest so far) subsequence
            max_length = current_count            # store the length of current (longest so far) subsequence


    start_element = input_list[starts_at]          # smallest element in the longest subsequence

    # return a NEW list starting from `start_element` to `(start_element + max_length)` 
    return [element for element in range(start_element, start_element + max_length)]