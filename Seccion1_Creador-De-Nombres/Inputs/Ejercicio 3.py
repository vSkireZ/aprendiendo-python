#Ejercicio 3 - Suma de N numeros

# - Pedir cuantos numeros sumar
# - Validar que sea entero positivo con isdigit
# - Con un bucle pedir cada numero en una linea separada
# - Acumular la suma
# - Imprimir resultado
# - Validar cada numero con try/except

while True:
    numeros_a_sumar = input("Ingresa la cantidad de numeros a sumar: ")
    if numeros_a_sumar.isdigit():
        numeros_a_sumar = int(numeros_a_sumar)
        print(f"{numeros_a_sumar} numeros.\n")
        break
    print("Ingresa un dato correcto.\n")

suma = 0

#Para este ejercicio investigue como podria usar for ya que no lo habia visto aun.

for i in range(numeros_a_sumar):
    while True:
        try:
            numero = input(f"Numero {i  + 1} >> ")
            numero = int(numero)
            suma += numero
            break
        except ValueError:
            print("Solo numeros, intenta de nuevo.\n")

print(f"\nLa suma final es: {suma}")



