import sys
from algs4.fundamentals import binary_search
import time

N = int(sys.stdin.readline())
vals = map(int, sys.stdin.readlines())
vals_list = [val for val in vals]

def four_sum_func(nums):
	N = len(nums)
	sort_nums = sorted(nums)
	for i in range(0,N):
		for j in range(i+1,N):
			for k in range(j+1,N):
				if binary_search.index_of(sort_nums,-sort_nums[i]-sort_nums[j]-sort_nums[k]) > k:
					return True
	return False

start = time.time()
print(four_sum_func(vals_list))
end = time.time()-start

print("Time: {}".format(end))

