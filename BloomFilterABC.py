from abc import ABC, abstractmethod
class BloomFilterABC(ABC):

    def __init__(self, capacity : int, item_ty, filter_ty : str):
        """
        Abstract base class for Bloom Filters
        :param capacity: The capacity of the filter
        :param item_ty: The python type of elements being hashed to
        the filter (e.g. str, int, etc...)
        :param filter_ty: Name for the implementing class
        """
        self.num_added = 0
        self.num_filled = 0
        self.capacity = capacity
        self.filter_ty = filter_ty
        self.item_ty = item_ty


    @abstractmethod
    def __contains__(self, item):
        #TODO
        pass

    @abstractmethod
    def _add(self, item):
        """
        adds the item to the bloom filter and returns true if
        hash of the item is not already in the filter
        :param item:  item to add
        :return: true iff hash of item is not in this filter
        """
        pass

    def add(self, item):
        temp = item in self
        added = self._add(item)
        assert item in self
        if added:
            assert not temp
            self.num_added+=1
            self.num_filled+=1

    def add_all(self, *items):
        for item in items:
            self.add(item)

    @abstractmethod
    def _hash(self, item):
        pass

    def hash(self, item):
        assert isinstance(item, self.item_ty)
        return self._hash(item) % self.capacity

    def __str__(self):
        s = 'bloom filter of type : '+ self.filter_ty
        s+= ', capacity : ' +str(self.capacity)
        s+= ', num filled : ' + str(self.num_filled)
        s+= ', num added : '+ str(self.num_added)
        return s

    def get_capacity(self):
        return self.capacity

    def get_num_filled(self):
        return self.num_filled

    def get_num_added(self):
        return self.num_added

