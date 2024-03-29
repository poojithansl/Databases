
import os
from collections import defaultdict
from utils import line2record, record2line
from iterator import Iterator
class Bucket:
    
    def __init__(self, **kwargs):
        self.max_filesize = kwargs.get("Maxfile_size")
        self.bucket_files = defaultdict(list)
        self.file_num = 1
        self.file_size = defaultdict(int)
        # self.file_names = []


    def write_to_file(self, record, file_num):
        if not os.path.exists('Files'):
            os.makedirs('Files')
        if self.file_size[file_num] <= self.max_filesize:
            with open('Files/'+str(file_num)+'.txt', 'a') as fp:
                record = record2line(record)
                fp.write(record)
                self.file_size[file_num] += len(record.encode('utf-8'))
        else:
            self.file_num = self.file_num+1
            self.bucket_files[bucket_num].append(self.file_num)
            file_num = self.file_num
            
            with open('Files/'+str(file_num)+'.txt','a') as fp:
                record = record2line(record)
                self.file_size[file_num] += len(record.encode('utf-8'))
                fp.write(record)
            self.file_num += 1


    def add(self, record, bucket_num):
        if bucket_num not in self.bucket_files:
            self.bucket_files[bucket_num].append(self.file_num)
            self.write_to_file(record,self.file_num)
            self.file_num += 1
        else:
            file_num = self.bucket_files[bucket_num][-1]
            self.write_to_file(record,file_num)
                

    def check(self, record, bucket_num):
        file_list = self.bucket_files[bucket_num] 
        record = record2line(record)
        for file_num in file_list:
            fp = open('Files/'+str(file_num)+'.txt','r')
            lines = fp.readlines()
            if record in lines:
                return True
        return False


if __name__ == '__main__':
    kb = 2**10
    mb = kb**2
    gb = kb**3
    bucky = Bucket(Maxfile_size =  * mb)
    x = Iterator(storage='file.txt', block_size=300)
    for i,record in enumerate(x):
        bucky.add(record,i%10)

