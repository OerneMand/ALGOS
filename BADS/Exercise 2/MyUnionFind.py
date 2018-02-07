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
        self._size = [1]*n
        self.max_component_size = 0

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

        # make root of smaller rank point to root of larger rank
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p
            
        self._parent[small] = large
        self._size[large] += self._size[small]
      
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
        '''
        Number of components
        '''
        return self._count

    def is_connected(self):
        if count == 1:
            return True