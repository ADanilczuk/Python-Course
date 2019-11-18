def reszta(n):   
    r20= n//20
    if (r20>0): 
        n=n-(20*r20)
    r10=n//10
    if (r10>0): 
        n=n-(10*r10)
    r5=n//5
    if (r5>0):
        n=n-(5*r5)
    r2=n//2
    if (r2>0):
        n=n-(2*r2)
    return [r20,r10,r5,r2,n]


print(reszta(68))