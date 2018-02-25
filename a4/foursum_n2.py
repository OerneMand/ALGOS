import sys
from algs4.fundamentals import binary_search

N = int(sys.stdin.readline())
vals = map(int, sys.stdin.readlines())
vals_list = [val for val in vals]

class FourSumFunction:
	def __init__(self,array):
		self._input = array
		self._n = len(array)
		self._m = int()
		self._pairs = list()
		self._vals = list()
	
	def get_pairs(self):
		for i in range(0,self._n-1):
			for j in range(i+1,self._n):
				pair = self._input[i] + self._input[j]
				self._pairs.append([pair,i,j])
		self._m = len(self._pairs)
		return
	
	def sort_list(self):
		self._pairs = sorted(self._pairs,key=lambda x: x[0])
		self._vals = [self._pairs[i][0] for i in range(self._m)]
		return
	
	def check_sum(self):
		for i in range(0,self._m-1):
			if binary_search.index_of(self._vals,-self._vals[i]) > i:
				j = binary_search.index_of(self._vals,-self._vals[i])
				if self.check_duplicate(i,j):
					return True
		return False
	
	def check_duplicate(self,p,q):
		if(self._pairs[p][1] != self._pairs[q][1] and self._pairs[p][1] != self._pairs[q][2]
			and self._pairs[p][2] != self._pairs[q][1] and self._pairs[p][2] != self._pairs[q][2]):
			return True
		else:
			return False
	
	def cal(self):
		self.get_pairs()
		self.sort_list()
		return self.check_sum()

fs = FourSumFunction(vals_list)
print(fs.cal())
