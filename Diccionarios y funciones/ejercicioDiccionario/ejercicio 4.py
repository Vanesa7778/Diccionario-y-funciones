calificaciones = {
 'Sandra': 5.0, 
 'Adriana':5.0,
 'Mauricio':4.5,
 'Jose':2.5
 }

print("Técnicas por clave")#se imprime Tecnicas por clave
# keys() es un método que se utiliza para obtener una vista de las claves (keys) del diccionario.
for i in calificaciones.keys():#for recorre cada clave (key) del diccionario, en cada iteracion i toma el valor de una de estas claves en el diccionario
    print(i)#imprime el valor de i que es la clave de calificaciones

