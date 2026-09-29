class CustomError(Exception):
    pass

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
        komunikat = komunikat.upper()
        try:
            kod = ""
            for i in range(len(komunikat)):
                if komunikat[i] not in self.mors.keys():
                    raise CustomError("«BŁĄD!» Wiadomość może składać się tylko z liter i spacji.")
                else:
                    kod += self.mors[komunikat[i]] + " "
            return print(kod)
        except CustomError as e:
            print(e)

    def dekoduj(self, kod):
        kod = kod.upper()
        try:
            kod = kod.split(" ")
            komunikat = ""
            for i in range(len(kod)):
                if kod[i] not in self.mors_odw.keys():
                    raise CustomError("«BŁĄD!» Wiadomość może składać się tylko z liter w kodzie Morse'a oddzielonymi spacjami i spacjami w postaci '_'.")
                else:
                    komunikat += self.mors_odw[kod[i]]
            return print(komunikat)
        except CustomError as e:
            print(e)

class Cezar(Kod_dekod):
    def __init__(self):
        pass

    def szyfruj(self, komunikat, przesuniecie):
        komunikat = komunikat.replace(" ","").upper()
        asciilista = []
        for i in range(65,91):
            asciilista.append(chr(i))
        try:
            kod = ""
            for i in range(len(komunikat)):
                if komunikat[i] not in asciilista:
                    raise CustomError("«BŁĄD!» Wiadomość może składać się tylko z liter.")
                elif type(przesuniecie) is not int or przesuniecie<0:
                    raise CustomError("«BŁĄD!» Przesunięcie musi być nieujemną liczbą.")
                else:
                    indeks = komunikat[i].upper()
                    kod += chr((ord(indeks) + przesuniecie - 65) % 26 + 65)
            return print(kod)
        except CustomError as e:
            print(e)

    def deszyfruj(self, kod, przesuniecie):
        asciilista = []
        for i in range(65,91):
            asciilista.append(chr(i))
        try:
            kod = kod.replace(" ","").upper()
            komunikat = ""
            for i in range(len(kod)):
                if kod[i] not in asciilista:
                    raise CustomError("«BŁĄD!» Wiadomość może składać się tylko z liter i spacji.")
                elif type(przesuniecie) is not int or przesuniecie<0:
                    raise CustomError("«BŁĄD!» Przesunięcie musi być nieujemną liczbą.")
                else:
                    indeks = kod[i].upper()
                    komunikat += chr((ord(indeks) - przesuniecie - 65) % 26 + 65)
            return print(komunikat)
        except CustomError as e:
            print(e)
