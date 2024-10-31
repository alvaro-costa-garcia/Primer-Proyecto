import os
import argparse
from PIL import Image

# Configuración de argparse
parser = argparse.ArgumentParser(description='Redimensionar imágenes en una carpeta y subcarpetas.')
parser.add_argument('--path', required=True, help='Ruta a la carpeta con imágenes.')
args = parser.parse_args()

# Carpeta de entrada
input_folder = args.path
sizes = {
    'thumbnail': (150, 150),
    'small': (300, 300),
    'medium': (600, 600),
    'large': (1200, 1200)
}

# Comienza a redimensionar imágenes
found_images = False
for root, _, files in os.walk(input_folder):
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            found_images = True
            img_path = os.path.join(root, filename)
            print(f"Procesando: {img_path}")  # Mensaje de depuración
            try:
                with Image.open(img_path) as img:
                    for size_name, size in sizes.items():
                        img_resized = img.resize(size, Image.LANCZOS)
                        resized_filename = f"{os.path.splitext(filename)[0]}_{size_name}{os.path.splitext(filename)[1]}"
                        resized_output_path = os.path.join(root, resized_filename)

                        img_resized.save(resized_output_path)
                        print(f"  Creando: {resized_output_path}")  # Mensaje de depuración

            except Exception as e:
                print(f"Error procesando {img_path}: {e}")

if not found_images:
    print("No se encontraron imágenes en la ruta especificada.")

print("Redimensionamiento completo.")
