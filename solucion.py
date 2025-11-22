# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    # imprimir reloj de arena
    for i in range(row, 0, -1):
        for j in range(row - i):
            print(" ", end="")
        for k in range(1, i * 2):
            print(s, end="")
        print()
    # parte inferior
    for i in range(2, row + 1):
        for j in range(row - i):
            print(" ", end="")
        for k in range(1, i * 2):
            print(s, end="")
        print()
    
    # implementar la lógica para generar el reloj de arena en ASCII
