
def zaszyfruj(tekst, klucz):
    tks = ''
    for i in range(len(tekst)):
        xored_value = klucz ^ ord(tekst[i])
        tks=tks+chr(int(bin(xored_value),2))
    return tks


def odszyfruj(tekst, klucz):
    tks=''
    for i in range(len(tekst)):
        xored_value = klucz ^ ord(tekst[i])
        tks=tks+chr(int(bin(xored_value),2))
    return tks


def zs(tekst, klucz):
    wyn = ""
    for c in tekst:
        wyn += chr((ord(c) ^ klucz))
    return wyn

a=0b1011
print(type(a))
print(zaszyfruj('Python',7))
print(zaszyfruj('W~sohi',7))

print(zs('Python',7))
print(zs('W~sohi',7))