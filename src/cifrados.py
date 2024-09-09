import base64

# Magic Bytes comunes para tipos de archivos
magic_bytes = {
    'pdf': b'%PDF',
    'png': b'\x89PNG',
    'mp3': b'\xFF\xFB'  # Añadiendo magic bytes de MP3 para referencia
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
    try:
        contenido_descifrado = base64.b64decode(contenido)
        formato = detect_magic_bytes(contenido_descifrado)
        if formato:
            return contenido_descifrado, f"Codificación Base64, formato {formato}"
    except Exception:
        pass
    return None, None

# Cifrado César
def descifrado_cesar(contenido, desplazamiento):
    contenido_descifrado = bytes((byte - desplazamiento) % 256 for byte in contenido)
    formato = detect_magic_bytes(contenido_descifrado)
    if formato:
        return contenido_descifrado, f"Cifrado César con desplazamiento {desplazamiento}, formato {formato}"
    return None, None

# Cifrado Decimado
def descifrado_decimado(contenido, factor):
    contenido_descifrado = bytes((byte * pow(factor, -1, 256)) % 256 for byte in contenido)
    formato = detect_magic_bytes(contenido_descifrado)
    if formato:
        return contenido_descifrado, f"Cifrado Decimado con factor {factor}, formato {formato}"
    return None, None

# Cifrado Afín
def descifrado_afin(contenido, a, b):
    contenido_descifrado = bytes(((byte - b) * pow(a, -1, 256)) % 256 for byte in contenido)
    formato = detect_magic_bytes(contenido_descifrado)
    if formato:
        return contenido_descifrado, f"Cifrado Afín con a={a}, b={b}, formato {formato}"
    return None, None