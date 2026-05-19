#Crear variables
nombre = "Maria"
edad = 25
precio = 99.99
activo = True
colores = ["rojo", "verde", "azul"]

#Usar las variables
print(nombre)
print(edad)
print(precio)
print(activo)
print(colores)

#Puedes cambiar el valor de una variable en cualquier momento
puntos = 100
print(puntos)
puntos = 150
print(puntos)

#Actualizar con operaciones
contador = 0
print(contador)

contador = contador + 1
print(contador)

contador += 1
print(contador)


#Asignar varios valores a varias variables
x,y,z = 1,2,3
print(x,y,z)

#Asignar el mismo valor a varias variables
a = b = c = 0
print(a,b,c)

#Intercambiar valores
x, y = y, x
print(x, y)

#Mostrar variables junto con texto
nombre = "Carlos"
edad = 30

print("Hola", nombre, "tienes", edad, "anios")

#Operaciones matematicas usando variables
precio = 100
cantidad = 5
descuento = 0.10

subtotal = precio * cantidad
print("Subtotal: ", subtotal)

ahorro = subtotal * descuento
print("Ahorro: ", ahorro)

total = subtotal - ahorro
print("Total:", total)

#Variables con input
nombre = input("Como te llamas? ")
print("Hola", nombre + "!")
#fstrings
print(f"Hola {nombre}!")