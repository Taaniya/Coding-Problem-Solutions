#! /bin/usr/bin/env python
count = 0
def editD(a, b, m, n, ed=None):
    """
    Paremeters:
    ---------------------
    a : string 1
    b : string 2
    m : lentgh of string 1
    n : length of string 2
    ed : array in mempry to store results of sub prooblems
    
    
    eg.
    >> editD("cut","cutter",3,6)
    >> 3
    
    >> editD("sunday","saturday",6,8)
    >> 3
    """
    global count
    
    if ed is None:
        ed = [[None for j in range(n)] for i in range(m)]
        

    if m == 0 :
        return n

    elif n == 0 :
        return m

    if ed[m-1][n-1] is not None:
        return ed[m-1][n-1]
    
    elif a[m-1] == b[n-1]:
        ed[m-1][n-1] = editD(a, b, m-1, n-1)

    else:
        ed[m-1][n-1] =  1 + min(editD(a, b, m, n-1, ed), editD(a, b, m-1, n, ed), editD(a,b , m-1 ,n-1, ed))
        count += 1
        print(ed)
    return ed[m-1][n-1]
