from index_structure import IndexStructure
from bucket import Bucket
from iterator import Iterator
import hashlib
from functools import *


class HashTable(IndexStructure):
    def __init__(**kwargs):
        #self.record = kwargs.get('record')
        self.kwargs = kwargs
        self.mapping = {}

    def _hash(self, record):
        hash_value = sum(record)
        return hash_value

    def load(self):
        """ Loads from the serialized output """
        pass

    def save(self):
        """ Serializes and writes out """
        pass

    def add(self, record):
        hv = self._hash(record)
        bucket = self.mapping(hv)
        bucket.add(record)
        pass

    def __contains__(self, record):
        pass
    


if __name__ == '__main__':
    iterator = Iterator(file_name)
    #IS = HashTable(..)
    IS = HashTable(..)
    for record in iterator:
        if record not in IS:
            IS.add(record)
