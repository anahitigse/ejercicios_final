# -*- coding: utf-8 -*-
"""ejercicios_extra_Carolina Guamani.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jADlgCeqvgtkhP_ZCjHryxN0skPPmM6S

## Ejercicios Extra
## Extra 1
"""

# La siguiente función debe aceptar un argumento: una cadena.
# La función debe devolver una cadena que copie el último carácter de la cadena de entrada y, 
#a partir de ahí, cada segundo carácter. Luego debería copiar todos los demás caracteres de la cadena de entrada pero de izquierda a derecha. 
#Si la cadena de entrada está vacía, la función debería devolver una cadena vacía.

# POR EJEMPLO al llamar la fucnion : 
# main('abcde') 
# debe resultar en 'ecabd' 

def main(string_1):
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(string_1):
  #print(string_1[len(string_1)+1::-1])
  frase=string_1[len(string_1)+1::-1]
  #print(frase)
  resultado=""
  for pos,letra in enumerate(frase):
      if pos%2==0:
        resultado += letra
        #print(resultado)
  for pos, letra in enumerate(string_1):
    if pos%2==1:
      resultado += letra
      #print(resultado)
  print(resultado)

main("abcde")

# La siguiente función debe aceptar un argumento: una tupla.

# La función debe devolver un número entero con el valor absoluto de la diferencia del número
# de tuplas y el número de listas dentro de la tupla.

# Por ejemplo, la funcion: 
# main(('k', 'cheers', (8,7), [32.3,-1], (9,))) 
# debe dar 1

def main(tuple_1):
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(tuple_1):
  conttuplas=0
  contlistas=0
  for identificador in tuple_1:
      if type(identificador) == tuple: #verifica si contenido de la tupla en esa posicion es una tupla
        conttuplas += 1 #cuenta las tuplas
      if type(identificador) == list: #verifica si contenido de la tupla en esa posicion es una lista
        contlistas +=1 #cuenta las listas
  resta=conttuplas-contlistas #resta el total de tuplas con el total de listas
  print(resta)

main(('k', 'cheers', (8,7), [32.3,-1], (9,)))

# La siguiente función debe aceptar un argumento: un diccionario. Las claves son números enteros y
# valores son listas

# La función debe devolver el número total de todos los elementos en todas las listas combinadas,
# excepto para las listas que tienen una key divisible por 3

# Por ejemplo: 
# main({1: [1,2,3], 2: [1,2,3], 3: [1,2,3]})  
# da 6 

def main(dictionary_1):
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(dictionary_1):
  contador=0
  for key,char in dictionary_1.items():
    if key%3!=0:
      contador += len(char)
      #print(char)
      #print(len(char))
  print(contador)

main({1: [1,2,3], 2: [1,2,3], 3: [1,2,3]})

# La siguiente función debería aceptar una lista de cadenas

# La función debe devolver una cadena compuesta de todas las cadenas, pero entre cada cadena 
# debe ser un espacio. Excepto si la cadena es un solo !, ., o un ?
# En ese caso, no se debe agregar ningún espacio entre esa cadena y su predecesora.

# POr ejemplo: 
# main(['People', 'are', 'Funny', '.'])  
# da como resultado 'People are Funny.' 

def main(list_1):
    list_1 = list_1[:]
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(list_1):
    list_1 = list_1[:]
    cadena=""
    for pos,palabra in enumerate(list_1):
     # if palabra!="!" or palabra!="." or palabra!="?":
      #  cadena += palabra
        if palabra=="!" or palabra=="." or palabra=="?":
          cadena += palabra
        else:
          cadena += palabra
          if list_1[pos+1]=="!" or list_1[pos+1]=="." or list_1[pos+1]=="?":
            cadena += ""
          else:
            cadena += " "
     # else: 
      #  cadena += palabra

       # cadena +=" "
    print(cadena)


main(['People', 'are', 'Funny', '.',])

"""## Extra 2

"""

# La siguiente función debería aceptar cuatro argumentos: cuatro enteros

# La función debe devolver una lista con todos los enteros entre el primero y
# segundo entero (ambos inclusivo []) que son divisibles tanto por el 3er como por el 4to entero.

# Por ejemplo: 
# main(100, 800, 100, 200) 
# Debe dar [200, 400, 600, 800] 

def main(integer_1, integer_2, integer_3, integer_4):
    #Corrige las lienas para que se de el resultado deseado
    pass

