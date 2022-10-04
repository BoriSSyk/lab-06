import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))
spisok = []
while a <= b:
    spisok.append(m.pow(2, a) / m.sqrt(m.pow(a, 2)+1) +
                  m.log(2)*m.sqrt(a)+m.sqrt(1))
    a += h
matarik = 0
while matarik != len(spisok):
    matarik += 1

spisok.sort()
print("найменше: " + str(spisok[0]), "найбільше: " + str(spisok[-1]))
