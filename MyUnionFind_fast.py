class UF:
    """
    This is an implementation of the union-find data structure - see module documentation for
    more info.
    This implementation uses weighted quick union by rank with path compression by
    halving. Initializing a data structure with n sites takes linear time. Afterwards,
    the union, find, and connected operations take logarithmic time (in the worst case)
    and the count operation takes constant time. Moreover, the amortized time per union,
    find, and connected operation has inverse Ackermann complexity.
    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n):
        """
        Initializes an empty union-find data structure with n sites,
        0 through n-1. Each site is initially in its own component.
        :param n: the number of sites
        """
        self._count = n
        self._parent = list(range(n))
        self._rank = [0]*n

        """
        Added a 'binary' list to keep track of sites that have been
        unioned, as well as an integer that counts the number of
        isolated sites. Also a list to keep track of the roots'
        tree sizes, as well as an integer that holds the maximum
        tree size (maximum component in the graph)
        """
        self._nodes = [1]*n
        self._iso = n
        self._size = [1]*n
        self._max = 0

    def _validate(self, p):
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))

    def union(self, p, q):
        """
        Merges the component containing site p with the
        component containing site q.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        
        #if the sites were isolated make them un-isolated
        if self._nodes[p] == 1:
            self._nodes[p] = 0
            self._iso -= 1
        if self._nodes[q] == 1:
            self._nodes[q] = 0
            self._iso -= 1

        # make root of smaller rank point to root of larger rank
        if self._rank[root_p] < self._rank[root_q]:
            self._parent[root_p] = root_q
            #add the small root size to the big root size
            self._size[root_q] += self._size[root_p]
            #check if the big root size is now the biggest
            if self._size[root_q] > self._max:
                self._max = self._size[root_q]
        elif self._rank[root_p] > self._rank[root_q]:
            self._parent[root_q] = root_p
            self._size[root_p] += self._size[root_q]
            if self._size[root_p] > self._max:
                self._max = self._size[root_p]
        else:
            self._parent[root_q] = root_p
            self._size[root_p] += self._size[root_q]
            if self._size[root_p] > self._max:
                self._max = self._size[root_p]
            self._rank[root_p] += 1

        self._count -= 1

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.
        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]] # path compression by halving
            p = self._parent[p]
        return p

    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.
        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)

    def count(self):
        return self._count

    def max_component(self):
        return self._max

    def isolated(self):
        #returns False if there are isolated sites, otherwise True
        if self._iso > 0:
            return False
        else:
            return True
