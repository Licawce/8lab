from random import randint
a = []
for i in range(20):
    a.append(randint(0, 100))
print(*a)
a.sort()
print(*a)
print(f"max - {max(a)}\nmin - {min(a)}")
summa = 0
for i in a:
    summa+= i
print(f"Сумма списка - {summa}")
