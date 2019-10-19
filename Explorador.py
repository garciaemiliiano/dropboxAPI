import os
from os import getcwd
from scandir import scandir
from os.path import abspath

##Intento para que solo suba una extension de archivos. O todos menos un formato, o algunos.
def estaEnCarpeta(extensionParam,listaCarpeta):
    for extension in listaCarpeta:
        if extension == extensionParam:
            return True;
    return False;

def solamenteExtension(nombreArchivo):
    cont = 0
    for letra in nombreArchivo:
        if letra == ".":
            return cont
        cont +=1

def archivosEnCarpeta(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

lista_arq = archivosEnCarpeta() 
ext=[]
listaExtensiones = [".jpg",".gif",".bmp",".jpeg",".png"]

name = "jp.jpeg"
a=""
for i in range (solamenteExtension(name),len(name)):
    a= a+name[i]

for extension in listaExtensiones:
    if (a == extension):
        print(a)