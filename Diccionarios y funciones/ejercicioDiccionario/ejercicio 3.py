#Tecnicas de iteracion
calificaciones = {
 'nombre': 'Sandra', 
 'notafinal': 5.0
 }
calificaciones = {
 'Sandra': 5.0, 
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

#items() es un metodo que se utiliza para obtener una vista de pares clave-valor en un diccionario
for i, j in calificaciones.items():#se utiliza para iterar a traves de las claves y valores en el diccionario "calificaciones"

    print(i,j)#imprime los valores de i que es las claves y j que seria los valores en este caso las calificaciones
