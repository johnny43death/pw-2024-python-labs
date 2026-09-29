import funkcja

wspolczynniki = [1, -3, 2]  # Wielomian: x^2 - 3x + 2
x_min = -10
x_max = 10
zakres = [x_min, x_max]
n = 10

pierwiastki, wartosci_x, wartosci_y = funkcja.oblicz(wspolczynniki, zakres, n)
print("Pierwiastki:", pierwiastki, "\nWartosciX: ", wartosci_x, "\nWartosciY: ", wartosci_y)

with open("output.txt", "w") as file:
    file.write("Pierwiastki:\n")
    file.write(", ".join(map(str, pierwiastki)) + "\n")
    file.write("\nWartości funkcji:\n")
    for x, y in zip(wartosci_x, wartosci_y):
        file.write(f"x = {x}, f(x) = {y}\n")
