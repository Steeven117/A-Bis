## PROGRAMA PARA SABER SI UN AÑO ES BISIESTO

print ("----------------------------------------------")
print ("-----------CUANDO UN AÑO ES BISIESTO----------")
print ("----------------------------------------------")

import math
#INPUT

Año = int(input("Escribe el año: "))

A= Año%4
B= Año%100
C= Año%400 


#PROCESING

if  (Año % 4 == 0 and Año % 100 !=0) or Año % 400 == 0:
    rta="El Año es bisiesto"
else:
    rta="El Año no es bisiesto"


#OUTPUT

print(rta)

