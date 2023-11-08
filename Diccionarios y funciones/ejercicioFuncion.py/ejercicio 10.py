#Funciones anónimas «lambda» es una funcion de una solo sentencia con una actividad en particular
#se define una funcion anonima (lambda) llamada numero_palabras que toma un argumento 't'
#utiliza el metodo .strip() para eliminar espacios en blanco
#utiliza el metodo .split() para dividir la cadena en palabras utilizando espacios
#utiliza len() para contar la cantidad de palabras en la cadena
numeroPalabras = lambda t: len(t.strip().split())
#Se llama a la funcion numero_palabras con la cadena "hola, esto es una prueba con lambda".
print(numeroPalabras("hola, esto es una prueba con lambda"))#resultado funcion numero 7(cantidad de palabras)

#Ejemplo 2 función Lambda
#se define una funcion anonima (lambda) llamada operadorand que toma dos argumentos, 'x' ,'y'
#realiza una operacion de AND bit a bit entre ellos
#Un bit es  un dígito binario que puede ser 0 o 1 es la forma mas basica de almacenar y manipular datos en un sistema informatico
operadorand = lambda x, y: x & y
#Se utilizan dos bucles anidados para iterar sobre todos los posibles valores de "i" y "j" (0 y 1).
for i in range(2):
    
    for j in range(2):
#se imprime una cadena que muestra los valores de 'i' y 'j' junto con el resultado de la operacion AND entre estos valores. Por ejemplo '0 & 0 = 0' significa que 0 AND 0 es igual a 0, y '1 & 0 = 0' significa que 1 AND 0 es igual a 0
        print(f"{i} & {j} = {operadorand(i, j)}")#devolver una tabla de verdad
