def fibo(n):
    wynik = []
    a = 0
    b = 1
    while a <= n:
        wynik.append(a)
        a, b = b, a + b
    return print(wynik)


if __name__ == "__main__":
    N = int(input("Podaj N (górną granicę ciągu Fibonacciego): "))
    fibo(N)
