def gcd(n,m):
    print(n,m)
    for i in range(1,min(n,m)+1):
        if ((m%i) == 0) and ((n%i) == 0):
            mrcf=i
    
    print(mrcf)

print("This program will print GCD of two numbers")
gcd(16,4)