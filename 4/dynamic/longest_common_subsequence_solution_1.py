def lcs(string_a, string_b):
    
    # initialize the matrix 
    lookup_table = [[0 for x in range(len(string_b) + 1)] for x in range(len(string_a) + 1)]
    
    # enumerate(str) returns a tuple containing the index and character in each iteration
    for char_a_i, char_a in enumerate(string_a):
        
        for char_b_i, char_b in enumerate(string_b):
            
            # If there is a match, 
            # fill that grid cell with the value to the top-left of that cell plus one
            if char_a == char_b:
                lookup_table[char_a_i + 1][char_b_i + 1] = lookup_table[char_a_i][char_b_i] + 1
                
            # If there is not a match, 
            # take the maximum value from either directly to the left or the top cell
            else:
                lookup_table[char_a_i + 1][char_b_i + 1] = max(
                    lookup_table[char_a_i][char_b_i + 1],
                    lookup_table[char_a_i + 1][char_b_i])

    # the bottom-right cell will hold the non-normalized LCS length value.
    return lookup_table[-1][-1]