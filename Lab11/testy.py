import funkcja, unittest

class TestWielomianu(unittest.TestCase):
    # schemat: test_s<stopien wielomianu>r<liczba rozwiązań>
    def test_s1r1(self):
        wielomian = [1, 3]
        rozwiazania = [-3]
        wynik = funkcja.oblicz(wielomian)
        for i, n in enumerate(wynik):
            self.assertAlmostEqual(n, rozwiazania[i], places=4)

    def test_s2r2(self):
        wielomian = [1, 2, -3]
        rozwiazania = [-3, 1]
        wynik = funkcja.oblicz(wielomian)
        for i, n in enumerate(wynik):
            self.assertAlmostEqual(n, rozwiazania[i], places=4)

    def test_s2r1(self):
        wielomian = [1, -6, 9]
        rozwiazania = [3]
        wynik = funkcja.oblicz(wielomian)
        for i, n in enumerate(wynik):
            self.assertAlmostEqual(n, rozwiazania[i], places=4)

    def test_s3r3(self):
        wielomian = [1, -9, -22, 240]
        rozwiazania = [-5, 6, 8]
        wynik = funkcja.oblicz(wielomian)
        for i, n in enumerate(wynik):
            self.assertAlmostEqual(n, rozwiazania[i], places=4)

    def test_s3r2(self):
        wielomian = [1, -6, 9]
        rozwiazania = [3]
        wynik = funkcja.oblicz(wielomian)
        for i, n in enumerate(wynik):
            self.assertAlmostEqual(n, rozwiazania[i], places=4)

    def test_s2deltaujemna(self):
        wielomian = [2, 2, 2]
        rozwiazania = []
        wynik = funkcja.oblicz(wielomian)
        for i, n in enumerate(wynik):
            self.assertAlmostEqual(n, rozwiazania[i], places=4)

if __name__ == '__main__':
    unittest.main()
