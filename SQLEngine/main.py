import sqlparse
from collections import *
from functools import reduce
import sys
from table import *
# if __name__==__main__:
# class Operations(t1,t2):
# 	def __init__(self,t1,t2):
def aand(tc):
		tk=[]
		for row in tc[0]:
			if row in tc[1]:
				tk.append(row)
		return tk
def oor(tc):
		tc=[]
		for i in range(2):
			for row in tc[i]:
				if row not in tc:
					tc.append(row)
		return tc
def get_rows(table,ch,cond):
		cols=cond.split(ch)
		col1=cols[0].strip()
		col2=cols[1].strip()
		p1=table.columns.index(col1)
		p2=table.columns.index(col2)
		rows=[]
		if ch=='=':
			ch='=='
		for row in table.data:
			if eval(str(row[p1])+ch+str(row[p2])):
				rows.append(row)
		return rows
def condition(table,where,fargs):
	where=str(where)
	wlist=where.split(' ')
	# print(wlist)
	try:
		i=wlist.index('WHERE')
		wlist[i]=wlist[i].lower()
	except:
		pass


	if 'AND' or 'and' in wlist:
		try:
			i=wlist.index('AND')
			wlist[i]=wlist[i].lower()
			pwhere=" ".join(wlist)
		except:
			pass

		conds=' '.join(pwhere.split('where')).split('and')
		print(conds)
		tcond_row=[]
		for cond in conds:
			if '<' in cond:
				tcond_row.append(get_rows(table,'<',cond))
			if '>' in cond:
				tcond_row.append(get_rows(table,'>',cond))
			if '<>' in cond:
				tcond_row.append(get_rows(table,'<>',cond))
			if '>=' in cond:
				tcond_row.append(get_rows(table,'>=',cond))
			if '=' in cond:
				tcond_row.append(get_rows(table,'=',cond))
			if '<=' in cond:
				tcond_row.append(get_rows(table,'<=',cond))
		print(tcond_row)
		print(aand(tcond_row))
	# # if 'OR' or 'or' in where.split(' '):

	# 	try:
	# 	i=wlist.index('WHERE')
	# 	wlist[i]=wlist[i].upper()
	# 	oor()
# 	def equal
def keval(query):
	parse = lambda y: list(filter(lambda x: not x.is_whitespace, sqlparse.parse(y)[0].tokens))
	query = parse(query)
	print(query)
	if 'where' in str(query[-1]):
		_,sargs,_,fargs,where=query
		print(str(where))
	else:
		_,sargs,_,fargs,p=query
	tables_query=list(map(lambda x: x.split()[0],str(fargs).split(',')))
	print(tables_query)
	store=parse_meta()
	new_table=store[tables_query[0]]
	for k in range(len(tables_query)-1):
		new_table=cross_product(new_table,store[tables_query[k+1]])
	# print(new_table)
	condition(new_table,where,fargs)

	# print(new_table)
sql_query = sys.argv[1]
# print(sql_query)
keval(sql_query)
