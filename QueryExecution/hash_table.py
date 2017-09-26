from index_structure import IndexStructure
from bucket import Bucket
from iterator import Iterator
import hashlib
from functools import *


class HashTable(IndexStructure):
    def __init__(self, **kwargs):
        #self.record = kwargs.get('record')
        self.kwargs = kwargs
        self.mapping = {}
        self.bucket_num = 1
        self.bucket = Bucket(**self.kwargs)

    def _hash(self, record):
        hash_value = sum(record)%10
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
            self.bucket.add(record,self.bucket_num)
            self.bucket_num += 1
        else:
            bucket_num = self.mapping[hv]
            self.bucket.add(record,bucket_num)
       

    def __contains__(self, record):
        hv = self._hash(record)
        if hv not in self.mapping:
            return False
        else:
            bucket_num = self.mapping[hv]
            return self.bucket.check(record,bucket_num)
        
    


if __name__ == '__main__':
    kb = 2**10
    mb = kb**2
    gb = kb**3
    iterator = Iterator(storage='file.txt', block_size=300)

    IS = HashTable(Maxfile_size=0.5*mb)
    for record in iterator:
        if record not in IS:
            IS.add(record)
