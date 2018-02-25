import sys

sys.stdin = open(sys.argv[1])
N = int(sys.stdin.readline())
vals = map(int, sys.stdin.readlines())
vals_list = [val for val in vals]

def four_sum_func(nums):
	N = len(nums)
	count = 0
	total = N*(N-1)*(N-2)*(N-3)
	for i in range(0,N): # i goes through {0,...,N-1}
		one = nums[i]
		for j in range(1,N):
			two = nums[j]
			for k in range(2,N):
				three = nums[k]
				for l in range(3,N):
					four = nums[l]
					four_sum = one+two+three+four
					count += 1
					if count % 2500000 == 0:
						print("{} percent done.".format(100*count/total))
					if four_sum == 0:
						print("Done.")
						return True
	print("Done.")
	return False

print(four_sum_func(vals_list))