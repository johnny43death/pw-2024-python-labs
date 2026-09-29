from zadanie import *

Morskoder = Morse()
Cezarkoder = Cezar()

#   TEST 1 = POPRAWNE DANE, przesunięcie cezara o 1
print("\nTEST 1 = POPRAWNE DANE, cezar=1")
kom1 = "LOREM IPSUM"
Morskoder.koduj(kom1)
kod1 = ".-.. --- .-. . -- _ .. .--. ... ..- --"
Morskoder.dekoduj(kod1)
mes1 = "LOREM IPSUM"
Cezarkoder.szyfruj(mes1, 1)
szfr1 = "LOREM IPSUM"
Cezarkoder.deszyfruj(szfr1, 1)

#   TEST 2 = RÓŻNE ROZMIARY LITER, mors bez spacji, przesunięcie cezara o 1
print("\nTEST 2 = RÓŻNE ROZMIARY LITER, mors bez spacji, cezar = 1")
kom2 = "LoReM iPsUm"
Morskoder.koduj(kom2)
kod2 = ".-..---.-..--_...--......---"
Morskoder.dekoduj(kod2)
mes2 = "LoReM iPsUm"
Cezarkoder.szyfruj(mes2, 1)
szfr2 = "lOrEm IpSuM"
Cezarkoder.deszyfruj(szfr2, 1)

#   TEST 3 = CYFRY I SYMBOLE ZAMIAST LITER, przesunięcie cezara o 1
print("\nTEST 3 = CYFRY I SYMBOLE ZAMIAST LITER, cezar = 1")
kom2 = "70:3'M 1+5^M"
Morskoder.koduj(kom2)
mes2 = "70:3'M 1+5^M"
Cezarkoder.szyfruj(mes2, 1)
szfr2 = "70:3'M 1+5^M"
Cezarkoder.deszyfruj(szfr2, 1)

#   TEST 4 = PRZESUNIĘCIE CEZARA MNIEJSZE OD 1
print("\nTEST 4 = cezar <= 0")
mes2 = "LOREM IPSUM"
Cezarkoder.szyfruj(mes2, -1)
szfr2 = "LOREM IPSUM"
Cezarkoder.deszyfruj(szfr2, 0)

#   TEST 5 = PRZESUNIĘCIE CEZARA NIE JEST CYFRĄ
print("\nTEST 5 = cezar nie jest cyfrą")
mes2 = "LOREM IPSUM"
Cezarkoder.szyfruj(mes2, "shift")
szfr2 = "LOREM IPSUM"
Cezarkoder.deszyfruj(szfr2, 3.14)
