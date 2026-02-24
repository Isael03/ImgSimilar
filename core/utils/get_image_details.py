from PIL import Image
import imagehash
import os

""" Desactiva el warning y limite de tamaño de imagen para evitar errores con imágenes grandes. 
De por si en get_phash se redimensiona la imagen antes de calcular el hash pudiendo desactivar esta medida de seguridad."""
Image.MAX_IMAGE_PIXELS = None     

def get_file_size(path):
    return os.path.getsize(path)

def get_resolution(path):
    with Image.open(path) as img:
        return img.width, img.height

def get_phash(path):
    """ with Image.open(path) as img:
        return imagehash.phash(img) """
    try:
        with Image.open(path) as img:
            img = img.convert("L") # Convierte a escala de grises 
            img.thumbnail((512, 512)) # Redimensiona la imagen para mejorar la velocidad de cálculo
            return imagehash.phash(img, hash_size=16) # hash_size=16 para obtener un hash de 256 bits y reducir falsos positivos
    except Exception:
        return None
    
def get_mtime(path):
    return os.path.getmtime(path)

def get_resolution_area(path):
    w, h = get_resolution(path)
    return w * h