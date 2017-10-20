import sqlparse
from collections import *
from functools import reduce

class Table:
    def __init__(self, name, columns,data):
        self.name=name
        self.columns=columns
        self.data=data
        
    def __str__(self):
        output=''
        output+=reduce(lambda x,y: x+','+y,self.columns)
        output+='\n'
        for row in self.data:
            srow=map(str,row)
            output+=','.join(srow)  
            output+='\n'
        return(output)
# class Condition:
#     def __init__(q):
#         pass
#     def aand(sargs,table1,table2):
#         for 

#     def oor(cols,table1,table2):
#         for col in cols:
#             if 


# def Select(table1.columns,table2.columns,rows1,rows2):


# def evaluate(w_args):



def parse_meta():
    result = {}
    def parse_table(name):
        with open('files/'+name+'.csv','r') as fp:
            data=fp.read().splitlines()
            rows=[]
            for line in data:
                row=list(map(int,line.split(',')))
                rows.append(row)
            return rows
    with open('files/metadata.txt','r') as fp:
        data=fp.read().splitlines()
        starts, ends = [], []
        for i, line in enumerate(data):
            if line=='<begin_table>':
                starts.append(i)
            if line=='<end_table>':
                ends.append(i)
        for i in range(len(starts)):
            tinfo=data[starts[i]+1:ends[i]]
            name, *headers = tinfo
            tdata = parse_table(name)
            headers=list(map(lambda x: name+'.'+x,headers))
            print(headers)
            result[name] = Table(name,headers, tdata)
    return result
def cross_product(table1,table2):
    cols=table1.columns+table2.columns
    data=[]
    for row1 in table1.data:
        for row2 in table2.data:
            data.append(row1+row2)
    return Table('',cols,data)