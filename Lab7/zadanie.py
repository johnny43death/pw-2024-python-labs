import funkcje

if __name__ == "__main__":
    file = open("plikwejscia.txt", "r")
    czyt = str(file.read())

    komunikat = f"Całkowita liczba znaków: {funkcje.zlicz_znaki(czyt)}\nLiczba słów: {funkcje.zlicz_slowa(czyt)}\nLiczba wielkich liter: {funkcje.zlicz_wielkie(czyt)}\nLiczba małych liter: {funkcje.zlicz_male(czyt)}\nLiczba małych liter: {funkcje.zlicz_male(czyt)}"
    print(komunikat)

    file.close()

    wynik = open("statystyka.txt", "w")
    wynik.write(komunikat)
    wynik.close()
