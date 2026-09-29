def addStudent():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    specjalnosc = input("Specjalność: ")
    ocena1 = float(input("Ocena 1: "))
    ocena2 = float(input("Ocena 2: "))
    ocena3 = float(input("Ocena 3: "))
    ocena4 = float(input("Ocena 4: "))
    ocena5 = float(input("Ocena 5: "))
    rekord = {
        "Imię": imie,
        "Nazwisko": nazwisko,
        "Specjalność": specjalnosc,
        "Ocena 1": ocena1,
        "Ocena 2": ocena2,
        "Ocena 3": ocena3,
        "Ocena 4": ocena4,
        "Ocena 5": ocena5,
    }
    print("Student dodany pomyślnie!")
    return rekord

def displayList():
    for i in range(len(lista)):
        srednia = (lista[i]["Ocena 1"] + lista[i]["Ocena 2"] + lista[i]["Ocena 3"] + lista[i]["Ocena 4"] + lista[i]["Ocena 5"])/5
        print(f'{lista[i]["Imię"]} {lista[i]["Nazwisko"]}\n\t'
              f'Student specjalności: {lista[i]["Specjalność"]}\n\t'
              f'Ma oceny: {lista[i]["Ocena 1"]}, {lista[i]["Ocena 2"]}, {lista[i]["Ocena 3"]}, {lista[i]["Ocena 4"]}, {lista[i]["Ocena 5"]}\n\t'
              f'Średnia ocen: {srednia}\n')

        print(f"\nLiczba studentów: {len(lista)}")


trwanieprogramu = True
lista = []
while trwanieprogramu == True:
    opcja = int(input("=======================\nCo chciałbyś sprawdzić?\n\t[1] - Dodaj studenta\n\t[2] - Wyświetl listę studentów\n\t[3] - Usuń ostatniego studenta\n\t[4] - Zakończ działanie\n"))
    if opcja == 1:
        lista.append(addStudent())
    elif opcja == 2:
        displayList()
    elif opcja == 3:
        lista.pop()
    elif opcja == 4:
        trwanieprogramu = False
        exit()
    else:
        print("Błąd wprowadzenia, wyłączam program")
        exit()