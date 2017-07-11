print("This is a GCD program")

def gcd(m,n):
    fm = []
    for i in range(1,m+1):
        if (m%i) == 0:
            fm.append(i)

    fn = []
    for i in range(1,n+1):
        if (n%i) == 0:
            fn.append(i)
    
    cf = []
    for i in fm:
        if i in fn:
            cf.append(i)
    
    return(cf[-1])

print(gcd(16,8))