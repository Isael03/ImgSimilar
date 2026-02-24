import core.utils.get_image_details as details

def show_group_info(group):
    print("\n============================")
   
    for idx, path in enumerate(group):
        size = details.get_file_size(path) / 1024
        width, height = details.get_resolution(path)
        print(f"[{idx}] {path}")
        print(f"    Resolución: {width}x{height}")
        print(f"    Tamaño: {size:.2f} KB")
    print("============================")
