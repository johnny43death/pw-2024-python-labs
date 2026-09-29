import sympy

N = int(input("Podaj N, kraniec przedziału: "))
possibleprime = 0
perfect = 0

for i in range(1, N+1):
    possibleprime = (pow(2, i)-1)
    if sympy.isprime(possibleprime) == True:
        perfect = possibleprime * (pow(2, i-1))
        if perfect > N:
            break
        print(perfect)