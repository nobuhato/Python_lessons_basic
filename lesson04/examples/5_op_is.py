# Оператор is - возвращает True если операнды указывают на один и то же объект в памяти
a = 10
b = 10

c = [1, 2]
d = c
e = [1, 2]

print(a is b)  # Неизменяемые типы данных python кэширует для экономия памяти

print(c is d)  # с и d - указывают на один и то же объект
print(d is e)  # d и e - разные объекты

# Так лучше, чем: if a == None
print(a is None)
