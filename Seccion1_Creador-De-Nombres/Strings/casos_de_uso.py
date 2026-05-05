#upper y lower
#Comparar sin importar mayusculas o minusculas

usuario = "MIGUEL"
if usuario.lower() == "miguel":
    print("Bienvenido")

#strip
#Limpiar lo que escribe el usuario en un formulario

nombre = "   Miguel   "
print(nombre.strip()) # "Miguel"

#replace
#Censurar palabras o corregir texto

mensaje = "Hola mundo cruel"
print(mensaje.replace("cruel", "bonito")) # "Hola mundo bonito"

#split
#Separar un CSV o datos que vienen juntos

datos = "Miguel,21,Estudiante"
lista = datos.split(",") # ["Miguel", "21", "Estudiante"]

#find
#Saber si un texto contiene algo y donde

email = "ejemplo@outlook.com"
print(email.find("@")) # 7

#count
#Contar vocales, letras, o palabras repetidas

texto = "banana"
print(texto.count("a")) # 3

#startswith y endswith
#Validar extensiones de archivo o prefijos

archivo = "documento.pdf"
if archivo.endswith(".pdf"):
    print("Es un archivo PDF")

