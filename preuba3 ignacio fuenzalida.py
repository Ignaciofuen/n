""""
l3=[]
l=[]
l2=[]
def filtro_jugador():

    eplayer=input("Singleplayer o Multiplayer (s/m)?: ")
    arch = open("juegos.csv", "r")
    for linea in arch:
        datos=linea.strip().split(",")
        nombre=datos[0]
        player=int(datos[1])
        
        if eplayer=="s":
            
            if player==1:
                l.append(nombre)
    
        if eplayer=="m":
             if player>1:
                l2.append(nombre)
             
    print(l2[:10])
    print(l[:10])
    arch.close()
def filtro_juego(a,b):
   
    arch = open("juegos.csv", "r")
    
    for linea in arch:
        datos=linea.strip().split(",")

  
        if datos[-2] == a and datos[-1]== b: 
            l3.append(datos[0])
   
    
    arch.close()   
    return(l3)
def guardar_archivo():
    
    print("1.juegos single player")
    print("2.juegos multipleyer")
    print("3.juegos por año y consol")
    op2= input("ingrese opcion")
  
    if op2=="1":
        arch = open("filtro_juegos.txt", "w")
        for dato in l:
            string = dato
            arch.write(string + "\n")
        arch.close()

    
    if op2=="2":
        arch = open("filtro_juegos.txt", "w")
        for dato in l2:
            string = dato
            arch.write(string + "\n")
        arch.close()
    if op2=="3":
        arch = open("filtro_juegos.txt", "w")
        for dato in l3:
            string = dato
            arch.write(string + "\n")
        arch.close()

"""

""""
while True:
    print("\nMenú:")
    print("1. filtro jugador")
    print("2. filtro juego")  
    print("3. Guardar archivos")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        filtro_jugador()
    
    elif opcion == "2":
        nconsola=input("igrese nombre consola")
        inaño=input("año de juego")   
        l_consola=filtro_juego(nconsola,inaño)
        if len (l_consola)== 0:
            print("no se encontro juego")
        else:
            print("juegos encontrados",l_consola[:10])

    elif opcion == "3":
        guardar_archivo()

    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtalo nuevamente.")

"""
l3=[]
l=[]
l2=[]
def registrar_usuario():
    player=input("eliga mododo multiplayer (m) o single player (s)")
    arch =open("juegos.csv","r")
    for linea in arch:
        datos =linea.strip().split(",")
        numero = int(datos[1])
        nombre=datos[0]
        if player == "s" and numero == 1:
            l.append(nombre)
        if player == "m" and numero>1:
            l2.append(nombre)
    arch.close() 
    print(l[:10])
    print(l2[:10])

def filtro_consola():
    nconsola=input("igrese nombre consola")
    año=input("ingrese año de juego")
    arch =open("juegos.csv","r")
    for linea in arch:
        datos =linea.strip().split(",")
        if datos[-2]==nconsola and datos[-1]==año:
            l3.append(datos[0])
    arch.close()
    print(l3[0:10])

def guardar():
    if op2 =="1":
        arch=open("filtro_singleplayer.txt","w")
        for datos in l[:10] :
            string=str(datos)
            arch.write(string+"\n")
        arch.close()
    if op2 =="2":
        arch=open("filtro_multiplayer.txt","w")
        for datos in l2[:10] :
            string=str(datos)
            arch.write(string+"\n")
        arch.close()
    if op2 =="3":
        arch=open("filtro_consola.txt","w")
        for datos in l3[:10] :
            string=str(datos)
            arch.write(string+"\n")
        arch.close()

while True :
    print("\nMenú:")
    print("1. registrar")
    print("2. filtro consola")
    print("3. guardar")
    print("4. salir ")
    op= input("ingrese opcion")

    if op == "1":
        registrar_usuario()
    elif op == "2":
        filtro_consola()

    elif op == "3" :
        print("elegir que ruta va desplegar")
        print("1.juegos sigleplayer")
        print("2.juegos multipleyer")
        print("3.juegos consola año")
        op2=input("ingrese opcion")
        guardar()
    elif op == "4":
        print("adios")
        break












