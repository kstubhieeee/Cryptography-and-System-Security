def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def main():
    P = 14
    print("The value of P:", P)
    
    G = 22
    print("The value of G:", G)
    
    a = 6
    print("The private key a for Kaustubh:", a)
    
    x = power(G, a, P)
    
    b = 5
    print("The private key b for Karan:", b)
    
    y = power(G, b, P)
    
    ka = power(y, a, P)
    kb = power(x, b, P)
    
    print("Secret key for Kaustubh is:", ka)
    print("Secret key for Karan is:", kb)

if __name__ == "__main__":
    main()