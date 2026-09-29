def suma_ciagu_geom(a1, q, n):
    return (a1 * (1 - pow(q,n))) / (1 - q)

a1 = 1
q = 2
n = 10
ciag_geom = []
an = a1
for i in range(n):
    ciag_geom.append(an)
    an *= q

print(ciag_geom)
print(suma_ciagu_geom(a1, q, n))