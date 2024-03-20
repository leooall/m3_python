
estimulos = input("¿Reponde a estimulos? (s/n)\n").lower() 

if estimulos == "s":
    print("Valorar la necesidad de llevar al hospital mas cercano") 
else :
    print("Abrir la via aérea")
    
    respira = input("¿Respira? (s/n)\n").lower()
    if respira == "s":
        print("Permitirle posicion de suficiente ventilacion")
    else :
        print("Administrar 5 ventilaciones y llamar a la ambulacia")

        ambulancia = "n"
        while ambulancia == "n": 
            signos_de_vida = input("¿Signos de vida? (s/n)\n").lower()
            
            if signos_de_vida == "s":
                print("Reevaluar a la espera de la ambulancia")  
            else:
                print("Administrar compresiones toracicas hasta que llegue la ambulancia")      

            ambulancia = input("¿llego la ambulacia? [s/n]").lower()

print("Fin del programa")

