from cifrados import descifrado_base64, leer_archivo_bytes, transformacion_suma

# Definir las rutas de los archivos
archivos = ['files/file1.lol', 'files/file2.lol', 'files/file3.lol', 'files/file4.lol']

# Procesar los archivos
for archivo in archivos:
    contenido = leer_archivo_bytes(archivo)
    
    if not contenido:
        print(f"El archivo {archivo} está vacío o no se pudo leer correctamente.")
        continue
    
    print(f"Procesando el archivo: {archivo}")
    
    # Probar con Base64
    descifrado, metodo = descifrado_base64(contenido)
    
    # Aplicar transformaciones adicionales si no se logra descifrar con Base64
    if not descifrado:
        descifrado, metodo = transformacion_suma(contenido)
    
    if descifrado:
        ruta_descifrado = archivo + '_descifrado'
        with open(ruta_descifrado, 'wb') as f:
            f.write(descifrado)
        print(f"Archivo {archivo} descifrado utilizando {metodo}. Guardado como {ruta_descifrado}.")
    else:
        print(f"El archivo {archivo} no pudo ser descifrado.")
