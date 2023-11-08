#se definen 2 listas con valores que son una de nombres y otra de edades
nombres = ['Melissa', 'Vanesa', 'Stiven']
edades = ['16', '17', '18']
#la funcion zip se utiliza para combinar las dos listas en parejas de elementos
for n, e in zip(nombres, edades):#for recorre y por cada iteracion n toma el de un nombre y e toma el valor de una edad
#la funcion format{} Permite combinar valores o variables con una cadena de formato 
    print('Tu nombre es {0} y tu edad {1}.'.format(n, e))#se imprime el nombre y edad de la persona
