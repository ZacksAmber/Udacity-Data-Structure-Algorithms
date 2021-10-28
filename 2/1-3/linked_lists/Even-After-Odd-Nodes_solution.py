"""
parameter: - head of the given linked list
return: - head of the updated list with all even elements placed after odd elements
"""
#--------------------------------------------------#
'''
The Idea: Traverse the given LinkedList, and build two sub-lists: EVEN and ODD. 
For this purpose, we will use four helper references, that denotes starting and 
current ending of EVEN and ODD sub-list respectively. 

1. For each Node in the LinkedList, check if its data is even/odd. 
Change the "next" reference (pointer) of each Node, based on the following rules:
 - First even valued Node will be referenced by head of EVEN sub-list
 - Subsequent even valued Node will be appended to the tail of EVEN sub-list

 - First odd valued Node will be referenced by head of ODD sub-list
 - Subsequent odd valued Node will be appended to the tail of ODD sub-list
 
2. After the loop, append the EVEN sub-list to the tail of ODD sub-list.
'''
#--------------------------------------------------#
def even_after_odd(head):
    
    if head is None:
        return head
    
    # Helper references
    ''' `even_head` and `even_tail` represents the starting and current ending of the "EVEN" sub-list '''
    even_head = None                    
    even_tail = None
    
    ''' `odd_head` and `odd_tail` represents the starting and current ending of the "ODD" sub-list '''
    odd_head = None
    odd_tail = None
    
    current = head                  # <-- "current" represents the current Node. 
    
    # Loop untill there are Nodes available in the LinkedList
    while current:                  # <-- "current" will be updated at the end of each iteration
        
        next_node = current.next    # <-- "next_node" represents the next Node w.r.t. the current Node
        
        if current.data % 2 == 0:   # <-- current Node is even
            
            # Below 
            if even_head is None:   # <-- Make the current Node as the starting Node of EVEN sub-list
                even_head = current     # `even_head` will now point where `current` is already pointing
                even_tail = even_head     
            else:                   # <-- Append the current even node to the tail of EVEN sub-list 
                even_tail.next = current
                even_tail = even_tail.next
        else:
            if odd_head is None:    # <-- Make the current Node as the starting Node of ODD sub-list
                odd_head = current
                odd_tail = odd_head
            else:                   # <-- Append the current odd node to the tail of ODD sub-list 
                odd_tail.next = current
                odd_tail = odd_tail.next
        current.next = None
        current = next_node         # <-- Update "head" Node, for next iteration
    
    if odd_head is None:            # <-- Special case, when there are no odd Nodes 
        return even_head

    odd_tail.next = even_head       # <-- Append the EVEN sub-list to the tail of ODD sub-list
    
    return odd_head