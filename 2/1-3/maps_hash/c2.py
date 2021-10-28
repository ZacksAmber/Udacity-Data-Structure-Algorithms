def staircase(n):
    
    # start with a blank dictionary. It will populate in the recursive call
    num_dict = dict({})           
    return staircase_faster(n, num_dict)


'''Recursice function'''
def staircase_faster(n, num_dict):
    ''' 
    Here `n` is a key and `output` would be the corresponding value 
    to be inserted into the dictionary as a pair
    '''
    
    # Base cases
    if n == 1:
        output = 1
    elif n == 2:
        output = 2
    elif n == 3:
        output = 4
    else:
        
        # Simply check if the "value" corresponding to "(n-1)" key is already available in the dictionary
        if (n - 1) in num_dict:
            first_output = num_dict[n - 1]

        # Otherwise, calculate and insert the new key-value pair into the dictioanry
        else:
            first_output =  staircase_faster(n - 1, num_dict)
        
        if (n - 2) in num_dict:
            second_output = num_dict[n - 2]
        else:
            second_output = staircase_faster(n - 2, num_dict)
            
        if (n - 3) in num_dict:
            third_output = num_dict[n - 3]
        else:
            third_output = staircase_faster(n - 3, num_dict)
        
        output = first_output + second_output + third_output
    
    num_dict[n] = output;   # insert a key-value pair in the ORIGINAL dictionary 
    return output

