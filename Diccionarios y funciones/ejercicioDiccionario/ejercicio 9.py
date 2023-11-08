calificaciones = {
 'Sandra': 5.0, 
 'Adriana': 5.0,
 'Mauricio': 4.5,
 'Jose': 2.5,
 'Rosa': 3.7,
 'German': 4.8
}

#BORRAR UN ELEMENTO DEL DICCIONARIO
#el del se utiliza para eliminar elementos o variables de listas o diccionarios 
del(calificaciones['Rosa'])#En este caso del esta elimando la clave rosa con su valor del diccionario elementos
for i, j in calificaciones.items():#for recoorre y por cada iteracion i toma una clave y j un valor
    print(i,j)#imprime el valor actual de i que son las claves y de j que son los valores

