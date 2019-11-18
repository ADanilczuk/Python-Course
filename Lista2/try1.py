from itertools import permutations

liczba_zmiennych = 3

tf_pattern = 't' * liczba_zmiennych + 'f' * liczba_zmiennych
print(tf_pattern)

   
a = list(set(list(permutations(tf_pattern, liczba_zmiennych))))
print (a)
print(len(a))