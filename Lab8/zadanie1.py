def wagomat(wartosc, jednostka):
    if jednostka == "km":
        wartosc*=1000
    elif jednostka == "m":
        wartosc*=1
    elif jednostka == "cm":
        wartosc*=0.01
    elif jednostka == "mm":
        wartosc*= 0.001
    return wartosc

class Wielkosc:
    dlugosc: float
    jednostka: str
    def __init__(self, dlugosc, jednostka='m'):
        self.dlugosc = dlugosc
        self.jednostka = jednostka
        self.m = wagomat(self.dlugosc, self.jednostka)
    def __add__(self, other):
        return Wielkosc(self.m + other.m, "m")
    def __sub__(self, other):
        return Wielkosc(self.m - other.m, "m")
    def __lt__(self, other):
        return (self.m < other.m)
    def __gt__(self, other):
        return (self.m > other.m)
    def __eq__(self, other):
        return (self.m == other.m)
    def __str__(self):
        return (str(self.dlugosc) + " " + self.jednostka)

x = Wielkosc(2)
y = Wielkosc(4000,"mm")
z = Wielkosc(100,"cm")

print("x = " + str(x))
print("y = " + str(y))
print("z = " + str(z))
print("suma w metrach = " + str(x+y+z))
print(x>z)
print(y<x)

x = Wielkosc(2) + Wielkosc(2)
print(str(x))