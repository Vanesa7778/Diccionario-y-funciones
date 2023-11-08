#Tomé el presente ejercicio,  y pasé a la función la lista con los días de la semana restantes
#Se define una funcion llamada lista que toma dos argumentos que son:'arg' y 'result'
def lista(arg, result=[]):#'arg' es el valor que se va a agregar a la lista 'result'
    result.append(arg)#dentro de la funcion se agrega el valor 'arg' a la lista 'result' con el metodo .append()
    print(result)#dentro de la funcion se agrega el valor 'arg' a la lista 'result' con el metodo .append()
#se define una lista llamada diasDeLaSemana con los dias restantes de la semana
diasDeLaSemana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
lista('domingo', diasDeLaSemana)#se llama a la funcion lista y domingo como valor'arg' y diasDeLaSemana como el valor de 'result' 
