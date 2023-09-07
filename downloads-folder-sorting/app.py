import os
import shutil

# İstenen klasör dizini
folder = os.path.abspath("E:\My Drive\Graphic Design\Teknominatör\YouTube\Thumbnails")

# Dosya türüne göre klasör yaratma
file_types = {
    "html": "HTML Dosyaları",
    "pdf": "PDF Dosyaları",
    "png": "PNG Dosyaları",
    "jpg": "JPG Dosyaları",
    "jpeg": "JPEG Dosyaları",
    "gif": "GIF Dosyaları",
    "txt": "Metin Dosyaları",
    "zip": "ZIP Dosyaları",
    "exe": "Uygulamalar",
    "msi": "Uygulamalar",
    "dmg": "Uygulamalar",
    "iso": "Uygulamalar",
    "psd": "PSD Dosyaları"
}

# Dosyaları türüne göre sınıflandırma
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        file_extension = filename.split(".")[-1]
        if file_extension in file_types:
            folder_name = file_types[file_extension]
            folder_path = os.path.join(folder, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            shutil.move(path, os.path.join(folder_path, filename))

