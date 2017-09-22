import random
import sys
import math
class Generator:
    def __init__(self, **kwargs):  
        self.nattrs = kwargs.get('n_attrs')          
        self.duplication_rate = kwargs.get('duplication_rate')
        self.file = kwargs.get('file_name')
        self.fp = open(self.file,'w')
        self.max_size = kwargs.get('max_size')
        self.file_size = 0
        self.file_pointer = 0
        self.ntuples = 0
    
    def create_tuples(self, k):  
        tuples = []
        for i in range(k):
            _tuple = ()
            for j in range(self.nattrs):
                _tuple = _tuple+(random.randint(1,1000),)
            tuples.append(_tuple)
        return tuples
    
    def file_write(self, tuples):
        for _tuple in tuples:
            _tuple = list(map(str, _tuple))
            outstring = ','.join(_tuple) + '\n'
            self.fp.write(outstring)
            self.file_size += len(outstring.encode('utf-8'))

    def random_generate(self, prev_tuples, k):
        count = 1
        tuples = []
        while count <= k:
            i = random.randint(0,len(prev_tuples)-1)
            tuples.append(prev_tuples[i])
            count += 1
        return tuples

    def generate(self):
        tupss = self.create_tuples(100)
        self.file_write(tupss)
        self.ntuples = 100
        count = 1
        while self.file_size < self.max_size:
            tupss = self.random_generate(tupss,self.duplication_rate)+\
            self.create_tuples(100-self.duplication_rate)
            # tuples.append(tupss)
            self.file_write(tupss)
            self.ntuples += 100
            if count%500==0:
                print(count)
            count += 1
        print("Total number of Records")
        print(self.ntuples)

if __name__ == '__main__':
    kb = 2**10
    mb = kb**2
    gb = kb**3
    params = {
            "duplication_rate" : 10,
            "n_attrs": 3,
            "max_size": 5*mb,
            "file_name": 'file.txt'
    }
    g = Generator(**params)
    g.generate()
    
