from datetime import datetime
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

    if fecha[MINUTO_LIMITE] >= 60:

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

        

def leerHorarios(archivo):

    fechaHoyEncontrada = False
    lineas = archivo.readlines()
    i = 0

    while(i < len(lineas) and not fechaHoyEncontrada):

        try:
            linea = str(lineas[i].strip("\n"))
            fecha = datetime.strptime(linea,"%d/%m/%Y").strftime("%d/%m/%Y")
            fechaHoy = datetime.now().strftime('%d/%m/%Y')
            
            if fecha == fechaHoy:
               print(f'El día de hoy {fechaHoy} las actividades son las siguientes:\n')
               print(f'{lineas[i + 2]}')
               print(f'{lineas[i + 3]}')
               fechaHoyEncontrada = True
        
        except:
            continue

        finally:
            i += 1
        
    return fechaHoyEncontrada
        



def main():

    with open("agenda.txt", "r") as archivo:
        fechaHoyEncontrada = leerHorarios(archivo)

    if not fechaHoyEncontrada:
        with open("agenda.txt", "a") as archivo:

            actividades = {}
            pedirActividades(actividades)
            definirHorarios(actividades) 

            fechaHoy = datetime.now().strftime('%d/%m/%Y') + "\n"
            archivo.write(fechaHoy)
            archivo.write("----------------------------------------------------------------\n")

            for key, value in actividades.items():
                lineaAEscribir = key + " de "
                lineaAEscribir += str(value[0]) + ":" + str(value[1]) + " a " + str(value[2]) + ":" + str(value[3])
                lineaAEscribir += "\n"

                archivo.write(lineaAEscribir)
                
                archivo.write("\n\n")

        

main()