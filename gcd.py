def gcd(n,m):
    print(n,m)
    if m < n:
        (m,n)=(n,m)

    if ((m%n)==0):
        return n
    else:
        diff = m - n
    
    # diff > n? Possible!
    return ( gcd( max(n,diff),min(n,diff) ) )

print("This program will print GCD of two numbers")
print(gcd(16,8))