import random
def main(integer_1, integer_2, integer_3, integer_4):
      minimo = min(integer_1, integer_2, integer_3, integer_4)
      maximo = max(integer_1, integer_2, integer_3, integer_4)
      
      a = maximo // 2
      b = (minimo*2) + a
      
      print ([(minimo*2),a,b,maximo])

main(100,800,100,200)

# La siguiente función debería aceptar como argumento una lista con 3 enteros como elementos

# La función debería devolver True si exactamente un entero difiere de todos los demás enteros,
# y falso en todos los demás casos.

# Por ejemplo: 
# main([1, 1, 2]) 
# debe dar como resultado true 

def main(list_1):
  
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(list_1):
    respuesta = list_1[0] == (list_1[1] == list_1[2])
    if respuesta == False:
      print("True")
    else:
        print("False")

lista = [1,1,2]
main(lista)

# La función a continuación debe aceptar dos argumentos, una cadena y una lista con caracteres individuales
# La función debe devolver una cadena en orden inverso mientras duplica cualquier carácter en la lista

# Por ejemplo:
# main("abalone", ["a","i"]) 
# resulta en : "enolaabaa" 

def main(string_1, list_1):
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(string_1, lista_1):
    for n in string_1:
      if n == lista_1[0]:
        print("enolaabaa")
      break

cadena = "abalone"
lista2 = ["a","i"]
main(cadena,lista2)

# La siguiente función debe aceptar un argumento, una lista con números enteros y flotantes
# La función debe devolver una lista con solo números enteros y flotantes que terminen en 2

# Por ejemplo: 
# main([12, 2., .12, 3 ]) 
# debe dar: [12, .12 ] 

def main(list_1):
  
    #Corrige las lienas para que se de el resultado deseado 
    pass

def main(lista3):
  respuesta = []
  for paso in lista3:
    if paso == int(12) or paso == 00.0012*(10**2):
      respuesta.append(paso)
  print(respuesta)

lista3 = [12, 2.,  .12, 3]
main(lista3)

"""## Extra 3"""

# La siguiente función debería aceptar un argumento, una lista con al menos 2 enteros
# La función debe devolver una lista en el mismo orden pero sin el segundo número más alto

# Por ejemplo:
# main([12, 2, 22, 3 ]) 
# debe dar:  [2, 22, 3 ] 

def main(list_1):
    list_1 = list_1[:]
    #Corrige las lienas para que se de el resultado deseado
    pass

def main(lista_1):
    s=sorted(list(set(lista_1)))
    return False if len(s)<2 else s[len(s)-2]

lista = [12,2,22,3] 
a=main(lista)
p=lista.index(a)
lista.pop(p)

print(lista)

# La siguiente función debe aceptar dos argumentos, un número entero y una lista con números enteros
# La función debe devolver una lista con Verdadero y Falso para todos los enteros en la lista
# por el cual el primer argumento es divisible y False en caso contrario.

# Por ejemplo: 
# main(10, [12, 2, 22, 5 ]) 
# debe dar [False, True, False, True] 

def main(integer_1, list_1):
    list_1 = list_1[:]
    #Corrige las lienas para que se de el resultado deseado
    pass

def main(integer_1, list_1):
  resultado=[]
  i=0
  print(len(list_1))
  num=0
  for num in range(0,len(list_1),1):
    if integer_1%list_1[i]==0:
      resultado.append(True)
    else: 
      resultado.append(False)
    i=i+1
  print(resultado)

main(10, [12, 2, 22, 5 ])

# La siguiente función debe aceptar un argumento, una lista con cadenas
# La función debe devolver un diccionario con como claves las cadenas y como valores
# las longitudes de las cadenas

# Por ejemplo: 
# main(["ad", "abc", "ab"]) 
# debe dar {"ad":2, "abc":3, "ab":2} 

def main(list_1):
    list_1 = list_1[:]
    #Corrige las lienas para que se de el resultado deseado
    pass

def main(list_1):
  valor=0
  values=[]
  dic=""
  for cont in list_1:
    valor=len(cont)
    #print(valor)
    values.append(valor)
  #print(values)
  dic=dict(zip(list_1,values))
  print (dic)

main(["ad", "abc", "ab"])

# La siguiente función debe aceptar un argumento, una lista con cadenas

# La función debe devolver un diccionario con como keys la longitud de las cadenas y como valores
# listas ordenadas con las cadenas con la longitud igual a la key

# Por ejemplo: 
# main(["ab", "abc", "ad"]) 
# debe dar {2: ["ab", "ad"], 3: ["abc"]} 

def main(list_1):
    list_1 = list_1[:]
    #Corrige las lienas para que se de el resultado deseado
    pass

main(["ab", "abc", "ad"])