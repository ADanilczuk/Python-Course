from itertools import permutations

class Formula:
    def funct(self):
        print("to")


class Prawda(Formula): 
    def __str__(self):
        return 'True'

    def oblicz(self):
        return True
    
class Falsz(Formula):
    def __str__(self):
        return 'False'

    def oblicz(self):
        return False

class Zmienna(Formula):
    def __init__(self,var_name):
        self.var_name = var_name

    def __str__(self):
        return self.var_name

    def oblicz(self,zmienne):
        return zmienne[self.var_name].oblicz()

class Not(Formula):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        if isinstance(self.formula, Zmienna):
            return '~' + self.formula.__str__()
        return '~ (' + self.formula.__str__() + ')'

    def oblicz(self, zmienne):
        return not  self.formula.oblicz(zmienne)        

class And(Formula):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if isinstance(self.a , Zmienna):
            st = self.a.__str__() + ' ^ ' 
        else: st = '(' + self.a.__str__() + ') ^ '
        if isinstance(self.b , Zmienna):
            st = st + self.b.__str__()
        else: st = st + '(' + self.b.__str__() + ')'
        return st

    def oblicz(self,zmienne):
        return self.a.oblicz(zmienne) and self.b.oblicz(zmienne)

class Or(Formula):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if isinstance(self.a , Zmienna):
            st = self.a.__str__() + ' v ' 
        else: st = '(' + self.a.__str__() + ') v '
        if isinstance(self.b , Zmienna):
            st = st + self.b.__str__()
        else: st = st + '(' + self.b.__str__() + ')'
        return st

    def oblicz(self,zmienne):
        return self.a.oblicz(zmienne) or self.b.oblicz(zmienne)

class Impl(Formula):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if isinstance(self.a , Zmienna):
            st = self.a.__str__() + ' => ' 
        else: st = '(' + self.a.__str__() + ') => '
        if isinstance(self.b , Zmienna):
            st = st + self.b.__str__()
        else: st = st + '(' + self.b.__str__() + ')'
        return st

    def oblicz(self,zmienne):
        result_a = self.a.oblicz(zmienne)
        result_b = self.b.oblicz(zmienne)
        if not result_a :
            return True
        return result_b 

class Rown(Formula):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        if isinstance(self.a , Zmienna):
            st = self.a.__str__() + ' <=> ' 
        else: st = '(' + self.a.__str__() + ') <=> '
        if isinstance(self.b , Zmienna):
            st = st + self.b.__str__()
        else: st = st + '(' + self.b.__str__() + ')'
        return st

    def oblicz(self,zmienne):
        result_a = self.a.oblicz(zmienne)
        result_b = self.b.oblicz(zmienne)
        if result_a == result_b:
            return True
        return False 



def czy_tautologia(form,zmienne):
    zm = list(zmienne.keys())
    liczba_zmiennych = len(zm)
    lista_wart = 't' * liczba_zmiennych + 'f' * liczba_zmiennych
    wartosciowania = list(set(list(permutations(lista_wart, liczba_zmiennych))))
    for w in wartosciowania:
        wartosci = {}
        for i in range(liczba_zmiennych):
            if w[i] == 'f':
                wartosci.update({zm[i] : Falsz()})
            else: wartosci.update({zm[i] :  Prawda()})
        if not form.oblicz(wartosci) :
            return False
    return True


zm = { 'a' : Prawda(), 'b' : Falsz(), 'c' : Prawda() }
an = Impl(Zmienna('a'),Or(Zmienna('c'),Zmienna('b')))
print(an.oblicz(zm))

nie_an= Not(Impl(Zmienna('a'),Or(Zmienna('c'),Zmienna('b'))))
print(nie_an)
print(nie_an.oblicz(zm))

print(Not(Zmienna('c')))

##print(czy_tautologia(an, zm))

z = {'a': Falsz(), 'b' : Falsz(), 'c': Falsz()}
##print(an.oblicz(z))

print(czy_tautologia(nie_an,z))