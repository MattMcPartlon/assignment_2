"""
Implement a "MultiBloomFilter", which extends the BloomFilterABC class.

This class will consist of k bloom filters, all with the same capacity,
and will answer membership queries by searching for the element in each
of the k bloom filters
We will add an element by adding it to each fo the k Bloom Filters aas well.

In addition to the parameters of the BloomFilterABC class, you must also
support a parameter 'hash_fs' denoting the hash function to use for each
of the k filters.

You can add any parameters you'd like to the __init__ funciton
and any helper methods you'd like, but you must extend the abstract
base class.

"""
class MultiBloomFilter(BloomFilterABC):
    #TODO
    def __init__(self):
        pass

    """
    Override these methods to return the
    sum of the capacities, num_filled, and num_added
    over each of the constituent Bloom Filters.
    """
    def get_capacity(self) :
        #TODO
        pass

    def get_num_filled(self) :
        #TODO
        pass

    def get_num_added(self) :
        #TODO
        pass