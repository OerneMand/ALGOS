from algs4.stdlib.stdrandom import uniform,shuffle
from algs4.stdlib.stdstats import mean,stddev
#from algs4.stdlib.stdio import eprint
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class RandomQueue:
    class Node:
        def __init__(self,item):
            self.item = item
    
    def __init__(self):
        self._n = 0
        self._in = list
        self._out = list

    def isEmpty(self):
        if self._n == 0:
            return True
        else:
            return False

    def size(self):
        return self._n

    def __len__(self):
        None

    def enqueue(self,item):
        if self._n == 0:
            self._in = [None]
            self._in[0] = item
        elif self._n == len(self._in):
            self._out = [None]*2*self._n
            for i in range(self._n):
                self._out[i] = self._in[i]
            self._in = self._out
            self._in[self._n] = item
        else:
            self._in[self._n] = item
        self._n += 1
        return

    def sample(self):
        m = uniform(self._n)
        return self._in[m]

    def dequeue(self):
        m = uniform(self._n)
        if m == self._n-1:
            item = self._in[m]
            self._in[m] = None
            self._n -= 1
        else:
            item = self._in[m]
            self._in[m] = self._in[self._n - 1]
            self._n -= 1
        if self._n == len(self._in) / 2:
            self._out = [None]*self._n
            for i in range(self._n):
                self._out[i] = self._in[i]
            self._in = self._out
        return item
        

    def __iter__(self):
        """
        Returns an iterator that iterates over the items in this RandomQueue in random order.

        :returns: an iterator that iterates over the items in this RandomQueue in random order.
        """
        # create the right mine
        items = self._in[:self._n]
        shuffle(items)
        for x in items:
            yield x

# This  "main method" tests your implementation. Do not change it.
if __name__ == '__main__':
    Q = RandomQueue()
    # build a randomQueue with 1,2,..,6
    for i in range(1,7):
        Q.enqueue(i)
        
    # print 30 die rolls
    eprint( ' '.join([str(Q.sample()) for i in range(30) ] ) )

    # Let's be more serious: do they really behave like die rolls?
    rolls = [ Q.sample() for i in range(1000) ]
    eprint("Mean (should be around 3.5): {:5.4f}".format(mean(rolls)))
    eprint("Standard deviation (should be around 1.7): {:5.4f}".format(stddev(rolls)))

    # removing 3 random values
    eprint( "Removing {}".format(' '.join( [str(Q.dequeue()) for i in range(3) ] ) ) )
    
    #Add 7,8,9
    for i in range(7,10):
        Q.enqueue(i); 
    # Empty the queue in random order
    while not Q.isEmpty():
        eprint(Q.dequeue(),end=' ');
    eprint()

    # Let s look at the iterator. First, we make a queue of colours:
    C= RandomQueue()
    C.enqueue("red"); C.enqueue("blue"); C.enqueue("green"); C.enqueue("yellow"); 

    I = iter(C)
    J = iter(C)

    eprint("Two colours from first shuffle: {} {}".format(next(I),next(I)))
    
    eprint("Entire second shuffle: {}".format(' '.join([i for i in J])));

    eprint("Remaining two colours from first shuffle: {} {}".format(next(I),next(I)))

    # for i in range(3):
    #     eprint(list( Q))
    # for i in range(6):
    #     eprint(Q.dequeue())
