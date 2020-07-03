from BloomFilterABC import BloomFilterABC
class BloomFilter(BloomFilterABC):
    """
    Bloom filter for integers
    """

    def __init__(self, capacity : int, hash_function = None):
        super().__init__(capacity, item_ty = int, filter_ty = "Integer BloomFilter")
        self.hash_function = hash_function

    def _add(self, item):
        #TODO
        pass

    def _hash(self, item):
        """
        Implement a standard hash function to use in the case where
        self.hash_function is None.
        If self.hash_function is not None, use the hash function
        provided on initialization to hash the item.

        :param item: an integer
        :return: hash of the integer.
        """
        #TODO
        pass

    def __contains__(self, item):
        #TODO
        pass


