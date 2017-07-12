def gcd(n,m):
    print(n,m)
    if m < n:
        (m,n)=(n,m)
    if (m%n) == 0:
        return n
    else:
        return (gcd(n,(m%n)))

print("This program will print GCD of two numbers")
print(gcd(16,4))