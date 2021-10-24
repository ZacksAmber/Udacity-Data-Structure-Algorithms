
# Recursive Solution
def keypad(num):
    
    # Base case
    if num <= 1:
        return [""]

    # If `num` is single digit, get the LIST having one element - the associated string
    elif 1 < num <= 9:
        return list(get_characters(num))

    # Otherwise `num` >= 10. Find the unit's (last) digits of `num` 
    last_digit = num % 10
    
    '''Step 1'''
    # Recursive call to the same function with “floor” of the `num//10`
    small_output = keypad(num//10)               # returns a LIST of strings
    
    '''Step 2'''
    # Get the associated string for the `last_digit`
    keypad_string = get_characters(last_digit)   # returns a string
    
    '''Permute the characters of result obtained from Step 1 and Step 2'''
    output = list()

    '''
    The Idea:
    Each character of keypad_string must be appended to the 
    end of each string available in the small_output
    '''
    for character in keypad_string:
        for item in small_output:
            new_item = item + character
            output.append(new_item)
    
    return output                                # returns a LIST of strings


