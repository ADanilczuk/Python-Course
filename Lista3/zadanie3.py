slownik = {0 : {(0,0): 0} }

def sudan(n,x,y):
    if n == 0:
        return x + y
    if y == 0 and x >= 0:
        slownik[n,x,0] = x
        return x
    else:
        if not (n,x,y-1) in slownik: 
            a = sudan(n,x,y-1)
            slownik[(n,x,y-1)] = a
        if not (n-1,a,a+y) in slownik:
            c = sudan(n-1,a,a+y)
            slownik[(n-1,a,a+y)] = c
            return c
        else:
            return slownik((n-1,a,a+y))

"""print(sudan(1,5,10)) """

print(sudan(2,5,1))






