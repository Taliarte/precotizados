# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import pandas as pd


def obtener_total_desde_csv(edad):
    # Leer el archivo CSV y crear el dataframe
    df = pd.read_csv('datosVidaTemporal.csv', sep=';')

    # Buscar la fila correspondiente a la edad ingresada
    fila = df.loc[df['Edad'] == edad]

    # Verificar si se encontró una coincidencia
    if len(fila) > 0:
        total = fila['Total'].values[0]
        return total
    else:
        return "La edad ingresada no se encontró en el archivo CSV"


# Ejemplo de uso:
edad = int(input("Ingrese una edad: "))
total = obtener_total_desde_csv(edad)
print("El valor de la columna Total para la edad", edad, "es", total)
