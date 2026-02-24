import os
import platform

def show_image(path):
    try:
        system = platform.system()
        if system == "Windows":
            os.startfile(path)      
        elif system == "Darwin":  
            os.system(f"open {path}")  
        else: # Linux y otros
            os.system(f"xdg-open {path}")
       
    except Exception as e:
        print(f"Error al mostrar la imagen: {e}")
