import requests as req
# import socket , time

url = "https://api.qrcode-monkey.com//qr/custom" #Link a monkeyQR

# Datos para el diccionario, link del arbol y su respectiva coordenada
data = "https://es.wikipedia.org/wiki/Árbol#/media/Archivo:Eiche_bei_Graditz.jpg" #Editar URL deseado
coor = 1 #Posicion de la corrdenada del arbol

data_base = {} #Diccionario de las paginas(datos) de los arboles

data_base[coor]= data #Ejemplo de dato del diccionario

for i in data_base: #para recorrer la lista 
    # Atributos de MonkeyQR para editar QR
    payload = {"data":data_base[i],"config":{"body":"square","eye":"frame13","eyeBall":"ball14","erf1":[],"erf2":[],
                                            "erf3":[],"brf1":[],"brf2":[],"brf3":[],"bodyColor":"#000000","bgColor":"#FFFFFF",
                                            "eye1Color":"#021326","eye2Color":"#021326","eye3Color":"#021326","eyeBall1Color":"#074f03",
                                            "eyeBall2Color":"#074f03","eyeBall3Color":"#074f03","gradientColor1":"#12a637","gradientColor2":"#0b509e",
                                            "gradientType":"linear","gradientOnEyes":"true","logo":"","logoMode":"default"},
                                            "size":1000,"download":"imageUrl","file":"png"}
    resp = req.post(url ,json=payload) #Configuracion de peticion para API de monkeyQR

    if resp.status_code == 200 : #Si salio correcto, genera QR y lo descarga
        OutPut = resp.json()
        Link = OutPut.get('imageUrl')
        Link = "http:" + Link
        response = req.get(Link)

        svnm = f"Arbol_{i}.png" #Editar nombre de archivo

        file = open(svnm, "wb") #Abrir un archivo para crear el QR
        file.write(response.content)
        file.close()
        print(f"Imagen generado: {svnm}") #Mensaje de imagen
    else:
        print("Error ",resp.status_code) #error si no se conecto a la API
