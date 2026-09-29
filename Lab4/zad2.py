import numpy
import math

x = float(input("Podaj wartość X: "))
SumaMaclaurina = 0
for N in range(0,11):
    SumaMaclaurina += (pow(x, N))/math.factorial(N)

print(f'suma obliczona z fora: {SumaMaclaurina}')
print(f'suma obliczona z exp(): {numpy.exp(x)}')
bbp = numpy.exp(x)-SumaMaclaurina
print(f'błąd bezwzględnego przybliżenia: {bbp}')