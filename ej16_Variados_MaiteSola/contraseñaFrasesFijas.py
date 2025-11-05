def cambia(frase, diccionario, n=None):
    """
    Reemplaza caracteres de 'frase' según 'diccionario'.
    Si se proporciona 'n', limita el número de reemplazos por carácter.
    """
    resultado = frase
    for clave, valor in diccionario.items():
        if n is None:
            # Reemplazo ilimitado
            resultado = resultado.replace(clave, str(valor))
        else:
            # Reemplazo limitado a n veces
            resultado = resultado.replace(clave, str(valor), n)
    return resultado

# Ejemplos de uso
frase1 = "quiero mi password segura."
diccionario1 = {'a':4,'e':3,'i':1,'o':0,'.':'?'}

print(cambia(frase1, diccionario1))
# Salida: "qu13r0 m1 p4ssw0rd s3gur4?"

frase2 = "gatito bonito"
diccionario2 = {'t':'n','o':''}

print(cambia(frase2, diccionario2))
# Salida: "ganin bonin"

frase3 = "pablito clavo un clavito"
diccionario3 = {'a':4,'o':0,'i':1}

print(cambia(frase3, diccionario3, 1))
# Salida: "p4bl1t0 clavo un clavito"

print(cambia(frase3, diccionario3, 3))
# Salida: "p4bl1t0 cl4v0 un cl4v1t0"
