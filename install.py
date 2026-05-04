import os
from time import sleep

# --- Configuración de Colores ---
class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

def run(cmd):
    os.system(cmd)

def main():
    run("clear")
    print(f"{Colors.PINK}=== Termux-Desktop-Openbox Installer ==={Colors.RESET}")
    print(f"{Colors.BLUE}[+] Preparando el entorno {Colors.RESET}")
    sleep(1)

    # 1. Instalación de Dependencias (x11-repo y aplicaciones)
    # Se incluyen las apps que mencionaste: Audacious, Eww, Openbox, etc.
    apps = "audacious cava eww rofi openbox thunar picom tint2 neofetch feh starship"
    print(f"{Colors.BLUE}[+] Instalando paquetes necesarios...{Colors.RESET}")
    run("pkg install x11-repo python python-pip git wget curl -y")
    run(f"pkg install {apps} -y")

    # 2. Creación de directorios base
    run("mkdir -p ~/.config")
    run("mkdir -p ~/.local/share/fonts")

    # 3. Despliegue de archivos de configuración (.config)
    # Lista basada en tu estructura actual
    config_items = [
        "Audacious", "cava", "eww", "neofetch", "openbox", 
        "picom", "rofi", "Thunar", "tint2", "Wallpaper", "starship.toml"
    ]

    print(f"{Colors.GREEN}[+] Instalando carpetas en ~/.config...{Colors.RESET}")
    for item in config_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/.config/")
            print(f"  -> {item} configurado.")
        else:
            print(f"  {Colors.PINK}[!] Omitido: {item} no encontrado en la carpeta config/{Colors.RESET}")

    # 4. Movimiento de Ejecutables a /usr/bin/
    # Se mueven para que puedas ejecutarlos escribiendo solo su nombre
    executables = ["colortest-slim", "panes", "lavat"]
    BIN_PATH = "/data/data/com.termux/files/usr/bin"

    print(f"{Colors.BLUE}[+] Configurando ejecutables globales...{Colors.RESET}")
    for exe in executables:
        exe_path = f"config/{exe}"
        if os.path.exists(exe_path):
            run(f"cp {exe_path} {BIN_PATH}/")
            run(f"chmod +x {BIN_PATH}/{exe}")
            print(f"  -> {exe} movido a {BIN_PATH}")
        else:
            print(f"  {Colors.PINK}[!] Ejecutable no encontrado: {exe}{Colors.RESET}")

    # 5. Instalación de Fuentes
    if os.path.isdir("fonts"):
        print(f"{Colors.BLUE}[+] Instalando fuentes en el sistema...{Colors.RESET}")
        run("cp -r fonts/* ~/.local/share/fonts/")
        run("fc-cache -fv > /dev/null")
        print(f"  -> Fuentes actualizadas.")

    print(f"\n{Colors.GREEN}¡Instalación completada exitosamente!{Colors.RESET}")
    print(f"{Colors.BLUE}Ya puedes usar tus comandos: colortest-slim, panes y lavat.{Colors.RESET}")

if __name__ == "__main__":
    main()

