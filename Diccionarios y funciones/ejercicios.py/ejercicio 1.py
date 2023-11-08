#Escriba una función en Python que reproduzca lo siguiente:𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2 Valor para X=3 y valor para Y=5
#se define la funcion como calcular y toma dos argumentos que 'x' ,'y'
def calcular(x, y):
    # Calcula el resultado y lo retorna
    return x * 2 + y * 2

# Se asignan los valores
x = 3
y = 5

# Se llama a la función "calcular" con los valores "x" e "y" y se guarda ese resultado en "result"
result = calcular(x, y)

# Se imprime el resultado
print(result)
