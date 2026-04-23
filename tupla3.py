from collections import namedtuple


planeta = namedtuple('planeta', ['nombre','numero'])

mercurio = planeta('mercurio', 1)
venus = planeta('venus', 2)
tierra = planeta('tierra', 3)
marte = planeta('marte', 14)

print(mercurio.nombre)
print(mercurio.numero)
print(venus.nombre)
print(tierra.nombre)
print(marte.nombre)
print(venus[0])
print(venus[1])

print("Campos de la tupla: {}".format(tierra._fiels))