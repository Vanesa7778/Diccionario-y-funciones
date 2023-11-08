calificaciones = {
 'Sandra': 5.0, 
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

print("Iterar por valor")#se imprime Iterar por valor
#values() es un metodo que se utiliza para obtener una vista de los valores almacenados en un diccionario. 
for j in calificaciones.values():#for recorre y en cada iteracion la j toma un valor de los valores que hay en los  diccionarios
    print(j)# se imprime el valor actual de j que seria uno de los valores que hay en el diccionario
