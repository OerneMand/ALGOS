import sys
from algs4.stdlib import stdio
from MyUnionFind_fast import UF



class UFW():
    if __name__ == '__main__':
        if len(sys.argv) > 1:
            try:
                sys.stdin = open(sys.argv[1])
            except IOError:
                print("File not found, using standard input instead")
        n = stdio.readInt()
        uf = UF(n)

        giant_time = 0
        giant_bool = True
        iso_time = 0
        iso_bool = True
        con_time = 0
        con_bool = True
        i = 0

        while not stdio.isEmpty():
            i += 1
            p = stdio.readInt()
            q = stdio.readInt()
            if uf.connected(p, q):
                continue
            uf.union(p,q)

            if uf.max_component() >= n/2 and giant_bool:
                giant_bool = False
                giant_time = i
            
            if uf.max_component() == n and con_bool:
                con_bool = False
                con_time = i
            
            if uf.isolated() and iso_bool:
                iso_bool = False
                iso_time = i
        print(n, iso_time, giant_time, con_time)