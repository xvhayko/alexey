def largest_power(n):
    if n==1: return (0,-1)
    if n<=4: return (1,-1)
    r,i=[],2
    while i*i<n:
        j=2
        while i**j<n:
            r.append(i**j)
            j+=1
        i+=1
    m=max(r)
    return (m,len([e for e in r if e==m]))