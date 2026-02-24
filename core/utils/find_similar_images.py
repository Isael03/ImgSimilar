import os
import core.utils.get_image_details as details
from core.utils.show_image import show_image

IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')

def find_similar_images(folder, threshold=5):
    images = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(IMAGE_EXTENSIONS):
                path = os.path.join(root, file)
                try:
                    phash = details.get_phash(path)
                    images.append((path, phash))
                except:
                    pass

    groups = []
    visited = set()

    for i in range(len(images)):
        if i in visited:
            continue

        group = [images[i][0]]

        for j in range(i + 1, len(images)):
            if images[i][1] - images[j][1] <= threshold:
                group.append(images[j][0])
                visited.add(j)

        if len(group) > 1:
            groups.append(group)

    return groups