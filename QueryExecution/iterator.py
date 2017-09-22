from utils import line2record, record2line

class Iterator:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.fp = open(kwargs.get("storage"), "r")
        self.block_size = kwargs.get("block_size")
        self.load()

    def load(self):
        self.i = 0
        self.size = 0
        self.records = []
        self.n = 0
        for line in self.fp:
            size, record = line2record(line)
            self.records.append(record)
            self.size += size
            self.n += 1
            if self.size >= self.block_size:
                return True
        else:
            return False

    def __iter__(self):
        """ Open """
        return self
        

    def __next__(self):
        """ GetNext 
        If no more elements raise StopIteration
        """
        if self.i < self.n:
            i = self.i
            self.i += 1
            return self.records[i]
        else:
            if self.load():
                return self.__next__()
            else:
                raise StopIteration()




if __name__ == '__main__':
    x = Iterator(storage='file.txt', block_size=300)
    for record in x:
        print(record2line(record), end='')

