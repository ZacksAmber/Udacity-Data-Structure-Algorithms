# Recursive Solution
def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """
    # Base case 
    if arr == [9]:
        return [1, 0]
    
    # A simple case, where we just need to increment the last digit
    if arr[-1] < 9:
        arr[-1] += 1

    # Case when the last digit is 9.
    else:
        '''Recursive call'''
        # We have used arr[:-1], that means all elements of the list except the last one.
        # Example, for original input arr=[1,2,9], we will pass [1,2] in next call.
        arr = add_one(arr[:-1]) + [0]
        
    return arr

