from datetime import date, time, datetime
from random import randrange

VACIO = ""
ACTIVIADES_REGULARES = ["Gimnasio", "Estudiar"]
HORA_INICIO = 0
MINUTO_INICIO = 1
HORA_LIMITE = 2
MINUTO_LIMITE = 3

def intConvertor(lista : list) -> None:

    for i in range(len(lista)):

        try:
            lista[i] = int(lista[i])

        except:
            raise Exception("Algo salio mal")
        


def pedirActividades(actividades: dict) -> None:

    for i in range(len(ACTIVIADES_REGULARES)):

        print(f'Hoy vas a realizar la actividad {ACTIVIADES_REGULARES[i]}? (1 para decir que si)')
        desicionUsuario = input()

        try:
            desicionUsuario = int(desicionUsuario)

            if desicionUsuario == 1:
                actividades.update({ACTIVIADES_REGULARES[i]: []})

        except ValueError:
            continue
        

    actividadActual = VACIO

    while(True):

        actividadActual = input("Hola Nicolás, tenés alguna otra actividad extra? (0 para indicar que ya no hay más)")
        
        if actividadActual != "0":
            actividades.update({actividadActual: []})
        
        else:
            break
    

def randomizarHorario(fecha):

    fecha[0] = randrange(fecha[0], 20)
    fecha[1] = randrange(0, 60)



def parsearHorario(fecha, usuario):
    
    fecha.append(fecha[HORA_INICIO])
    fecha.append(fecha[MINUTO_INICIO])
    fecha[MINUTO_LIMITE] += usuario

    while fecha[MINUTO_LIMITE] >= 60:
        fecha[MINUTO_LIMITE] -= 60
        fecha[HORA_LIMITE] += 1
    
    

def definirHorarios(actividades):

    for key, value in actividades.items():

        fecha = datetime.now().strftime('%H:%M').split(":")
        intConvertor(fecha)
        randomizarHorario(fecha)

        preferenciaUsuario = int(input(f'¿Cuanto minutos quieres trabajar en {key}?')) 
        parsearHorario(fecha, preferenciaUsuario)

        actividades[key] = fecha

        

def main():

    actividades = {}
    pedirActividades(actividades)
    definirHorarios(actividades)

    for key, value in actividades.items():

        print(f'{key} de {value[0]}:{value[1]} a {value[2]}:{value[3]}')

    with open("agenda.txt", "a") as archivo:
        
        fechaHoy = datetime.now().strftime('%d/%m/%Y') + "\n----------------------------------------------------------------\n"
        archivo.write(fechaHoy)

        for key, value in actividades.items():
            lineaAEscribir = key + "->"
            lineaAEscribir += str(value[0]) + ":" + str(value[1])
            lineaAEscribir += "\n"

            archivo.write(lineaAEscribir)
        
        archivo.write("\n\n")
        


main()