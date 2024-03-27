from os import system
computador = {
    'notebook': 489990, 
    'tablet': 120000, 
    'cargador': 12400
    }
print(computador.keys())#dict_keys(['notebook', 'tablet', 'cargador'])
for key in computador.keys():
    print(key)  #notebook
                #tablet
                #cargador
    
print("*****")
system("clear")
print(computador.values())#dict_values([489990, 120000, 12400])
for valor in computador.values():
    print(valor)#489990
                #120000
                #12400

print("*****")
system("clear")
print(computador.items())#dict_items([('notebook', 489990), ('tablet', 120000), ('cargador', 12400)])
for clave,valor in computador.items():
    print(f"clave {clave} - valor {valor}")
    #clave notebook - valor 489990
    #clave tablet - valor 120000
    #clave cargador - valor 12400
print("*****")
""" 
Sets
Se escriben con {}, no tienen clave, no permite datos repetidos
no tienen un orden especifico
"""
system("clear")
muchos_animales = {'Gato', 'Perro', 'Tortuga',
                    'Gato', 'Perro', 'Tortuga',
                    'Gato', 'Perro', 'Tortuga',
                    'Gato', 'Perro', 'Tortuga',
                    'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)
muchos_animales.add(7)
muchos_animales.remove("Hamster")
muchos_animales.discard("Hurón")
muchos_animales.discard("Raton")
muchos_animales.pop()
print(muchos_animales)
muchos_animales.clear()
print(muchos_animales)#set()

