def ciagodtylu(ciag):
    ciagrewers = [] # tworzy nową zmienną listową
    ciagrewers += ciag  # dodanie wartości, inaczej by przypisało odniesienie do oryginalnej tablicy i później odwracało obie tablice
    ciagrewers.reverse()
    return(ciagrewers)

def suma_ciagu_arytm(a1, r, n):
    return (2 * a1 + (n - 1) * r) * n / 2

a1 = 1
r = 1
n = 10
ciag_arytm = []
an = a1
for i in range(n):
    ciag_arytm.append(an)
    an += r

print(ciag_arytm)
print(suma_ciagu_arytm(a1, r, n))
print(ciagodtylu(ciag_arytm))