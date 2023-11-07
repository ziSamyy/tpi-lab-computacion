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