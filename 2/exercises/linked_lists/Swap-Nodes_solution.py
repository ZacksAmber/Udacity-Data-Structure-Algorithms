# Solution
"""
:param: head- head of input linked list
:param: `position_one` - indicates position (index) ONE
:param: `position_two` - indicates position (index) TWO
return: head of updated linked list with nodes swapped
"""
def swap_nodes(head, position_one, position_two):

    # If both the indices are same
    if position_one == position_two:
        return head
    
    # Helper references
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head 
    new_head = None

    # LOOP - find out previous and current node at both the positions (indices)
    while current_node is not None:
        
        # Position_one cannot be equal to position_two, 
        # so either one of them might be equal to the current_index
        if current_index == position_one:
            one_current = current_node
        
        elif current_index == position_two:
            two_current = current_node
            break

        # If neither of the position_one or position_two are equal to the current_index
        if one_current is None:
            one_previous = current_node
        
        two_previous = current_node
        
        # increment both the current_index and current_node
        current_node = current_node.next         
        current_index += 1
        

    # Loop ends
    
    
    '''SWAPPING LOGIC'''
    # We have identified the two nodes: one_current & two_current to be swapped, 
    # Make use of a temporary reference to swap the references
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp
    
    # if the node at first index is head of the original linked list
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head
    # Swapping logic ends
    
    return new_head