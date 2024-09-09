import cifrados

# Definir las rutas de los archivos
archivos = ['files/file1.lol', 'files/file2.lol', 'files/file3.lol', 'files/file4.lol']

# Procesar los archivos
for archivo in archivos:
    contenido = cifrados.leer_archivo_bytes(archivo)
    
    if not contenido:
        print(f"El archivo {archivo} está vacío o no se pudo leer correctamente.")
        continue
    
    print(f"Procesando el archivo: {archivo}")
    
    # Intentar descifrar con Base64
    descifrado, metodo = cifrados.descifrado_base64(contenido)
    
    # Intentar transformación de suma de constante si Base64 falla
    if not descifrado:
        descifrado, metodo = cifrados.transformacion_suma(contenido)
    
    # Intentar Cifrado César si los métodos anteriores fallan
    if not descifrado:
        descifrado, metodo = cifrados.descifrado_cesar(contenido)
    
    # Guardar y reportar si se logró descifrar
    if descifrado:
        ruta_descifrado = archivo + '_descifrado'
        with open(ruta_descifrado, 'wb') as f:
            f.write(descifrado)
        print(f"Archivo {archivo} descifrado utilizando {metodo}. Guardado como {ruta_descifrado}.")
    else:
        print(f"El archivo {archivo} no pudo ser descifrado.")