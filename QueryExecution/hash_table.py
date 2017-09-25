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
        self.bucket_num = 1

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
        if hv not in self.mapping.keys():
            self.mapping[hv] = self.bucket_num
            bucket.add(record,self.bucket_num)
            self.bucket_num += 1
        else:
            bucket_num = self.mapping[hv]
            bucket.add(record,bucket_num)
       

    def __contains__(self, record):
        hv = self._hash(record)
        if hv not in self.mapping:
            return False
        else:
            bucket_num = self.mapping[hv]
            return bucket.check(record,bucket_num)
        
    


if __name__ == '__main__':
    iterator = Iterator(file_name)
    #IS = HashTable(..)
    IS = HashTable(..)
    for record in iterator:
        if record not in IS:
            IS.add(record)
