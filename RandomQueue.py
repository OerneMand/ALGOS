class RandomQueue:
    class Node:
        def __init__(self,item,next):
            self.item = item
            self.next = next
    
    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0
    
    def empty(self):
        if self._n == 0:
            return True
        else:
            return False

    def size(self):
        return self._n
    
    def insert(self,item,k):
        if k > self._n+1:
            return "Out of range."
        elif self.empty():
            self._last = self.Node(item,None)
            self._first = self._last
            self._n += 1
        elif k == 1:
            oldfirst = self._first
            self._first = self.Node(item,oldfirst)
            self._n += 1
        else:
            prev = self.iterate(k-1)
            current = self.Node(item,prev.next)
            prev.next = current
            self._n += 1

    def sample(self,k):
        if k > self._n:
            return
        current = self.iterate(k)
        return current.item

    def delete(self,k):
        if k > self._n:
            return
        else:
            prev = self.iterate(k-1)
            current = self.iterate(k)
            prev.next = current.next
            current.item = None
            self._n -= 1
            return
    
    def iterate(self,k):
        if k > self._n:
            return
        current = self._first
        for i in range(k-1):
            current = current.next
        return current

ciao = RandomQueue()
ciao.insert('miaw',1)
ciao.insert('moo',2)
ciao.insert('vuf',3)
ciao.insert('meh',4)
ciao.insert('quack',5)
ciao.delete(3)
print(ciao.size())
