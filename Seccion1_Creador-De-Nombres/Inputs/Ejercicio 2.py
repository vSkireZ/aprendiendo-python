# Ejercicio 2 - Registro de usuario

# - Pedir nombre, apellido y ciudad
# - Normalizar todo con strip y title
# - Pedir edad con while true
# - Imprimir resumen con todos los datos

nombre = input("Ingresa tu nombre\n>> ").strip().title()
apellido = input("Ingresa tu apellido\n>> ").strip().title()
ciudad = input("Ingresa tu ciudad\n>> ").strip().title()

while True:
    edad_str = (input("Ingresa tu edad: "))
    if edad_str.isdigit():
        edad = int(edad_str)
        break
    print("Ingresa datos validos.\n")

print(f"\nNombre:\t\t {nombre} \nApellido:\t {apellido} \nCiudad:\t\t {ciudad} \nEdad:\t\t {edad}")
