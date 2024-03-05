from list_mapping import ListMapping


# A mapping using a hashtable and dynamic reallocation of new buckets when needed
class HashMapping:
    def __init__(self, size=2):
        # Number of buckets
        self._size = size
        # Create a list of empty ListMappings
        self._buckets = [ListMapping()] * self._size
        # Keep track of the number of elements currently in the mapping
        self._length = 0

    # Implement the assignment self[key] = value
    def __setitem__(self, key, value):
        # Use the helper function to find the bucket
        m = self._bucket(key)
        if key not in m:
            self._length += 1
        # Use the ListMapping contained in the bucket to find the key
        m[key] = value
            
        # Check if we need more buckets.
        if self._length > self._size:
            self._double()

    # Implement the evaluation of self[key]
    def __getitem__(self, key):
        # Use the helper function to find the bucket
        m = self._bucket(key)
        # Use the ListMapping contained in the bucket to find the key
        return m[key]

    # Identify the right bucket
    def _bucket(self, key):
        return self._buckets[hash(key) % self._size]

    # Rehashing
    def _double(self):
        print("I need more space!")
        # Save a reference to the old buckets.
        old_buckets = self._buckets
        # Double the size.
        self._size *= 2
        # Create new buckets
        self._buckets = [ListMapping()] * self._size
        # Add in all the old entries.
        for bucket in old_buckets:
            # For each entry in the old buckets
            for key, value in bucket.items():
                # Identify the new bucket.
                m = self._bucket(key)
                # Add it to the bucket
                m[key] = value

    def __len__(self):
        return self._length


if __name__ == '__main__':
    my_mapping = HashMapping()
    my_mapping[42] = 'Some text'
    my_mapping[42] = 'Bla'
    my_mapping[(2, 5)] = 'Something completely different'
    print(my_mapping[42])
    print(my_mapping[(2, 5)])
    my_mapping['Hello'] = 'Something else'
    print(my_mapping['Hello'])
    print(my_mapping[42])
