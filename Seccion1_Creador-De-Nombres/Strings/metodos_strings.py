#Metodos mas usados

#upper
print("hola".upper()) # "HOLA"

#lower
print("HOLA".lower()) # "hola"

#strip: Elimina los espacios en blanco al inicio y al final de la cadena
print("   Hola Miguel   ".strip()) # "Hola Miguel"

#replace: Reemplaza una subcadena por otra
print("Hola Miguel".replace("Hola", "Adios"))

#split: Divide una cadena en una lista de subcadenas utilizando un separador
print("a,b,c".split(","))

#find: Devuelve el indice de donde aparece el caracter, o -1 si no se encuentra
print("hola".find("o")) # 1

#count: Cuenta cuantas veces aparece una subcadena en la cadena
print("banana".count("a")) # 3

#startswith: Devuelve True si la cadena empieza con la subcadena dada
print("hola".startswith("ho")) # True
print("hola".startswith("la")) # False

#endswith: Devuelve True si la cadena termina con la subcadena dada
print("hola".endswith("la")) # True
print("hola".endswith("ho")) # False

#Slicing: Permite obtener una subcadena a partir de un rango de indices
texto = "Python"
print(texto[0]) # "P"
print(texto[-1]) # "n"
print(texto[0:3]) # "Pyt"
print(texto[2:]) # "thon"
print(texto[::-1]) # "nohtyP" (invierte la cadena)
print(len(texto)) # 6 (longitud de la cadena)

