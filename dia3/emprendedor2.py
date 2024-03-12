#Solicitud de datos
s_normal = float(input("Ingrese precio de suscripcion normal en clp: \n"))
s_premium = float(input("Ingrese precio de suscripcion premium en clp: \n"))
u_normales = float(input("Ingrese numero de usuarios normales: \n"))
u_premium= float(input("Ingrese numero de usuarios premium: \n"))
gt = float(input("Ingrese gastos totales en clp: \n"))

#Calculo de utilidades
utilidades = (s_normal * u_normales) + (s_premium * u_premium) - gt

#Salida de datos
print("La utilidad es: ", round(utilidades, ), "Clp")