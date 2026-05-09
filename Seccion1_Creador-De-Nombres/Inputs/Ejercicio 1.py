# Ejercicio 1 - Calculadora de propina

# - Pedir al usuario el total de la cuenta
# - Pedir al usuario el porcentaje de propina que desea dejar
# - Calcular el monto de la propina y el total a pagar
# - Usar try/except para validar que los inputs sean numeros


while True:
    try:
        total_cuenta = input("Ingrese el total de la cuenta\n>> ")
        total_cuenta = float(total_cuenta)
        break
    except ValueError:
        print("Solo numeros, intentalo de nuevo.\n")

while True:
    try:
        propina = input("Ingrese el % de propina a dejar (5, 10, 15, 20...)\n>> ")
        propina = float(propina) / 100
        break
    except ValueError:
        print("Solo numeros, intentalo de nuevo.\n")


calculo_propina = total_cuenta * propina
print(f"Propina: {calculo_propina:.2f}$\nTotal a pagar: {total_cuenta + calculo_propina:.2f}")