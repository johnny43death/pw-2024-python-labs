class Kod_dekod:
    def __init__(self,kod):
        self.kod = kod
    def __init__(self,kod,przesuniecie):
        self.kod = kod
        self.przesuniecie = przesuniecie

class Morse(Kod_dekod):
    mors = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ':'_'
    }
    #self.mors_odw = {}
    def __init__(self):
        self.mors_odw = dict(map(reversed, self.mors.items()))

    def koduj(self, komunikat):
        kod = ""
        for i in range(len(komunikat)):
            kod += self.mors[komunikat[i]] + " "
        return print(kod)

    def dekoduj(self, kod):
        kod = kod.split(" ")
        komunikat = ""
        for i in range(len(kod)):
            komunikat += self.mors_odw[kod[i]]
        return print(komunikat)

class Cezar(Kod_dekod):
    def __init__(self):
        pass

    def szyfruj(self, komunikat, przesuniecie):
        kod = ""
        for i in range(len(komunikat)):
            indeks = komunikat[i].upper()
            kod += chr((ord(indeks) + przesuniecie - 65) % 26 + 65)
        return print(kod)

    def deszyfruj(self, kod, przesuniecie):
        kod.replace(" ","")
        komunikat = ""
        for i in range(len(kod)):
            indeks = kod[i].upper()
            komunikat += chr((ord(indeks) - przesuniecie - 65) % 26 + 65)
        return print(komunikat)
