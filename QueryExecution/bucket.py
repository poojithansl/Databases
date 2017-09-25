
import os
from collections import defaultdict
from utils import line2record, record2line
from iterator import Iterator
class Bucket:
    def __init__(**kwargs):
        self.max_filesize = kwargs.get("Maxfile_size")
        self.bucket_files = defaultdict(list)
        self.file_num = 1
        # self.file_names = []

    def overloads(self,file_num):
        fp = open('Files/'+str(file_num)+'.txt','r')
        file_size = 0
        for line in fp:
            size, _= line2record(line)
            file_size += size
            if file_size > self.max_filesize:
                fp.close()
                return True
        fp.close()
        return False

    def write_to_file(self, record, file_num):
        if not os.path.exists('Files'):
            os.makedirs('Files')
        if overloads(file_num):
            self.file_num = self.file_num+1 
            self.bucket_files[bucket_num].append(self.file_num)
            self.file_num += 1
            file_num = self.file_num
        with open('Files/'+str(file_num)+'.txt', 'a') as fp:
            fp.write(record+'\n')


    def add(self, record, bucket_num):
        if bucket_num not in self.bucket_files:
            self.bucket_files[bucket_num].append(self.file_num)
            self.file_num += 1
        else:
            file_num = self.bucket_files[bucket_num][-1]
            write_to_file(record,file_num)
                

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
    bucky = Bucket(Maxfile_size = )
    x = Iterator(storage='file.txt', block_size=300)
    for record in x:
        bucky.add(record)

