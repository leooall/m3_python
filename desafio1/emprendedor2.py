#Solicitud de datos
suscripcion = float(input("Ingrese precio de suscripcion en clp: \n"))
u_normales = int(input("Ingrese numero de usuarios normales: \n"))
u_premium= int(input("Ingrese numero de usuarios premium: \n"))
gastos_totales = float(input("Ingrese gastos totales en clp: \n"))

#Calculo de utilidades
utilidades_usuarios_normales = suscripcion * u_normales
utilidad_usuarios_premium = (1.5 * suscripcion * u_premium)

utilidades = (utilidades_usuarios_normales + utilidad_usuarios_premium) - gastos_totales

#Salida de datos
print(f"La utilidad es: {round(utilidades, )} Clp")