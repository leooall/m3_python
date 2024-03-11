p = float(input("Ingrese precio de suscripcion en clp: \n"))
u = float(input("Ingrese numero de usuarios: \n"))
gt = float(input("Ingrese gastos totales en clp: \n"))
utilidades_año_anterior= float(input("Ingrese las utilidades del año anterior en clp: \n"))

#utilidades = p * u - gt
utilidades_actuales = p * u - gt
#se divide la utilidad actual por la ultilidad del año anterior para obtener la razon
razon_utilidad_actual_y_anterior = utilidades_actuales / utilidades_año_anterior

#el resultado de la division se puede mulpiplicar por 100 para pasarlo a % -> ver linea 12
#razon_utilidad_actual_y_anterior = razon_utilidad_actual_y_anterior * 100

print("La razón entre la utilidad actual y del año anterior es: ", round(razon_utilidad_actual_y_anterior,2), "de crecimiento")
