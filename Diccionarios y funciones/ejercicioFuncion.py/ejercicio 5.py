#Funciones con Parámetros Posicionales
#se define una funcion llamada compra que toma tres argumentos los cuales son:"marca", "cantidad" y "valor"
def compra(marca,cantidad,valor):#la funcion calcula el costo total de la compra
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )#retornando en un diccionario con la informacion de la compra

print(f' lo comprado fue:{compra("AMD",3,2500000)}')#imprime y asume el orden que esta arriba
