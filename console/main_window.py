import core.utils.find_similar_images as finder
from console.interactive_delete import interactive_delete

def main_window():
    folder = input("📂 Ruta de la carpeta: ").strip()

    try:
        threshold = int(input("🔎 Nivel de similitud (recomendado 5) \n0 -> Idénticas visualmente \n5 -> Casi iguales \n>10 más permisivo: "))
    except ValueError:
        print("Se usará el valor por defecto (5).")
        threshold = 5

    print("\n=========Buscando imágenes similares===================")
    groups = finder.find_similar_images(folder, threshold)

    print(f"\nSe encontraron {len(groups)} grupos de imágenes similares.")

    for group in groups:
        interactive_delete(group)

    print("\n✨ Proceso finalizado.")