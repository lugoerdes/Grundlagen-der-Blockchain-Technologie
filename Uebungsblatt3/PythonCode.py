import sys
sys.set_int_max_str_digits(1000000000)

def modinv(a, m):
    # Erweiterter Euklidischer Algorithmus
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        # q ist der Quotient
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

d = modinv(65537, 5760)
print("d:", d)
print(3169**7 % 1403)
print(558**943 % 1403)
print(3169**1613 % 2813)
print(pow(3169,1613) % 2813)
print(677**5 % 2813)
print(pow(677,5) % 2813)