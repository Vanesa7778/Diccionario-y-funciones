#Declaracion de un diccionario 
diccionario = dict()#Esta linea crea un diccionario vacío llamado "diccionario" utilizando la función dict().En este caso, el diccionario se inicializa sin ningún par clave-valor.

# Diccionario vacio inicializado con llaves
diccionario= {}

# Diccionario inicializado con valores
diccionario = {'nombre':'Sandra' , 'edad': 44}# se crea un diccionario llamado 'Diccionario' con dos atributos que almacenan un valor 

#Accediendo a los elementos de  un diccionario
#imprime el diccionario
print(diccionario ['nombre'])#Se imprimira el valor 'Sandra' que corresponde a la clave 'nombre' en el diccionario "Diccionario"
print(diccionario.get('nombre','No existe'))#se utiliza el metodo .get()para acceder al valor de la clave 'nombre' en el diccionario y si la clave existe  imprime el valor de esa clave ('Sandra') pero si la clave no existe, imprimira 'No existe' 

