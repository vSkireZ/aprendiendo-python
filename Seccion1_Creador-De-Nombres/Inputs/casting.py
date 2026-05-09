#input siempre devuelve un string. Si necesitamos otro tipo de dato, debemos hacer un casting.
# Por ejemplo, si queremos pedir la edad, debemos convertir el string a un entero.

# int
edad = int(input("Edad: "))
print(f"En 10 anios tendras {edad + 10}")

# float
precio = float(input("Precio: "))
iva = precio * 0.16
print(f"El precio con IVA es: {precio + iva:.2f}")

#Booleano desde texto
resp = input("Aceptas? (s/n): ")
acepta = resp.lower() == 's'
print(acepta)