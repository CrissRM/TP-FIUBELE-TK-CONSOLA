import operator
def leer_Archivo(archivo):
    linea = archivo.readline()
    if linea !="":
        respuesta=linea.rstrip('\n').split(' ') 
    else :
        respuesta=""
    return respuesta

def grabar_Nuevo(archivo,palabra,c1,c2,c3):
    archivo.write(str(palabra) + ',' + str(c1) +","+ str(c2) +","+ str(c3) +'\n')

palabras={}
def analizador_palabras_texto1(texto1):
    palabra=leer_Archivo(texto1)
    while (palabra !=""):
        for i in palabra :
            if (i.isalpha()) and (i!="") and (len(i)==7):
                if i.lower() in palabras:
                    palabras[i.lower()][0]+=1
                else :
                    palabras.setdefault(i.lower(),[1,0,0])
        palabra=leer_Archivo(texto1)


def analizador_palabras_texto2(texto2):
    palabra=leer_Archivo(texto2)
    while (palabra !=""):
        for i in palabra :
            if (i.isalpha()) and (i!="") and (len(i)==7) :
                if i.lower() in palabras:
                    palabras[i.lower()][1]+=1
                else:
                    palabras.setdefault(i.lower(),[0,1,0])
        palabra=leer_Archivo(texto2)
    
   

def analizador_palabras_texto3(texto3):
    palabras_texto3={}
    palabra=leer_Archivo(texto3)
    while (palabra !=""):
        for i in palabra :
            if (i.isalpha()) and (i!="") and (len(i)==7) :
                if i.lower() in palabras_texto3:
                    palabras[i.lower()][2]+=1
                else :
                    palabras.setdefault(i.lower(),[0,0,1])
        palabra=leer_Archivo(texto3)

def ordenar_palabras(texto4):
    palabras_ordenadas=sorted(palabras.items(),key=operator.itemgetter(0))
    for elementos in palabras_ordenadas:
        grabar_Nuevo(texto4,elementos[0],elementos[1][0],elementos[1][1],elementos[1][2])
    return palabras_ordenadas

texto1=open("Cuentos.csv","r")
texto2=open("La araña negra - tomo 1.csv","r")
texto3=open("Las 1000 Noches y 1 Noche.csv","r")
texto4=open("FIUBLE/InterfazGrafica/jugadores.csv","w")
# texto4=open("palabras.csv","w")
analizador_palabras_texto1(texto1)
analizador_palabras_texto2(texto2)
analizador_palabras_texto3(texto3)
ordenar_palabras(texto4)
texto1.close()
texto2.close()
texto3.close()
texto4.close()


