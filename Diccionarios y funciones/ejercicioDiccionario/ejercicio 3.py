#Tecnicas de iteracion
calificaciones1 = {
 'nombre': 'Sandra', 
 'notafinal': 5.0
 }
calificaciones2 = {
 'Sandra': 5.0, 
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

#items() es un metodo que se utiliza para obtener una vista de pares clave-valor en un diccionario
for i, j in calificaciones2.items():#se utiliza para iterar a traves de las claves y valores en el diccionario calificaciones2

    print(i,j)#imprime los valores de i que es las claves y j que seria los valores en este caso las calificaciones
