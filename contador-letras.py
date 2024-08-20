
    # Solicitar al usuario ingrasar una palabra
veces = 0
veces_max = 3

while veces < veces_max:
    palabra_ingresada = input("Por favor ingrese una palabra: ")

    # Contaríamos la cantidad de letras que tiene la palabra ingresada

    cantidad_letras = len(palabra_ingresada)

    # Mostraríamos al ususario la cantidad de letras que tiene la palabra que ingresó

    print("La palabra ingresada tiene", cantidad_letras, "letras")

    veces += 1

print("Gracias por contar conmigo")