computador = {
    'notebook': 489990, 
    'tablet': 120000, 
    'cargador': 12400
    }

print(computador.keys())#dict_keys(['notebook', 'tablet', 'cargador'])

for elemento in computador.keys():
    print(elemento)
    
print(computador.values())#dict_values([489990, 120000, 12400])
for valor in computador.values():
    print(valor)
    


