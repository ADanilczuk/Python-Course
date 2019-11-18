def romb(n):
    h=n
    x=' '
    y='#'
    while (h>=0):
        print (h*x+y*(2*(n-h)+1))    
        h=h-1
    h=1
    while (h<=n):
        print (h*x+y*(2*(n-h)+1))    
        h=h+1
    
romb(4)

