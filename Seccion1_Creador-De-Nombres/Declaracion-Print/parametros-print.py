#Parámetro sep= define qué va entre los valores
#Por defecto es un espacio " "

print("a", "b", "c") # -> a b c
print("a", "b", "c", sep="-") # -> a-b-c
print("a", "b", "c", sep="") # -> abc
print("a", "b", "c", sep=" | ") # -> a | b | c
print("a", "b", "c", sep="\n") # -> cada valor en su propia linea \n es el caracter de escape para salto de linea

#Parámetro end= define qué va al final de cada print

