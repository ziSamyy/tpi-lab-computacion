import os

#######################
# FUNCIONES
#######################

def terrain_menu():
    print('Ingrese los datos que le dio el cliente')
    print('')
    print('Que unidad desea usar?')
    print('1. Metros')
    print('2. Pies')
    print('3. Yardas') 
    print('4. Salir')
    print('')
    while True:
        sistema = int(input('Ingresa la unidad que se usara: '))
        match sistema:
            case 1:
                terrain_input('Metros')
            case 2:
                terrain_input('Pies')
            case 3:
                terrain_input('Yardas')
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

def concrete_type_menu():
    print('Ahora debe ingrear la dosificacion de concreto que el cliente desea usar')
    print("esta puede ser de 5 tipos que varia en precio y resistencia ")
    print('Tener en cuenta que depende el tipo varia el precio y resistencia.')
    print('')
    
    print('1. 246')
    print('2. 210')
    print('3. 175')
    print('4. 140')
    print('5. 105')
    print('')
    while True:
        concrete_type = int(input('Ingrese el tipo de concreto que desea usar: '))
        match concrete_type:
            case 1:
                materiales = [420, 0.67, 0.67, 220] # Cemento (kg), arena(m3), grava(m3), agua(L)
                
                  
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass  

def terrain_input(unidad):
    longitud = float(input(f"ingrese la longitud del terreno ({unidad}): "))
    ancho = float(input(f"ingrese el ancho del terreno ({unidad}) : "))
    espesor = float(input(f"ingrese el espesor del terreno ({unidad}) : "))
    volumen = (longitud*ancho*espesor)
    return longitud, ancho, espesor, volumen

def calc_amount(materiales):
    amount_cem = round((materiales[0] / peso_sacos['cemento']), 2)
    amount_arena = round((materiales[1]))

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


#crea un menu simple para de 4 opciones
