"""Matemaatilised tehted"""
import math

# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b
a = float(input("Sisesta oma a kaatet: "))
b = float(input("Sisesta oma b kaatet: "))
# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
c2 = float(a * a + b * b)
c = round(math.sqrt(c2), 2)
print(f"hüpoteenus on {c}")
print (f"ümbermõõt on {c + a + b}")
print (f"pindala on {(a + b)/2}")
# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
