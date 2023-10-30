import os

#######################
# FUNCIONES
#######################

def user_input(unidad):
    longitud = float(input(f"ingrese la longitud del terreno ({unidad}): "))
    ancho = float(input(f"ingrese el ancho del terreno ({unidad}) : "))
    espesor = float(input(f"ingrese el espesor del terreno ({unidad}) : "))
    volumen = (longitud*ancho*espesor)
    return longitud, ancho, espesor, volumen

def calculo(volumen, cemento, arena, grava, agua):
    volumen_arena = (volumen*arena)
    volumen_grava = (volumen*grava)
    volumen_cemento = (volumen*cemento)
    cantidad_agua = (volumen*agua)
    return volumen_arena, volumen_grava, volumen_cemento, cantidad_agua

#######################
# VARIABLES
#######################

peso_sacos = {'cemento':50,'grava':30,'grava':25,'agua':20}


#######################
# MAIN
#######################

print('Ingrese los datos que le dio el cliente')
print('')
print('Que unidad desea usar?')
print('1. Metros')
print('2. Pies')
print('3. Yardas')
print('4. Salir')
print('')
#crea un menu simple para de 4 opciones
while True:
    sistema = int(input('Ingresa la unidad que se usara: '))
    match sistema:
        case 1:
            user_input('Metros')
        case 2:
            user_input('Pies')
        case 3:
            user_input('Yardas')
        case 4:
            print('')
            print('👋┊Gracias por usar el programa')
            print('')
            break
        case _:
            print('')
            print('❌┊Ingrese una opcion valida')
            print('')
            continue