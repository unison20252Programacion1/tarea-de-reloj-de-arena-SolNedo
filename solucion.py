# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        return "Error: La altura debe ser un entero positivo"
    lines = []
    # Parte superior
    for i in range(m, 0, -2):
        space = (m - i) // 2
        lines.append(" " * space + s * i)
    # Parte inferior
    for i in range(2 if m % 2 == 0 else 3, m + 1, 2):
        space = (m - i) // 2
        lines.append(" " * space + s * i)
    return "\n".join(lines)
    
    # implementar la lógica para generar el reloj de arena en ASCII
