class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    '''Input a string that has to be stored in the table.'''
    def store(self, string):
        hv = self.calculate_hash_value(string)   # generate the hash value
        
        if hv != -1:                             # if the string is a new one
            if self.table[hv] != None:           # if the bucket is non-empty 
                self.table[hv].append(string)    # append the string in the list at that bucket
            else:
                self.table[hv] = [string]        # store the string in a new list at that bucket
                
                
    '''Return the hash value if the string is already in the table. Return -1 otherwise.'''
    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        
        # Check collision, and confirm the availability of the given string
        # There might be a case when two strings can generate same hash value.
        # However, one string is present, and other one is not.
        if self.table[hv] != None:
            if string in self.table[hv]:
                return hv
        
        return -1                                # otherwise

    '''Helper function to calulate a hash value from a string.'''
    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value

# TESTING Setup
hash_table = HashTable()

# Test calculate_hash_value
print (hash_table.calculate_hash_value('UDACITY'))    # Should be 8568

# Test lookup edge case
print (hash_table.lookup('UDACITY'))                  # Should be -1

# Test store
hash_table.store('UDACITY')
print (hash_table.lookup('UDACITY'))                  # Should be 8568

# Test store edge case
hash_table.store('UDACIOUS')
print (hash_table.lookup('UDACIOUS'))                 # Should be 8568