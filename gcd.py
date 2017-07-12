def gcd(n,m):
    print(n,m)
    i = min(n,m)

    while i > 0:
        if ((n%i)==0) and ((m%i)==0):
            print(i)
            break
        i=i-1

print("This program will print GCD of two numbers")
gcd(16,8)