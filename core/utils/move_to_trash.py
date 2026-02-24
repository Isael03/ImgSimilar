
from send2trash import send2trash
from core.utils.get_image_details import get_file_size


def move_to_trash(path):
    try:
        size = get_file_size(path)
        send2trash(path)
        print(f"🗑 Enviado a papelera: {path}")
        return size
    except Exception as e:
        print(f"⚠ Error moviendo {path}: {e}")
        return 0