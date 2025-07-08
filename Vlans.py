# vlan_checker.py
while True:
    entrada = input("Ingrese el número de VLAN (o 's' para salir): ")
    if entrada.lower() == 's':
        break
    try:
        vlan = int(entrada)
        if 1 <= vlan <= 1005:
            print(f"VLAN {vlan} es del tipo NORMAL.")
        elif 1006 <= vlan <= 4094:
            print(f"VLAN {vlan} es del tipo EXTENDIDA.")
        else:
            print("Número de VLAN fuera del rango válido (1-4094).")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
