import os
import subprocess
import winreg

def get_programs_wmic():
    programs = {}
    try:
        result = subprocess.run(['wmic', 'product', 'get', 'name'], stdout=subprocess.PIPE, text=True)
        lines = result.stdout.split('\n')[1:-1]

        for line in lines:
            line = line.strip()
            if line:
                programs[line] = "WMIC - Bilgi Yok"
    except Exception as e:
        print(f"WMIC Hata: {e}")

    return programs

def get_programs_registry():
    programs = {}
    registry_keys = [
        r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
        r'SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall'
    ]

    for registry_key in registry_keys:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_key)
        for i in range(0, winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)
            try:
                program_name = winreg.QueryValueEx(subkey, 'DisplayName')[0]
                program_version = winreg.QueryValueEx(subkey, 'DisplayVersion')[0] if winreg.QueryValueEx(subkey, 'DisplayVersion') else "Bilgi Yok"
                publisher = winreg.QueryValueEx(subkey, 'Publisher')[0] if winreg.QueryValueEx(subkey, 'Publisher') else "Bilgi Yok"
                programs[program_name] = f"Versiyon: {program_version}, Yayıncı: {publisher}"
            except WindowsError:
                pass

    return programs

if __name__ == "__main__":
    wmic_programs = get_programs_wmic()
    registry_programs = get_programs_registry()

    # İki sözlüğü birleştir ve tekrarlayanları kaldır
    all_programs = {**wmic_programs, **registry_programs}

    with open('programs.txt', 'w', encoding='utf-8') as f:
        for program, info in sorted(all_programs.items()):
            f.write(f"{program} ({info})\n")

    print("Program listesi programs.txt dosyasına yazıldı.")
