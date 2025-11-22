# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    # Imprimir la parte superior del reloj de arena
    for i in range(m, 0, -2):
        space = (m - i) // 2
        print(" " * space + s * i)
    # Imprimir la parte inferior del reloj de arena
    for i in range(3, m + 1, 2):
        space = (m - i) // 2
        print(" " * space + s * i)
    
    # implementar la lógica para generar el reloj de arena en ASCII
