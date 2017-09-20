import random
import sys
import math
class Generator:
    def __init__(self,**kwargs):  
        self.nattrs = kwargs.get('nattrs')          
        self.duplication_rate=kwargs.get('duplication_rate')
        self.file=kwargs.get('file')
        self.file_size=0
        self.file_pointer=0
        self.ntuples=0


    def create_tuples(self,k):  
        tuples = []
        for i in range(k):
            _tuple = ()
            for j in range(self.nattrs):
                _tuple = _tuple+(random.randint(1,1000),)
            tuples.append(_tuple)
        return tuples
    
    def file_write(self,tuples):
        with open(self.file,'ab') as fp:
            for _tuple in tuples:
                s=''
                for k in _tuple:
                    s=str(k)+','+s
                fp.write(s+'\n')

    def limit_size(self):
        with open(self.file,'rb') as fp:
            fp.seek(self.file_pointer)
            for line in fp:
                self.file_size+=len(line.encode('utf-8'))
                if self.file_size>=pow(10,9):
                    return False
            self.file_pointer=fp.tell()
        return True

    def random_generate(self,prev_tuples,k):
        count=1
        tuples=[]
        while count <= k:
            i = random.randint(0,len(prev_tuples)-1)
            tuples.append(prev_tuples[i])
            count+=1
        return tuples

    def generate(self):
        tupss = self.create_tuples(100)
        self.file_write(tupss)
        self.ntuples=100
        count=1
        while self.limit_size():
            tupss = self.random_generate(tupss,self.duplication_rate)+\
            self.create_tuples(100-self.duplication_rate)
            # tuples.append(tupss)
            self.file_write(tupss)
            self.ntuples+=100
            if count%500==0:
                print count
            count+=1
        print "Total number of Records"
        print self.ntuples
g=Generator(nattrs = 3,duplication_rate = 10,file = 'file.txt')
g.generate()
    