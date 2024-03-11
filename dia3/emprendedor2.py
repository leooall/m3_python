
p_normal = float(input("Ingrese precio de suscripcion normal en clp: \n"))
p_premium = float(input("Ingrese precio de suscripcion premium en clp: \n"))
u_normales = float(input("Ingrese numero de usuarios normales: \n"))
u_premium= float(input("Ingrese numero de usuarios premium: \n"))
gt = float(input("Ingrese gastos totales en clp: \n"))


utilidades = (p_normal * u_normales) + (p_premium * u_premium) - gt


print("La utilidad es: ", round(utilidades, ), "Clp")