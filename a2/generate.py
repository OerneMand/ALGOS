import random
import math

text_file = open('test.txt', 'w')

n = 2000
m = -int(6.90776 / ( math.log(n-1) - math.log(n) ))
#m = int(n*(n-1)*0.5)

text_file.write('{} \n'.format(n))

for i in range(m):
    a = random.randint(0,n-1)
    b = random.randint(0,n-1)
    text_file.write('{} {} \n'.format(a,b))
