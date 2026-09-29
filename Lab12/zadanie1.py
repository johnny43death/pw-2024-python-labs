import numpy as np

def obrot(macierz, kat):
    try:
        if kat % 90 != 0:
            raise ValueError()
        l_obrotow = (kat // 90) % 4
        mat = macierz.copy()
        for i in range(int(l_obrotow)):
            mat = mat.transpose()
            mat = np.flip(mat, 1)
        return mat
    except TypeError:
        print("Podaj całkowitą liczbę, wielokrotność 90 stopni")
    except ValueError:
        print("Kąt musi być całkowitą wielokrotnością 90 stopni!")

#def obrot3D(macierz, kat)

if __name__ == "__main__":
    x = np.ndarray(shape=(2,2),dtype=int, order='F', buffer=np.array([1,2,3,4]))
    print(x)
    print(obrot(x, 90))