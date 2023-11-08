def retornarnumero():#esta devolviendo la informacion por medio del programa principal y puede afectarlo
    return 1
retornarnumero()#llama a la funcion retornarnumero

if retornarnumero()==1:#se llama a la funcion retornarnumero() y compara su resultado con el valor 1
    print("devolvió un uno")#si la funcion retorna 1,se imprime "devolvio un uno"
else:
    print("No devolvió un uno")#si la funcion no  retorna 1,se imprime "no devolvio un uno"