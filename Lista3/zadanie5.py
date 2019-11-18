def kompresja(tekst):
    literka = 'a'
    ilosc = 1
    wynik = ''
    i = 0
    x = (len(tekst))
    tekst = tekst + ' ' 
    while i < x:
        literka = tekst[0]
        if tekst[0] == tekst[1]:
            ilosc = ilosc + 1 
        else:
            if ilosc > 1:
                wynik = wynik + '%i' % (ilosc) + literka 
            else:
                wynik = wynik + literka
            ilosc = 1
        tekst = tekst[1:]
        i = i+1
    return wynik
            


def dekompresja(tekst):
    wynik = ''
    i = 0
    while i < (len(tekst)):
        a = tekst[i]
        if a.isdigit():
            wynik = wynik + tekst[i+1] * int(tekst[i])
            i = i+2
        else:
            wynik = wynik + tekst[i]
            i = i+1
    return wynik


print(kompresja("Ala maaaat kotaaa  tiruuriru."))

print(dekompresja("Ala m4at kot3a."))
