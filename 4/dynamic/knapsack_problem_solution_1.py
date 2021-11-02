# DP Solution
# Get the maximum total value ($) of items that can be accommodated into the given knapsack
def knapsack_max_value(knapsack_max_weight, items):
    
    # Initialize a lookup table to store the maximum value ($) 
    lookup_table = [0] * (knapsack_max_weight + 1)


    # Iterate down the given list
    for item in items:
        
        # The "capcacity" represents amount of remaining capacity (kg) of knapsack at a given moment. 
        for capacity in reversed(range(knapsack_max_weight + 1)):
            
            if item.weight <= capacity:
                lookup_table[capacity] = max(lookup_table[capacity], lookup_table[capacity - item.weight] + item.value)

    return lookup_table[-1]