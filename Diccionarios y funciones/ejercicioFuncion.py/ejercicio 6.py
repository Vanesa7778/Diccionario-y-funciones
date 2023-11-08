#Funciones con Parámetros Nominales
def compra(marca,cantidad,valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )
#llama la funcion compra con valores específicos y imprime un mensaje que incluye el resultado.
print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')
