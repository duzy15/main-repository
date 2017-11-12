a = int(input("Wprowadż wartość a:"))
if a==0:
    print("Kiedy a jest równe 0 to mamy funkcję liniową")
    exit()
b = int(input("Wprowadż wartość b:"))
c = int(input("Wprowadż wartość c:"))

d=b*b-4*a*c

if d<0:
    print("Delta < 0, Funkcja nie posiada miejsc zerowych")
elif d==0:
    print("Delta = 0, Funkcja posiada jedno miejsce zerowe: x0 = ",int(b*(-1)/2*a))
else:
    print("Delta > 0, Funkcja posiada dwa miejsca zerowe: ""x1=",int((b*(-1)+d**0.5)/2*a),", x2=",int((b*(-1)-d**0.5)/2*a))

p=b*(-1)/2*a
q=d*(-1)/4*a

print("Współrzędne wierzchołka wykresu funkcji kwadratowej : p=",int(p),", q=",int(q),)

if a>0:
    print("Wyraz a jest dodatni więc ramiona paraboli skierowane są do góry")
elif a<0:
    print("Wyraz a jest ujemny więc ramiona paraboli skierowane są do dołu")
