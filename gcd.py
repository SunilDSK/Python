def gcd(n,m):
    print(n,m)
    cf = []
    for i in range(1,min(n,m)+1):
        if ((m%i) == 0) and ((n%i) == 0):
            cf.append(i)
    
    print(cf[-1])

print("This program will print GCD of two numbers")
gcd(16,8)