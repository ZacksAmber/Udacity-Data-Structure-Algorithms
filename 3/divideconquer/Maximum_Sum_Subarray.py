# Solution

'''Helper Function - Find the max crossing sum w.r.t. middle index'''
def maxCrossingSum(arr, start, mid,  stop):
    '''LEFT PHASE - Traverse the Left part starting from mid element'''
    leftSum = arr[mid]                                     # Denotes the sum of left part from mid element to the current element
    leftMaxSum = arr[mid]                                  # Keep track of maximum sum
    
    # Traverse in reverse direction from (mid-1) to start 
    for i in range(mid-1, start-1, -1):                    # The second argument of range is not inclusive. Third argument is the step size.
        leftSum = leftSum + arr[i]
        if (leftSum > leftMaxSum):                         # Update leftMaxSum
            leftMaxSum = leftSum
    
    '''RIGHT PHASE - Traverse the Right part, starting from (mid+1)'''
    rightSum = arr[mid+1]                                  # Denotes the sum of right part from (mid+1) element to the current element
    rightMaxSum = arr[mid+1]                               # Keep track of maximum sum
    
    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid+2, stop+1):                         # The second argument of range is not inclusive
        rightSum = rightSum + arr[j]
        if (rightSum > rightMaxSum):                       # Update rightMaxSum
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would contain value of atleast one element from the arr'''
    return (rightMaxSum + leftMaxSum)

'''Recursive function'''
def maxSubArrayRecursive(arr, start, stop):                # start and stop are the indices
    # Base case
    if (start==stop):
        return arr[start]

    if(start < stop):
        mid = (start+stop)//2                              # Get the middle index
        L = maxSubArrayRecursive(arr, start, mid)          # Recurse on the Left part
        R = maxSubArrayRecursive(arr, mid+1, stop)         # Recurse on the Right part
        C = maxCrossingSum(arr, start, mid, stop)          # Find the max crossing sum w.r.t. middle index
        return max(C, max(L,R))                            # Return the maximum of (L,R,C)
    
    else:                                                  # If ever start > stop. Not feasible. 
        return nums[start]

def maxSubArray(arr):
    start = 0                      # staring index of original array
    stop = len(arr) -1             # ending index of original array
    return maxSubArrayRecursive(arr, start, stop)
