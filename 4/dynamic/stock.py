# Solution

def max_returns(arr):
    min_price_index = 0
    max_price_index = 1
    current_min_price_index = 0
    
    if len(arr) < 2:
        return
    
    for index in range(1, len(arr)):
        # current minimum price
        if arr[index] < arr[current_min_price_index]:
            current_min_price_index = index
            
        # current max profit
        if arr[max_price_index] - arr[min_price_index] < arr[index] - arr[current_min_price_index]:
            max_price_index = index
            min_price_index = current_min_price_index
    max_profit = arr[max_price_index] - arr[min_price_index]
    return max_profit