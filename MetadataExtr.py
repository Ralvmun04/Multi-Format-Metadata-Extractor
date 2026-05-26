from pathlib import Path
import pymupdf as fitz
from tika import parser
from PIL import Image
from PIL.ExifTags import TAGS

ruta_input = input("Pon la ruta del archivo a analizar: ")
archivo = Path(ruta_input)
ext = archivo.suffix.lower()

if not archivo.exists():
    print("Archivo no encontrado")
else:

    if ext == ".pdf":
        doc = fitz.open(archivo)
        print("\n------ PDF Metadata: ------")
        for  key, value in doc.metadata.items():
            print(f"{key}: {value}")
        doc.close()

    elif ext in [".jpeg", ".jpg"]:
        print("\n------ Image EXIF Data: -------")
        try:
            imagen = Image.open(archivo)
            info = imagen._getexif()
            if not info:
                print("No se ha encontrado metadata en este archivo .jpg")
            else:
                for tag, value in info.items():
                    key = TAGS.get(tag, tag)
                    print(f"{key}: {str(value)[:1000]}")
        except Exception as e:
            print("No se ha encontrado la imagen")

    elif ext == ".mp4":
        print("\n------ Video Metadata: ------")
        metadata = parser.from_file(ruta_archivo)
        for key, value in metadata.get("metadata", {}).items():
            print(f"{key}: {value}")