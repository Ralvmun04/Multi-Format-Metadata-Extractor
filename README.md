## Multi-Format-Metadata-Extractor
Una herramienta sencilla y eficiente en Python diseñada para extraer metadatos de diferentes tipos de archivos, incluyendo documentos PDF, imágenes JPG/JPEG y archivos de video MP4.

## 🚀 Características
Este script identifica automáticamente la extensión del archivo y utiliza la librería más adecuada para procesarlo:

  -PDF: Extrae información del documento (autor, título, software de creación, etc.) usando PyMuPDF.

  -Imágenes (JPG/JPEG): Extrae etiquetas EXIF (modelo de cámara, fecha, coordenadas GPS, etc.) mediante Pillow.

  -Video (MP4): Obtiene metadatos técnicos detallados utilizando Apache Tika.

## 🛠️ Requisitos previos
Antes de ejecutar el script, asegúrate de tener instalado Python 3.x y las dependencias necesarias:
```
pip install pymupdf tika Pillow
```
**Nota**: Apache Tika requiere que tengas instalado el Entorno de Ejecución de Java (JRE) en tu sistema para funcionar correctamente.

## 📋 Uso
1. Clona este repositorio o descarga el archivo .py.

2. Ejecuta el script en tu terminal:
  ```
  python nombre_del_archivo.py
  ```
3. Introduce la ruta completa o relativa del archivo que deseas analizar cuando el programa lo solicite.

## ⚙️ Funcionamiento
El flujo de trabajo del script es el siguiente:

1. Validación: Comprueba si el archivo existe en la ruta proporcionada.

2. Identificación: Analiza la extensión del archivo (.pdf, .jpg, .jpeg, .mp4).

3. Extracción:

  -Si es PDF, recorre el diccionario de metadatos del documento.

  -Si es Imagen, decodifica las etiquetas EXIF legibles.

  -Si es Video, utiliza el servidor de Tika para parsear la estructura interna del archivo.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Si tienes ideas para soportar más formatos (como .docx o .png), no dudes en abrir un Pull Request o crear un Issue.

>[!WARNING]
>Si no puedes descargar algunas librerias, hazlo desde un entorno env en la terminal
