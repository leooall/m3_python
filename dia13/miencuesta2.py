def imprimir_menu():
    print('Opciones: ')
    print('1). De acuerdo')
    print('2). En desacuerdo')
    print('3). No me interesa')
preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2', 'Enunciado Pregunta 3']
respuestas = []
# Hacer preguntas
for pregunta in preguntas:
    print(pregunta)
    imprimir_menu()
    respuestas.append(input('> '))

for i in range(len(respuestas)): #[0,1,2]  len=3
    print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')

print('Muchas gracias por responder la encuesta')
