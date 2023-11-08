#Parámetros por defecto    
#Se define una funcion llamada 'compra' que toma dos argumentos que son 'marca','cantidad' y 'valor' con un valor predeterminado de 2500000.
def compra(marca,cantidad,valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )
#fuera de la funcion se llama a compra con valores especificos para 'marca'("AMD") y 'cantidad'(3)Como esta el valor de 'valor'se utiliza el valor predeterminado de 2500000
print(f' lo comprado fue:{compra("AMD",3)}')
