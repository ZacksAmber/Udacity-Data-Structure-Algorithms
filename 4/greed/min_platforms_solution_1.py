def min_platforms(arrival, departure):
    if(len(arrival) != len(departure)): # Mismatch in the length of the lists
        return -1

    # Sort both the lists.    
    arrival.sort()
    departure.sort()
    
    platform_required = 1              # Count of platforms required at the moment when comparing i^th arrival and j^th departure
    max_platform_required = 1          # Keep track of the max value of platform_required

    # Iterate such that (i-j) will represent platform_required at that moment
    i = 1
    j = 0

    # Traverse the arrival list with iterator `i`, and departure with iterator `j`.
    while i < len(arrival) and j < len(arrival):
        
        # if i^th arrival is scheduled before than j^th departure, 
        # increment platform_required and i as well.
        if arrival[i] < departure[j]:
            platform_required += 1
            i += 1

            # Update the max value of platform_required
            if platform_required > max_platform_required:
                max_platform_required = platform_required
         
        # Otherwise, decrement platform_required count, and increase j.
        else:
            platform_required -= 1
            j += 1

    return max_platform_required