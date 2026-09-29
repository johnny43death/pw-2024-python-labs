from zadanie import *

komik = input("Podaj kod do zaszyfrowania alfabetem Morse'a: ").upper()
# KOD DO DEKODOWANIA NALEZY WPROWADZAC ZE SPACJAMI
#   np lorem ipsum to: ".-.. --- .-. . -- _ .. .--. ... ..- --"
kodzik = input("Podaj kod do odszyfrowania alfabetem Morse'a: ").upper()
cos = Morse()
cos.koduj(komik)
cos.dekoduj(kodzik)

szyfr = input("Podaj kod do zaszyfrowania szyfrem cezara: ").upper()
step = int(input("Ile ma się przesunąć? "))
wiadom = input("Podaj kod do odszyfrowania szyfrem cezara: ").upper()
krok = int(input("Ile ma się przesunąć? "))
cos2 = Cezar()
cos2.szyfruj(szyfr, step)
cos2.deszyfruj(wiadom, krok)
