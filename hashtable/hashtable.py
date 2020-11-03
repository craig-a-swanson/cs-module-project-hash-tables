class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.table = [None] * capacity
        self.node_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.node_count/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        pass


    def djb2(self, key):
        """
        The simple C function starts with the hash variable set to the number 5381.
        It then iterates the given array of characters str and performs the following operations for each character:
        Multiply the hash variable by 33.
        Add the ASCII value of the current character to it.
        After iterating through the whole array, it returns the value held by hash.
        """
        hash_init = 5381

        for character in key:
            hash_init = hash_init * 33 + ord(character)
        
        return hash_init


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Go to the index of the array.
        Search through the linked list if present.
        If the key exists, replace the value;
        Else add a new node to the linked list.
        """
        table_index = self.hash_index(key)
        new_node = HashTableEntry(key, value)

        if self.table[table_index] is None:
            self.table[table_index] = new_node
            self.node_count += 1
        else:
            head = self.table[table_index]
            cur_node = head
            while cur_node is not None:
                if cur_node.key == key:
                    cur_node.value = value
                    return True
                else:
                    cur_node = cur_node.next
            
            new_node.next = head
            head = new_node
            self.table[table_index] = head
            self.node_count += 1

    def delete(self, key):
        """
        Go to the index of the array.
        Search through the linked list for the matching key.
        Delete that node and return the value.
        """
        # Your code here
        table_index = self.hash_index(key)

        if self.table[table_index] is None:
            return None
        
        head = self.table[table_index]
        cur_node = head

        # case where node to delete is the head
        if cur_node.key == key:
            head = cur_node.next
            self.table[table_index] = head
            self.node_count -= 1
            return head
        
        prev_node = cur_node
        cur_node = cur_node.next

        while cur_node is not None:
            if cur_node.key == key:
                prev_node.next = cur_node.next
                self.node_count -= 1
                return cur_node.value
            else:
                prev_node = cur_node
                cur_node = cur_node.next


    def get(self, key):
        """
        Go to the index of the array.
        Search through the linked list for the matching key.
        If the key exists, return the value, else None.
        """
        # Your code here
        table_index = self.hash_index(key)

        if self.table[table_index] is None:
            return None
        
        head = self.table[table_index]
        cur_node = head
        while cur_node is not None:
            # print(f'searching for {key}')
            if cur_node.key == key:
                # print(f'for index {table_index} returning {cur_node.value}')
                return cur_node.value
            else:
                cur_node = cur_node.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # make a new array (not a whole new table)
        # loop over your existing (old) storage
        # if the array index is not None, iterate through linked list there
        # for each node you find, call put()
        table_copy = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for element in table_copy:
            if element is not None:
                cur_node = element
                while cur_node is not None:
                    self.put(cur_node.key, cur_node.value)
                    cur_node = cur_node.next
        
        table_copy = None


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
