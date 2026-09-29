def listowanie(numstring):
    numlist = numstring.split()
    ncount = 0

    print(len(numlist))

    for i in range(len(numlist)):
        icount = 0
        for j in range(i + 1, len(numlist)):
            if numlist[i] == numlist[j]:
                icount += 1
        if icount > 0:
            ncount += 1
    print(f'liczb powtarzających się jest: {ncount}')

    numlist.sort()
    numlist = list(dict.fromkeys(numlist))
    print(numlist)

    numlist.pop()
    print(numlist)

    prime = input("Dodaj element na początku listy: ")
    last = input("Dodaj element na końcu listy: ")
    numlist.insert(0, prime)
    numlist.insert(len(numlist), last)
    print(numlist)

    oddlst = []
    evenlst = []

    for i in range(len(numlist)):
        if i % 2 == 0:
            evenlst.append(numlist[i])
        else:
            oddlst.append(numlist[i])

    print("Parzyste indeksy: ", evenlst)
    print("Nieparzyste indeksy: ", oddlst)


if __name__ == "__main__":
    ciagznakow = input("Podaj listę numerków: ")
    listowanie(ciagznakow)
