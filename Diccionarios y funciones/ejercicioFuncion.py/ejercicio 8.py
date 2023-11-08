#Modificando parámetros mutables
#Se define una funcion llamada lista que toma dos argumentos que son:'arg' y 'result'
def lista(arg, result=[]):#'arg' es el valor que se va a agregar a la lista 'result'
    result.append(arg)#dentro de la funcion se agrega el valor 'arg' a la lista 'result' con el metodo .append()
    print(result)#dentro de la funcion se agrega el valor 'arg' a la lista 'result' con el metodo .append()

lista('domingo', [])#se llama a la funcion lista con los argumentos 'domingo' y una lista vacia

