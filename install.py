import os
from time import sleep

# --- Color Settings ---
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
    print(f"{Colors.BLUE}[+] Preparing the environment {Colors.RESET}")
    sleep(1)

    # 1. Installing Dependencies
    # Añadí lsd y w3m que tenías a medias en tu captura
    apps = " audacious cava eww rofi openbox thunar picom tint2 neofetch feh starship kitty lsd w3m"
    print(f"{Colors.BLUE}[+] Installing necessary packages...{Colors.RESET}")
    
    # IMPORTANTE: termux-setup-storage necesita interacción. Lo ideal es correrlo aparte,
    # pero aquí intentamos que no bloquee.
    run("termux-setup-storage") 
    
    run("pkg install x11-repo python python-pip git wget curl termux-x11-nightly pulseaudio firefox tur-repo zsh kitty termux-api virglrenderer-android fontconfig-utils freetype xfce4 jq lxappearance neovim-nightly rust -y")
    run(f"pkg install {apps} -y")
    run("pip install pyxdg pywal")
    run("cargo install pokeget")

    # 2. Creating base directories
    run("mkdir -p ~/.config")
    run("mkdir -p ~/.local/share/fonts")
    run("mkdir -p ~/.local/share/nvim") # Carpeta para tu nvim

    # 3. Deploying configuration files (.config)
    # Añadí gtk-3.0 aquí porque suele ir en .config
    config_items = [
        "audacious", "cava", "eww", "neofetch", "openbox",
        "picom", "rofi", "Thunar", "tint2", "Wallpaper", "starship.toml", "gtk-3.0"
    ]

    print(f"{Colors.GREEN}[+] Installing folders in ~/.config...{Colors.RESET}")
    for item in config_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/.config/")
            print(f"  -> {item} configurado.")

    # 4. Moving Executables to /usr/bin/
    executables = ["colortest-slim", "panes", "lavat"]
    BIN_PATH = "/data/data/com.termux/files/usr/bin"
    for exe in executables:
        exe_path = f"config/{exe}"
        if os.path.exists(exe_path):
            run(f"cp {exe_path} {BIN_PATH}/")
            run(f"chmod +x {BIN_PATH}/{exe}")

    # 5. Installation of Fonts
    if os.path.isdir("fonts"):
        run("cp -r fonts/* ~/.local/share/fonts/")
        run("fc-cache -fv > /dev/null")

    # 6. Display Themes, Icons, Zsh, Cache and NVIM
    # Agregamos 'nvim' a la lista para moverlo a ~/.local/share/
    dot_items = [".themes", ".icons", ".cache", ".zsh", ".zshrc"]
    
    print(f"{Colors.BLUE}[+] Installing system files...{Colors.RESET}")
    for item in dot_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/")
            print(f"  -> {item} desplegado en ~")

    # Caso especial para NVIM en ~/.local/share/
    if os.path.exists("config/nvim"):
        run("cp -r config/nvim ~/.local/share/")
        print("  -> nvim desplegado en ~/.local/share/")

    # 7. Shell and Terminal Tweaks
    print(f"{Colors.BLUE}[+] Finalizing shell configuration...{Colors.RESET}")
    
    # Instalar Oh My Zsh (sin que bloquee el script)
    run('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
    run("chsh -s zsh")

    # Configuración de fuente para la terminal de Termux
    if os.path.exists("config/CascadiaCode.zip"):
        run("mkdir -p ~/.termux")
        run("cp config/CascadiaCode.zip ~/.termux/")
        run("cd ~/.termux && unzip -o CascadiaCode.zip && mv CaskaydiaCoveNerdFont-Italic.ttf font.ttf")
        run("termux-reload-settings")

    print(f"\n{Colors.GREEN}Installation completed successfully!{Colors.RESET}")
    print(f"{Colors.BLUE}Keytaro, tu setup está listo. Reinicia Termux.{Colors.RESET}")

if __name__ == "__main__":
    main()
