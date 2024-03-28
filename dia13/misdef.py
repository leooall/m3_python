#****ANATOMIA DE UNA FUNCION; PARAMETROS Y ARGUMENTOS
def elevado_2(x):# x es el parametro, al remplazarlo por un numero se convierte en argumento
    print(x**2)

elevado_2(4)#16

def elevar(x, y):# x ,y son los parametros
    print(x**y)
elevar(3, 3) #27 --> 3,3 son los argumentos

def elevar(base, exponente):
    print(base**exponente)

elevar(3,3)#27 --> 3,3 son los argumentos


