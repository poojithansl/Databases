import random
import sys
import math
class Generate:
	def __init__(self,n_a,r):	#r- duplication, n_a = number of attributes
		self.n_a = n_a			
		self.r=r
	def create_tuples(self,k):	#create k tuples
		tuples = []
		for i in range(k):
			tup = ()
			for j in range(self.n_a):
				tup = tup+(random.randint(1,1000),)
			tuples.append(tup)
		return tuples
	
	def file_write(self,tu,file):
		with open(file,'ab') as fp:
			for tup in tu:
				s=''
				for k in tup:
					s=str(k)+','+s
				fp.write(s+'\n')

	def limit_size(self,file):
		file_size = 0
		with open(file,'rb') as fp:
			for line in fp:
				file_size += len(line.encode('utf-8'))
				if file_size >= pow(10,9):
					return False
		return True

	def random_generate(self,tu,rd):
		cnt=1
		tuples=[]
		while cnt <= rd:
			i = random.randint(0,len(tu)-1)
			tuples.append(tu[i])
			cnt+=1
		return tuples

	def generate(self,file):
		tupss = self.create_tuples(100)
		self.file_write(tupss,file)
		cnt=1
		while self.limit_size(file):
			tupss = self.random_generate(tupss,self.r)+self.create_tuples(100-self.r)
			# tuples.append(tupss)
			self.file_write(tupss,file)
			if cnt%500==0:
				print cnt
			cnt+=1
g=Generate(3,10)
g.generate('file.txt')