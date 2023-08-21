from datetime import date, time, datetime
from random import randint, seed, randrange

VACIO = ""

def intConvertor(lista : list) -> None:

    for i in range(len(lista)):

        try:
            lista[i] = int(lista[i])

        except:

            raise Exception("Algo salio mal")
        


def pedirActividades(actividades:dict) -> None:

    actividadActual = VACIO

    while(True):

        actividadActual = input("Hola Nicolás, que actividades tenés hoy? (0 para indicar que ya no hay más)")
        
        if actividadActual != "0":
            actividades.update({actividadActual: []})
        
        else:
            break
    

def randomizarHorario(fecha):
    fecha[0] = randrange(14, 20)
    #fecha[0] = randrange(fecha[0], 20)
    fecha[1] = randrange(0, 60)


#parsear cuando queda un minuto menor a 10
def parsearHorario(fecha, usuario):
    
    fecha[1] += usuario

    while fecha[1] >= 60:
        fecha[1] -= 60
        fecha[0] += 1
    
    

def definirHorarios(actividades):

    for key, value in actividades.items():

        fecha = datetime.now().strftime('%H:%M:%S').split(":")
        intConvertor(fecha)
        randomizarHorario(fecha)
        actividades[key] = fecha


def imprimirHorarios(actividades):
    
    for key, value in actividades.items():

        preferenciaUsuario = int(input(f'¿Cuanto minutos quieres trabajar en {key}?'))
        horarioParseado = value.copy() 
        parsearHorario(horarioParseado, preferenciaUsuario)
        print(f'{key} de {value[0]}:{value[1]} a {horarioParseado[0]}:{horarioParseado[1]}')

def main():
    fechaHoy = datetime.now().strftime('%H:%M:%S')

    actividades = {}
    pedirActividades(actividades)
    definirHorarios(actividades)
    imprimirHorarios(actividades)

    with open("agenda.txt", "w") as archivo:
        
        for key, value in actividades.items():
            archivo.write(fechaHoy)
        


main()