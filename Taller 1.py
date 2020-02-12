# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:43:10 2020

@author: CATALINA ALVEAR 0118002
"""

# 1. Sin utilizar el comando abs, escribir un programa que calcule e imprima
# el valor absoluto de cualquier número (sea entero o decimal)
 
try: #usamos try por si se ingresa un numero que no es entero ni decimal
    
   #Definimos variables   
   va = input('Digite un número para calcular su valor absoluto: ')
            
   if '.' in va:
       vabs=float(va) #¨Para los decimales
       
   else:
       vabs=int(va) # Para los enteros
       
   if vabs<0:
       vabs=vabs*-1 #para los negativos
               
   print('El valor absoluto es: ', vabs)
           
except:
   print('Intente de nuevo, el número ingresado no es válido')
        
    
#%% 2. Leer dos numeros enteros y determinar si la magnitud de la diferencia
# entre los dos numeros es un primo

try: #Por si digitan un número que no es entero
    #Definimos variables
    n1=int(input('\n Digite un numero entero: \n'))
    n2=int(input('\n Digite otro entero: \n'))

    ##Definimos la funcion
    def np(n):
        print('\n Números primos \n')
        for i in range(2,n):
            if n%i==0: #Para determinar qué número es primo
                return False
        return True

    dif=abs(n1-n2) #diferencia entre cada número

    if np(dif):
        print ('\n La diferencia entre los números es: ',dif,' y es primo')
    else:
        print ('\n La diferencia entre los números es: ',dif,' y no es primo')
except:
    print('\n Intente de nuevo, los números ingresados no son válidos \n')

#%%3. iterar entre los primeros 100 numeros positivos, buscando los primeros 15 
#     multiplos de 3
# Continuar con los multiplos de 4 

#definimos variables
m3 = [] #Multiplos de 3
m4 = [] #Multiplos de 4
marcador = 0 #Agrega los multiplos

for i in range(1,101):
    
    if len(m3)<15:
        
        if i%3 == 0:
            m3.append(i) #Multiplos de 3
            marcador += 1
            
    if marcador > 14:
        
        if i%4 == 0:
            m4.append(i) #Multiplos de 4
            
print('\n Primeros 15 multiplos de 3: \n',m3)
print('\n Los 15 multiplos de 4, después de los 15 multiplos de 3: \n',m4)

    
#%% 4.  Programa que lee las coordenadas del centro de dos circunferencia y su
# radio. Ademas determina si un punto se encuentra contenido por estas

try: # Por si ingresan coordenadas que no son números enteros
    #Definimos las variables (x,y)
    x = float(input('Escriba la coordenada en el eje x: '))
    y = float(input('Escriba la coordenada en el eje y: '))
    
    marcador = 0 ##Esta variable nos cuenta dentro de cuantas circunferencias
                  #esta

    def circunferencia(n):
          print('\n Centro y radio de la circunferencia \n')
        
         #Datos de la circunferencia
        cx=float(input(f'Escriba la coordenada en el eje x del centro de la {n} \
circunferencia: '))
        cy=float(input(f'Escriba la coordenada en el eje x del centro de la {n} \
circunferencia: '))
        r=float(input(f'Digite el radio de la {n} circunferencia: '))
    
        c1=cy+((r**2)-(x-cx)**2)**0.5 #circunferencia 1
        c2=cy-((r**2)-(x-cx)**2)**0.5 #cicunferencia 2
        
        ##Si la x no esta dentro de la circunferencia 1 y la circunferencia 2
        #dan resultado complejo
        
        try: #Para que no se incluyan variables complejas
            if y<=c1 and y>=c2:
                global marcador
                global indet
            
                indet=n ##Esta variable servira para determinar dentro de que 
                #circunferencia esta el punto
                marcador +=1
        except:
            return False
            
            
    circunferencia('primera')
    circunferencia('segunda')
    
    ##Salida de resultados
    if marcador==2:
        print('\nEl punto se intercepta en las dos circunferencias')
    elif count==1:
        print('\nEl punto se intercepta en la ',indet,' circunferencia')
    else:
        print('\nEl punto no se intercepta en las dos circunferencias')
        
except:
    print('\n Intente de nuevo, los números ingresados no son válidos \n')


#%%5 Programa que recibe una cadena de texto y calcula cuantas:
    ##a Vocales mayusculas tiene
    ##b Cuantas letras con tilde tiene
    ##c Cuantos digitos tiene
    ##d Cuantos espacios tiene
    ##e Cuantas palabras reservadas tiene

c = input('Escriba una cadena de texto: ')
mayus = 'AEIOU'
tilde = 'áéíóúÁÉÍÓÚ'
dig = '0123456789'
esp = ' '
pres = ['print','in','finall','def','yield','import','excec','continue','while'\
,'exceptor','class','try','not','global','break','return','lambda','from','elif'\
,'else','if','assert','raise','is','for','del','and']

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0

for i in range(len(c)):
    if c[i] in mayus:
        a1 += 1
    elif c[i] in tilde:
        a2 += 1
    elif c[i] in dig:
        a3 += 1 
    elif c[i] in esp:
        a4 += 1

print('En la cadena de texto hay ',a1,' vocal(es) en mayuscula')
print('En la cadena de texto hay ',a2,' tilde(s)')
print('En la cadena de texto hay ',a3,' digito(s)')
print('En la cadena de texto hay ',a4,' espacio(s)')

a = c.split()
print(a)


#for n, i in enumerate(a):
#    if i in pres:
#        a5 += 1
#print('En la cadena de texto hay ',a5,' palabra(s) reservada(s)')

#%% 6 Leer una cadena de texto y organizarla alfabeticamente

##Condiciones iniciales
i=0
execution=True ##Mantiene la ejecucion
order=[]
digits=['1','2','3','4','5','6','7','8','9','0']

##Entrada de datos
string=input('Introduzca un texto: ').lower()

##Busca digitos dentro del texto para generar una excepcion
while i<len(digits):
    if digits[i] in string:
        execution=False
    i+=1
    
##Mi version del try except
if execution:
    for n in string:
        if n.isspace()==False:
            order.append(n)
    order.sort()
    
    ##Salida de datos
    print('\nEl texto ordenado alfabeticamente (en minusculas) sin espacios es'\
,''.join(order))
else:
    ##Except
    print('\nHa ocurrido un error, No introduzca numeros')

#%% 7.  
a == True
while a == True:
    lista =[]
    cn = int(input('Mencione una cantidad de números para la lista: '))
    for m in range(cn):
        lista.append(float(input(f'Escriba el número {m+1}: ')))
    print('La lista es: ', lista)
    for i in lista:
        if i > 0:
            a = False
            add = float(input('Ingrese un número para añadirlo a la lista en\
su posición correspondiente'))
            lista.append(add)
            lista.sort()
            print('La lista resultante es: ', lista)
            break
        else:
            print('Esta lista no es válida, intente de nuevo')
            
#%% 8 Leer una lista de números enteros y determinar cual es el segundo elemento
# mayor de dicha lista.       

s = ('El segundo elemento mayor de la lista')

lista = eval(input('Digite una lista con números enteros: '))
mx = max(lista)
lista.remove(mx)

mx2 = max(lista)
print('El segundo elemento mayor de la lista es: ', mx2)
        

#%% 9 Escribir un programa que calcule términos de la sucesión 
#  Un+1 = 3 Un + 1 si Un es impar y U n+1 = Un / 2 si Un es par

try:
    ##Ingreso de datos
    u=int(input('Digite el valor de U(0): '))
    n=int(input('Digite el numero de terminos a calcular: '))-1

    ##Condiciones iniciales
    list_u=[u]

    for i in range(0,n):
        if list_u[i]%2==0:
            u_n=int(list_u[i]/2)
        else:
            u_n=3*list_u[i]+1
        list_u.append(u_n)
    
    print(list_u)
    
except:
    print('\nHa ocurrido un error, los valores digitados no son validos')

#%% 10. 
            
    
#%% 11.

def fun (h,b,c) :
    for i in range(1,h+1):
        for i in range(1,b+1):
            print(f' {c} ', end =' ')
        print('')
        
h = int(input('Altura del rectángulo: '))
b = int(input('Ancho del rectángulo: '))
c = input('Carácter del rectángulo: ')

fun(h,b,c)

#%% 12.

def fun1(x): 
    for i in range(1,x+1):
       print('*'*i)
    for j in range(x-1,0,-1):
        print('*'*j)
    
x = int(input('Base del triángulo: '))

fun1(x) 

#%% 13. Diseñe una función que pida dos años y escriba cuántos años bisiestos 
  #hay entre esas dos fechas (incluidos los dos años):
  
año1 = int(input('Digite un año inicial: ')) #Definimos variables
año2 = int(input('Digite un año posterior: ')) #Definimos variables
diferencia = año2 - año1 #encontramos la diferencia de años
biciestos = int(diferencia / 4) #Dividimos esta diferencia para encontrar qué 
                                #años son biciestos

#definimos la función
def fun1():
    if año1 > año2: #la diferencia de los años no puede ser negativa
        print(F'{año1} no puede ser mayor que {año2}, intenta de nuevo.')
        
    elif año1 < año2:
        for i in range(año1,año2+1):       
            residuo1 = i%4  #encontramos los números que dividen exactamente al
            residuo2 = i%100 #cuatro
            residuo3 = i%400
            if residuo1 == 0: #el número es valido si el residuo es cero
                residuo3 == 0 
                print() 
                
    print(f'Del año {año1} al año {año2} hay {diferencia} años,\
 {biciestos} de ellos son biciestos')
fun1()

#%% 14.

import random

def fun3(): 
    print('Escriba el resultado de las siguientes operaciones: ')
    
    c = 0
    
    while c < 5 :
        a = random.randrange(1,101)
        b = random.randrange(1,101)
        
        ans = int(input(f'{a} + {b} = '))
        
        if ans == a + b :
            c += 1
            print('respuesta correcta! tu puntuación es: ', c)
            
        else:
            print('respesta incorrecta :c, tu puntuación es: ', c)
        print()
        
    print('Programa terminado')
fun3() 
        
#%%15 Diseñar una función que permita jugar a una versión simplificada del juego
# Master Mind

##Funcion
def master_mind():
    '''Funcion que permite jugar una version simplificada de master mind'''
    
    ##Importar la libreria en caso de que no se tenga
    import random
    
    try:
        ##Intervalo restriccion
        min_len=2
        max_len=9
        
        ##Pedimos la longitud de la cadena
        lenght=int(input(f'Digite la longitud de la cadena de numeros (entre \
 {min_len} y {max_len}): '))
        
        ##Generamos una excepcion si el valor no esta en el intervalo [min_len,
        #max_len]
        if lenght<min_len or lenght>max_len:
            error=0/0
            
        ##Generamos la cadena aleatoria
        string=[]
    
        for i in range(0,lenght):
            num=random.randint(0,9)
            string.append(num)
            
        ##Para activar la ayuda quite el comentario de la siguiente linea
        ##print(string)
        
        ##Que se ejecute el programa hasta que adivine la cadena entera
        while True:
            ##Reinicio de condiciones
            m=0
            hits=0
            string_guest=[]
        
            quest=input('Intente adivinar la cadena: ')
    
            for n in quest:
                k=int(n)
                string_guest.append(k)
            
            while m<lenght:
                if string_guest[m]==string[m]:
                    hits+=1
                m+=1
        
            if hits==lenght:
                print('\nFelicitaciones con ',quest,' adivinaste toda la cadena')
            
                break
            else:
                print('\nCon ',quest,' adivinaste ',hits,' numeros de la cadena')
    except:
        print('\nHa ocurrido un error, los valores digitados no son validos')

##Prueba funcion
master_mind()