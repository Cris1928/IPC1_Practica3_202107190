from operator import itemgetter
from poplib import POP3_PORT
import random
import os
vectormov=[]
vectornom=[]
rev=[]
diccionario={}
while True :
    
    print("\n PACMAN - IPC 1 - 2022")
    print("----------------------")
    print("1.       iniciar juego")
    print("2. tabla de posiciones")
    print("3.               salir")
    print("----------------------")
    print("")
    try:
        entrada = int(input("ingrese la opcion: "))
    except (ValueError, TypeError, IndexError):
        print("tiene que ingresar un valor numerico")

    if(entrada==1):
        nombre=input("Ingrese su nombre: ")
        vectornom.append(nombre)

                    
        def creatablero(fil,col,val):
            tablero=[]
            comida=[]
            numero=0
            for i in range(fil):
                tablero.append([])
                for j in range(col):
                    tablero[i].append(val)
            return tablero

        def muestratablero(tablero):
            comida=[]
            numero=0
            print("• • • • • • • • • • • •")
            for fila in tablero:
                print("•",end=" ")
                for elem in fila:
                    print(elem, end=" ")
                print("•")
            print("• • • • • • • • • • • •")
 


        
        def menu():
            
            opcion = input("ingese el movimiento")
            return opcion
        
        
        columnas= 10
        movimientos=0
        filas=10
        contador=0
        ncomida=((filas)*(columnas)*0.4)
        cantidadcomida=random.randint(1,ncomida)
        comidatotal=cantidadcomida
        comidaobtenida=0
        nparedes=((filas)*(columnas)*0.3)
        cantidadparedes=random.randint(1,nparedes)
        contadornom=0
        comida=[]
        paredes=[]
        numero=0
        numero2=0
        visible=creatablero(filas, columnas," ")
        


        y= random.randint(0,columnas-1)
        x=random.randint(0,filas-1)
        real= visible[x][y]
        if visible[x][y] != "@" and visible[x][y] != "#" :
            visible[x][y]="c"
       
       
        while numero < cantidadcomida:
            p= random.randint(0,columnas-1)
            q=random.randint(0,filas-1)
            if visible[p][q] != "c" and visible[p][q] != "#" and visible[p][q] != "@":
                visible[p][q]="@"
                numero +=1
                comida.append((p,q))




        while numero2 < cantidadparedes:
            m= random.randint(0,columnas-1)
            n=random.randint(0,filas-1)
            if visible[m][n] != "c" and visible[m][n] != "@" and visible[m][n] != "#":
                visible[m][n]="#"
                numero2 +=1
                paredes.append((m,n))
        
        



        os.system("cls")
        muestratablero(visible)
       
        jugando=True
        
        
        
        while jugando:
            
            print("cantidad de comida obtenida: ",comidaobtenida)
            print("cantidad de comida restatnte: ",comidatotal)
            print(movimientos," movimientos")
            print("puntos: ",contador)
            
            mov=input("\nIngese el movimiento: ")
            
            
            
            
            if mov =="w" or  mov=="8":
                
                if x==0 :
                    x=0
                    real=visible[x][y]
                    visible[x][y]="c"
                    
                    movimientos+=0
                

                else:
                    visible[x][y]=real
                    x-=1
                    real=visible[x][y]
                    visible[x][y]="c"
                    visible[x+1][y]=" "
                    movimientos+=1
                 
                    
            elif mov =="s" or mov=="5":
                if x==filas-1:
                    x=filas-1
                    real=visible[x][y]
                    visible[x][y]="c"
                    movimientos+=0
                else:
                    visible[x][y]=real
                    x+=1
                    real=visible[x][y]
                    visible[x][y]="c"
                    visible[x-1][y]=" "
                    movimientos+=1

                    
                 
            elif mov =="d" or mov=="6":
                if y==columnas-1:
                    y=columnas-1
                    real=visible[x][y]
                    visible[x][y]="c"
                    
                    movimientos+=0
                else:
                    visible[x][y]=real
                    y+=1
                    real=visible[x][y]
                    visible[x][y]="c"
                    visible[x][y-1]=" "
                    movimientos+=1

            elif mov =="a" or mov=="4":
                if y==0:
                    y=0
                    real=visible[x][y]
                    visible[x][y]="c"
                    movimientos+=0
                else:
                    visible[x][y]=real
                    y-=1
                    real=visible[x][y]
                    visible[x][y]="c"
                    visible[x][y+1]=" "
                    movimientos+=1

            if mov =="e":
                vectormov.append(movimientos)
                diccionario[nombre]=movimientos
                print("has finalizado la partida")
                break
            
                

            if mov =="s"  and real == "#":
                visible[x][y]=real
                x-=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1
            
            if mov =="5"  and real == "#":
                visible[x][y]=real
                x-=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1




                
            if mov =="w" and real == "#":
                visible[x][y]=real
                x+=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1
            
            if mov =="8" and real == "#":
                visible[x][y]=real
                x+=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1
                

                    
            if mov =="a" and real == "#":
                visible[x][y]=real
                y+=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1

            if mov =="4" and real == "#":
                visible[x][y]=real
                y+=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1
                
            elif mov =="d" and real == "#":
                visible[x][y]=real
                y-=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1

            elif mov =="6" and real == "#":
                visible[x][y]=real
                y-=1
                real=visible[x][y]
                visible[x][y]="c"
                movimientos-=1
           

            
            if real != "@":
                contador +=0
            else:
                contador +=5
                comidatotal-=1
                comidaobtenida+=1
                
            if contador==40 or comidatotal==0:
                print("\nganaste :)")
                vectormov.append(movimientos)
                diccionario[nombre]=movimientos
                break
            os.system("cls")
            muestratablero(visible)

         
    elif(entrada==2):
        
        print("__________________________")
        print("\n Tabla de posiciones\n")
        vectormov.sort(reverse=True)
        #convierto el diccionario a una lista ya desendente
        ddd=sorted(diccionario.items(), key=itemgetter(1),reverse = True)
        de=ddd[0:3]
        #convierto el diccionario a otro diccionario pero ya ordenado (no fue utilizado)
        descent=dict(sorted(diccionario.items(), key=itemgetter(1),reverse = True))
        t=descent.items()
        for clave,valor in de:
            print("{0} = {1}".format(clave,valor))
        print(" ")
        print("__________________________")
        
    elif(entrada==3):
        print("\nfin del programa")
        break
    else:
        print("\n es opcion no existe")
    

