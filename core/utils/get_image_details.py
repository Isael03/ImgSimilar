from PIL import Image
import imagehash
import os


def get_file_size(path):
    return os.path.getsize(path)

def get_resolution(path):
    with Image.open(path) as img:
        return img.width, img.height

def get_phash(path):
    with Image.open(path) as img:
        return imagehash.phash(img)
    
def get_mtime(path):
    return os.path.getmtime(path)

def get_resolution_area(path):
    w, h = get_resolution(path)
    return w * h