import base64

# Magic Bytes comunes para tipos de archivos
magic_bytes = {
    'pdf': b'%PDF',
    'png': b'\x89PNG'
}

# Función para detectar si el contenido descifrado coincide con Magic Bytes conocidos
def detect_magic_bytes(contenido_descifrado):
    for formato, magic in magic_bytes.items():
        if contenido_descifrado.startswith(magic):
            return formato
    return None

# Manipulación de Bytes
def leer_archivo_bytes(ruta_archivo):
    with open(ruta_archivo, 'rb') as archivo:
        return archivo.read()

# Base64
def descifrado_base64(contenido):
    print("Intentando Base64...")
    try:
        contenido_descifrado = base64.b64decode(contenido)
        formato = detect_magic_bytes(contenido_descifrado)
        if formato:
            return contenido_descifrado, f"Codificación Base64, formato {formato}"
    except Exception:
        pass
    return None, None

# Transformación: suma de constante a los bytes
def transformacion_suma(contenido):
    print("Intentando suma de constante a los bytes...")
    for constante in range(1, 256):
        contenido_descifrado = bytes([(byte + constante) % 256 for byte in contenido])
        formato = detect_magic_bytes(contenido_descifrado)
        if formato:
            return contenido_descifrado, f"Suma de constante {constante}, formato {formato}"
    return None, None
