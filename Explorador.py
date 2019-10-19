import os
from os import getcwd
from scandir import scandir
from os.path import abspath

##Intento para que solo suba una extension de archivos. O todos menos un formato, o algunos.
def estaEnCarpeta(extensionParam,listaCarpeta):
    for extension in listaCarpeta:
        if extension == extensionParam:
            return true;
    return false;

def solamenteExtension(nombreArchivo):
    nueva = ""
    for letra in nombreArchivo:
        nueva = letra + nueva
    n=""
    for letra in nueva:
        while letra != ".":
            n=n+letra
    return n


def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

lista_arq = ls() 
ext=[]
listaExtensiones = [".jpg",".gif",".bmp",".jpeg",".png"]

for extensiones in listaExtensiones:
    if (extensiones,lista_arq):
        ext.append(extensiones)

print(solamenteExtension('jp.jpeg'))
