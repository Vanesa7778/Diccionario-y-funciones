#Modificando parámetros mutables
#se define una funcion llamada 'listalimpia' que tiene dos argumentos:'arg' y 'result con un valor predeterminado de None
def listalimpia(arg, result=None):
    if result is None:#si el argumento 'result' es None 
        result = []#se crea una lista vacia
        result.append(arg)#se agrega el valor del argumento 'arg' a la lista utilizando el metodo .append()
        print(result)
#llama a la funcion 'listalimpia' con el valor 'a'       
listalimpia("a")
#llama a la funcion 'listalimpia' con el valor 'b'
listalimpia("b") 