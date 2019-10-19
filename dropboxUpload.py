import dropbox #Importamos API Dropbox

class DropboxUploader:


    def filesUploaderDropbox(): #Funcion que sube archivos.
        nArchiv = input("Ingrese el nombre del archivo ")
        ex = [".jpg",".gif",".bmp",".jpeg",".png"]
        print (ex)
        extensionElegida = int(input("Ingrese con numeros el tipo de extension de su imagen "))
        nombreDelArchivo = nArchiv + ex[extensionElegida-1] #Nombre final.
        archivoNube = "/DropboxPython/"+nombreDelArchivo #Direccion en la carpeta de dropbox a donde se va a guardar.
        abrirArchivo = open(nombreDelArchivo,'rb').read() #Lee el archivo.
        clienteDropbox = dropbox.Dropbox('AcessToken') #Token de seguridad que confirma al usuario.
        clienteDropbox.files_upload(abrirArchivo,archivoNube) #Metodo que sube los archivos, toma la lectura de un archivo y la direccion a donde se guardara en la nube.


if __name__ == "__main__":
    DropboxUploader.filesUploaderDropbox()


