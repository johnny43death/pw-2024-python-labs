def zlicz_znaki(tekst):
    ileenterow = tekst.count('\n')
    ileznakow = len(tekst)-ileenterow
    #return print(f"Całkowita liczba znaków: {ileznakow}")
    return ileznakow

def zlicz_slowa(tekst):
    slowa = tekst.split()
    ileslow = len(slowa)
    #return print(f"Liczba słów: {ileslow}")
    return ileslow

def zlicz_wielkie(tekst):
    ilewielkich = 0
    for i in range(len(tekst)):
        if tekst[i].isupper() == True:
            ilewielkich+=1
    #return print(f"Liczba wielkich liter: {ilewielkich}")
    return ilewielkich

def zlicz_male(tekst):
    ilemalych = 0
    for i in range(len(tekst)):
        if tekst[i].islower() == True:
            ilemalych+=1
    #return print(f"Liczba małych liter: {ilemalych}")
    return ilemalych

def zlicz_spacje(tekst):
    ilespacji = 0
    for i in range(len(tekst)):
        if tekst[i] == " ":
            ilespacji+=1
    #return print(f"Liczba spacji: {ilespacji}")
    return ilespacji