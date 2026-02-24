# ImgSimilar CLI

Herramienta para detectar imágenes similares y mover duplicados a la papelera.

## Pasos
- Indicar la ruta de la carpeta que contiene las imágenes.
- Indicar el threshold (ver Threshold).
- Esperar que detecte los duplicados, si no hay la app se cerrará.
- Responder si abre el grupo de imágenes iguales o similares.
- Decidir con cual quedarse (Ver acciones.)

## Requisitos

- Python 3.14.3

## Instalación

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Threshold

* 0 → solo idénticas visualmente
* 5 → casi iguales
* 10 → más permisivo
* >15 → empieza a detectar cosas distintas

## Acciones

Para cada grupo similar puedes:

* m → elegir cuál conservar
* r → quedarte con mayor resolución
* s → quedarte con la más liviana
* n → no tocar nada

## Generar ejecutable
```
python -m PyInstaller --onefile img_similar.py
```