import random

def uprosc_zdanie(zdanie, maks, ilosc):
    z = zdanie.split()
    i = 0
    amount = len(z)
    while i < amount:
        if len(z[i]) > maks:
            z.remove(z[i])
            amount = amount - 1
        i = i + 1
    amount = len(z)
    while ilosc < amount:
        r = random.randint(0,len(z))
        z.remove(z[r])
        amount = amount - 1
    return " ".join(z)


zd = "Podział peryklinalny inicjałów wrzecionowatych \
kambium charakteryzuje się ścianą podziałową inicjowaną \
w płaszczyźnie maksymalnej."

print (uprosc_zdanie(zd, 10, 5))
