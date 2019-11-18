
def vat_faktura(a):
    wynik=sum(a)
    return wynik*1.23


def vat_paragon(lista ):
    second_list=[1.23*e for e in lista]
    return sum(second_list)

l=[1,2,3]
print(vat_faktura(l))
print(vat_paragon(l))

zakupy = [0.2, 0.5, 4.59, 6,0.2, 0.5, 4.59, 6,0.2, 0.5, 4.59, 6,0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy) == vat_paragon(zakupy))