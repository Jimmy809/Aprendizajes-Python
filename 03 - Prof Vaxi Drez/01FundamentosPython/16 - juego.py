from ast import Continue
from timeit import repeat


tablero = ["  " for i in range(9)]

def print_tablero():
    fila1 = "| {} | {} | {} |".format(tablero[0], tablero[1], tablero[2])
    fila2 = "| {} | {} | {} |".format(tablero[3], tablero[4], tablero[5])
    fila3 = "| {} | {} | {} |".format(tablero[6], tablero[7], tablero[8])

    print()
    print(fila1)
    print(fila2)
    print(fila3)
    print()

def jugador_mov(icono):
    if icono == "X":
        numero = 1
    elif icono == "O":
        numero = 2
    print("Tu turno jugador {}".format(numero))
    
    eleccion = int(input("Ingrese su movimiento (1-9): ").strip()) 
     
    # codigo @JimmyReyes     
    if eleccion > 9:
        print('Numero Incorrecto! haz perdido tu turno')
        repeat
    # codigo @JimmyReyes    
        
    elif tablero[eleccion - 1] == "  ":
        tablero[eleccion - 1] = icono
    else:
        print()
        print("Ese espacio esta ocupado")
    
def es_victoria(icono):
    if (tablero[0] == icono and tablero[1] == icono and tablero[2] == icono) or \
       (tablero[3] == icono and tablero[4] == icono and tablero[5] == icono) or \
       (tablero[6] == icono and tablero[7] == icono and tablero[8] == icono) or \
       (tablero[0] == icono and tablero[3] == icono and tablero[6] == icono) or \
       (tablero[1] == icono and tablero[4] == icono and tablero[7] == icono) or \
       (tablero[2] == icono and tablero[5] == icono and tablero[8] == icono) or \
       (tablero[0] == icono and tablero[4] == icono and tablero[8] == icono) or \
       (tablero[2] == icono and tablero[4] == icono and tablero[6] == icono):
        return True
    else:
        return False

def es_empate():
    if "  " not in tablero:
        return True
    else:
        return False

while True:
    print_tablero()
    jugador_mov("X")
    print_tablero()
    if es_victoria("X"):
        print("X es el ganador, felicitaciones")
        break
    elif es_empate():
        print("Esto es empate")
        break
    jugador_mov("O")
    if es_victoria("O"):
        print_tablero()
        print("O es el ganador, felicitaciones")
        break
    elif es_empate():
        print("Esto es empate")
        break