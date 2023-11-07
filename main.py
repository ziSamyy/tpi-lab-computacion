import os

#######################
# FUNCIONES
#######################


def client_info():
    client_dni = int(input('Ingrese el DNI del cliente: '))
    client_name = input('Ingrese el nombre del cliente: ')
    client_lastname = input('Ingrese el apellido del cliente: ')
    client_phone = int(input('Ingrese el telefono del cliente: '))
    return client_dni, client_name, client_lastname, client_phone

def convertidor(sistema, longitud, ancho, espesor):
    match sistema:
        case 'Metros': 
            longitud = longitud
            ancho = ancho
            espesor = espesor
        case "Pies": 
            longitud = longitud * 0.0254
            ancho = ancho * 0.0254
            espesor =espesor * 0.0254
        case "Yardas":
            longitud = longitud * 0.3048
            ancho = ancho * 0.3048
            espesor = espesor * 0.3048
    return longitud, ancho, espesor

def cant_bolsas(materiales, peso_sacos):
    bolsa_cemento = round((materiales[0] / peso_sacos['cemento']), 2)
    bolsa_arena = round((materiales[1] / peso_sacos['arena']), 2)
    bolsa_grava = round((materiales[2] / peso_sacos['grava']), 2)
    bidon_agua = round((materiales[3] / peso_sacos['agua']), 2)
    return bolsa_cemento, bolsa_arena, bolsa_grava, bidon_agua

def volumen_materiales(volumen, materiales):
    volumen_cemento = volumen * materiales[0]
    volumen_arena = volumen * materiales[1]
    volumen_grava = volumen * materiales[2]
    volumen_agua = volumen * materiales[3]
    return volumen_cemento, volumen_arena, volumen_grava, volumen_agua

def cant_sacos(cant_bolsas, peso_sacos):
    cant_cemento = round((cant_bolsas[0] / peso_sacos['cemento']), 2)
    cant_arena = round((cant_bolsas[1] / peso_sacos['arena']), 2)
    cant_grava = round((cant_bolsas[2] / peso_sacos['grava']), 2)
    cant_agua = round((cant_bolsas[3] / peso_sacos['agua']), 2)
    return cant_cemento, cant_arena, cant_grava, cant_agua

def ticketfile(clientinfo, terrainmenu, concretetpye, cantbolsas, volmat, cantsacos):
    with open('ticket.txt', 'w') as ticket:
        ticket.write('Informacion del cliente\n')
        ticket.write(f'DNI: {clientinfo[0]}\n')
        ticket.write(f'Nombre: {clientinfo[1]}\n')
        ticket.write(f'Apellido: {clientinfo[2]}\n')
        ticket.write(f'Telefono: {clientinfo[3]}\n')
        ticket.write('Informacion del terreno\n')
        ticket.write(f'Sistema: {terrainmenu[0]}\n')
        ticket.write(f'Longitud: {terrainmenu[1]}\n')
        ticket.write(f'Ancho: {terrainmenu[2]}\n')
        ticket.write(f'Espesor: {terrainmenu[3]}\n')
        ticket.write(f'Volumen: {terrainmenu[4]}\n')
        ticket.write('Informacion del concreto\n')
        ticket.write(f'Tipo: {concretetpye[1]}\n')
        ticket.write(f'Cemento: {concretetpye[0][0]}\n')
        ticket.write(f'Arena: {concretetpye[0][1]}\n')
        ticket.write(f'Grava: {concretetpye[0][2]}\n')
        ticket.write(f'Agua: {concretetpye[0][3]}\n')
        ticket.write('Informacion de los materiales\n')
        ticket.write(f'Cemento: {cantbolsas[0]}\n')
        ticket.write(f'Arena: {cantbolsas[1]}\n')
        ticket.write(f'Grava: {cantbolsas[2]}\n')
        ticket.write(f'Agua: {cantbolsas[3]}\n')
        ticket.write('Informacion de los volumenes\n')
        ticket.write(f'Cemento: {volmat[0]}\n')
        ticket.write(f'Arena: {volmat[1]}\n')
        ticket.write(f'Grava: {volmat[2]}\n')
        ticket.write(f'Agua: {volmat[3]}\n')
        ticket.write('Informacion de los sacos\n')
        ticket.write(f'Cemento: {cantsacos[0]}\n')
        ticket.write(f'Arena: {cantsacos[1]}\n')
        ticket.write(f'Grava: {cantsacos[2]}\n')
        ticket.write(f'Agua: {cantsacos[3]}\n')

