from PIL import Image # Importa la biblioteca Pillow para el procesamiento de imágenes.
import os # Importa el modulo os para interactuar con el sistema de archivos.

def convert_png_to_jpg(png_file_path, jpg_file_path):
    # Abre la imagen PNG
    with Image.open(png_file_path) as img:
        # Convierte la imagen a modo RGB (necesario para guardar como JPEG)
        rgb_img = img.convert('RGB')
        # Guarda la imagen en formato JPG
        rgb_img.save(jpg_file_path, format='JPEG')

def convert_all_png_in_directory(directory_path):
    # Recorre todos los archivos en el directorio
    for filename in os.listdir(directory_path):
        # Si el archivo es una imagen PNG
        if filename.endswith(".png"):
            # Construye las rutas de los archivos
            png_file_path = os.path.join(directory_path, filename)
            # Construye la ruta completa del archivo JPG, cambiando la extensión a .jpg
            jpg_file_path = os.path.join(directory_path, filename[:-4] + ".jpg")
            # Convierte la imagen
            convert_png_to_jpg(png_file_path, jpg_file_path)
            # Imprime un mensaje indicando que la conversion se ha realizado.
            print(f"Convertido: {png_file_path} a {jpg_file_path}")

# Especifica el directorio que contiene las imágenes PNG
directorio_imagenes = 'C:/Users/TuUsuario/Desktop/imagenes_convertir' # Cambiar por tu directorio real

# Ejecuta la conversión
convert_all_png_in_directory(directorio_imagenes)
