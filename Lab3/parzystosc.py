"""N = 7
ile_razy = 0
for i in range(N):
ile_razy += 1
if i%3 == 0:
print(str(i)+" jest liczbą parzystą")
els:
print(str(i)+" jest liczbą nieparzystą")
print("sprawdzonych "+str(ile_razy)+" liczb")"""

N = 7
ile_razy = 0
for i in reversed(range(N)):
    ile_razy += 1
    if i%2 == 0:
        print(str(i)+" jest liczbą parzystą")
    else:
        print(str(i)+" jest liczbą nieparzystą")
print("sprawdzonych "+str(ile_razy)+" liczb")