def clientagenda(clientinfo):
    if not os.path.isfile('agenda.txt'):
        with open('agenda.txt', 'w') as agenda:
            agenda.write('Informacion del cliente\n')
            agenda.write(f'DNI: {clientinfo[0]}\n')
            agenda.write(f'Nombre: {clientinfo[1]}\n')
            agenda.write(f'Apellido: {clientinfo[2]}\n')
            agenda.write(f'Telefono: {clientinfo[3]}\n')
    else:
        with open('agenda.txt', 'a', encoding='utf-8') as agenda:
            agenda.write('Informacion del cliente\n')
            agenda.write(f'DNI: {clientinfo[0]}\n')
            agenda.write(f'Nombre: {clientinfo[1]}\n')
            agenda.write(f'Apellido: {clientinfo[2]}\n')
            agenda.write(f'Telefono: {clientinfo[3]}\n')
#######################
# MENUS
#######################
def terrain_menu():
    print('')
    print('Que unidad desea usar?')
    print('1. Metros')
    print('2. Pies')
    print('3. Yardas') 
    print('')
    while True:
        sistema = int(input('Ingresa la unidad que se usara: '))
        match sistema:
            case 1:
                longitud = float(input("ingrese la longitud del terreno (Metros): "))
                ancho = float(input("ingrese el ancho del terreno (Metros): "))
                espesor = float(input("ingrese el espesor del terreno (Metros): "))
                volumen = (longitud*ancho*espesor)
                sistema = 'Metros'
                return sistema, longitud, ancho, espesor, volumen
            case 2:
                longitud = float(input("ingrese la longitud del terreno (Pies): "))
                ancho = float(input("ingrese el ancho del terreno (Pies): "))
                espesor = float(input("ingrese el espesor del terreno (Pies): "))
                volumen = (longitud*ancho*espesor)
                sistema = 'Pies'
                return sistema, longitud, ancho, espesor, volumen
            case 3:
                longitud = float(input("ingrese la longitud del terreno (Yardas): "))
                ancho = float(input("ingrese el ancho del terreno (Yardas): "))
                espesor = float(input("ingrese el espesor del terreno (Yardas): "))
                sistema = 'Yardas'
                volumen = (longitud*ancho*espesor)
                return sistema, longitud, ancho, espesor, volumen
            case _:
                print('')
                print('❌Ingrese una opcion valida')
                print('')
                continue

def concrete_type_menu():
    print('')
    print('Ingresa la dosificacion de Concreto')
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
                materiales = [420, 0.67, 0.67, 0.22] # Cemento (kg), arena(m3), grava(m3), agua(m3)
                type = '246'
                return materiales, type
            case 2:
                materiales = [350, 0.56, 0.84, 0.18] # Cemento (kg), arena(m3), grava(m3), agua(m3)
                type = '210'
                return materiales, type
            case 3:
                materiales = [300, 0.56, 0.96, 0.17] # Cemento (kg), arena(m3), grava(m3), agua(m3)
                type = '175'
                return materiales, type
            case 4:
                materiales = [260, 0.63, 0.84, 0.17] # Cemento (kg), arena(m3), grava(m3), agua(m3)
                type = '140'
                return materiales, type
            case 5:
                materiales = [210, 0.5, 1, 0.16]
                type = '105'
                return materiales, type
            case _:
                print('')
                print('❌Ingrese una opcion valida')
                print('')
                continue

def main():
    
    peso_sacos = {'cemento':0.022727272727272728, 'grava': 0.01764705882352941, 'arena':0.019230769230769232, 'agua': 0.02}
    clientinfo = client_info() # ('DNI', 'Nombre', 'Apellido', 'Telefono') ✅
    terrainmenu = terrain_menu() # ('Sistema', 'Longitud', 'Ancho', 'Espesor', 'volumen') ✅
    convertido = convertidor(terrainmenu[0], terrainmenu[1], terrainmenu[2], terrainmenu[3]) #✅
    concretetpye = concrete_type_menu() # ('Materiales', 'Tipo') ✅
    cantbolsas = cant_bolsas(concretetpye[0], peso_sacos) # ('Cemento', 'Arena', 'Grava', 'Agua') ✅
    volmat = volumen_materiales(terrainmenu[4], concretetpye[0]) # ('Cemento', 'Arena', 'Grava', 'Agua') ✅
    cantsacos = cant_sacos(cantbolsas, peso_sacos) # ('Cemento', 'Arena', 'Grava', 'Agua') ✅
    ticketfile(clientinfo, terrainmenu, concretetpye, cantbolsas, volmat, cantsacos) # ✅
    clientagenda(clientinfo) # ✅