import math

def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a

def rsa():
    p = 2
    q = 5
    n = p * q
    totient = (p - 1) * (q - 1)
    
    e = 2
    while e < totient:
        if gcd(e, totient) == 1:
            break
        e += 1
    
    k = 2
    d = (1 + (k * totient)) // e
    
    msg = int(input("Enter Message data: "))
    
    c = pow(msg, e, n)
    
    m = pow(c, d, n)
    
    print("\nMessage data:", msg)
    print("p:", p)
    print("q:", q)
    print("n = pq:", n)
    print("totient:", totient)
    print("e (public key):", e)
    print("d (private key):", d)
    print("\nEncrypted data:", c)
    print("Original Message Sent:", m)

if __name__ == "__main__":
    rsa()