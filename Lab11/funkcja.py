import numpy

def oblicz(wielomian:list, zakres:list = [0,0], przedzialy:int = 0):
    assert isinstance(wielomian,list)
    assert all(isinstance(x, (int,float)) for x in wielomian)
    assert isinstance(zakres, list)
    assert isinstance(przedzialy, int)
    assert len(zakres) == 2
    assert przedzialy >= 0
    assert len(wielomian) > 0
    pierwiastki = numpy.polynomial.polynomial.polyroots(wielomian[::-1])
    pierwiastki_rw = numpy.real(pierwiastki)
    pierwiastki_wyjsciowe = []

    for i, e in enumerate(pierwiastki):
        if e == pierwiastki_rw[i]:
            pierwiastki_wyjsciowe.append(float(numpy.real(e)))
    pierwiastki_wyjsciowe = set(pierwiastki_wyjsciowe)
    if przedzialy == 0:
        return sorted(list(pierwiastki_wyjsciowe))
    else:
        wartosci_x = numpy.linspace(zakres[0], zakres[1], przedzialy)
        wartosci_y = []
        for przedzialy in wartosci_x:
            wartosci_y.append(numpy.polyval(wielomian, przedzialy))
        return sorted(list(pierwiastki_wyjsciowe)), list(wartosci_x), wartosci_y
