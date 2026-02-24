import os
from core.utils import get_image_details as details
from core.utils.move_to_trash import move_to_trash
from console.show_group_info import show_group_info
from core.utils.show_image import show_image




def interactive_delete(group):
    view = input("¿Deseas ver las imágenes? (s/n): ").strip().lower()
    if view == "s":
        for path in group:
            show_image(path)

    show_group_info(group)

    try:
        choice = input("¿Qué deseas hacer? (m = manual, r = mayor resolución, s = menor tamaño, n = nada): ")

        if choice == "m":
            keep = int(input("Número de imagen a conservar: "))
            for i, path in enumerate(group):
                if i != keep:
                    move_to_trash(path)
                    print(f"🗑 Eliminado: {path}")

        elif choice == "r":
            best = min(
                group,
                key=lambda p: (
                    -details.get_resolution_area(p),
                    details.get_file_size(p),
                    -details.get_mtime(p)
                )
            )
           
            for path in group:
                if path != best:
                    move_to_trash(path)
                    print(f"🗑 Eliminado: {path}")
            print(f"✅ Conservada (mayor resolución): {best}")

        elif choice == "s":
            best = min(
                group,
                key=lambda p: (
                    details.get_file_size(p),
                    -details.get_resolution_area(p),
                    -details.get_mtime(p)
                )
            )

            for path in group:
                if path != best:
                    move_to_trash(path)
                    print(f"🗑 Eliminado: {path}")
            print(f"✅ Conservada (menor tamaño): {best}")

        else:
            print("⏭ Grupo omitido.")
    except Exception as e:
        print(f"⚠ Error: {e}. Grupo omitido.")