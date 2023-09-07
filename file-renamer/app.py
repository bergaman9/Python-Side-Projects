import os

def rename_files_in_directory(directory_path):
    # Dizin içerisindeki dosyaları listele
    files = os.listdir(directory_path)

    # Dosyaları sırala
    files.sort()

    # Dosyaların yeni isimlerini oluştur ve yeniden adlandır
    count = 1
    for file in files:
        # Yeni dosya adını oluştur
        new_filename = f"{count:03d}{os.path.splitext(file)[1]}"

        # Dosyanın eski ve yeni yolu
        old_file_path = os.path.join(directory_path, file)
        new_file_path = os.path.join(directory_path, new_filename)

        # Dosyayı yeniden adlandır
        os.rename(old_file_path, new_file_path)

        # Sayacı artır
        count += 1

# Uygulama
# NOT: Bu kodu çalıştırmadan önce, lütfen yedeklerinizi alın!
rename_files_in_directory("C:\\Users\\berga\\Desktop\\Datasets\\full-atilla-kaya-songs-200-epochs")
