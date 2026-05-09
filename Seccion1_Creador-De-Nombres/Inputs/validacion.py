#Pedir hasta que el input sea valido

while True:
    edad_str = input("Edad: ")
    if edad_str.isdigit(): #isdigit devuelve True si todos los caracteres son digitos (0-9), False si hay otra cosa.
        edad = int(edad_str)
        print(f"Tienes {edad} anios.")
        break
    print("Solo numeros, intenta de nuevo.")

#Validar con try/except
try:
    precio = float(input("Precio: "))
    print(f"El precio es: {precio:.2f}")
except ValueError:
    print("Valor no valido, se esperaba un numero.")


#Normalizar texto (quitar espacios, lowercase)
ciudad = input("Ciudad: ").strip().title()
print(f"Ciudad: {ciudad}") # "  guadalajara  " -> "Guadalajara"



#Varios valores en una linea - avanzado
a, b = input("Ingresa dos numeros separados por espacio: ").split()
a, b = int(a), int(b)
print(f"{a} + {b} = {a + b}")


#Truco: input() como pausa del programa

print("Programa terminado.")
input("Presiona Enter para salir...")
