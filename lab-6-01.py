import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))

for Bar in range(100):
    mox = (m.pow(2, Bar) / m.sqrt(m.pow(Bar, 2)+1) +
           m.log(2)*m.sqrt(Bar)+m.sqrt(1))
    print(mox)
    if Bar == b:
        break
