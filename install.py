import os
import sys
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
    print(f"{Colors.BLUE}[+] Preparing the environment...... {Colors.RESET}")
    sleep(1)

    # 1. Installation of Dependencies
    apps = " audacious cava eww rofi openbox thunar picom tint2 neofetch feh starship kitty lsd w3m"
    print(f"{Colors.BLUE}[+] Installing necessary packages...{Colors.RESET}")
    run("pkg install x11-repo python python-pip git wget curl termux-x11-nightly pulseaudio firefox tur-repo zsh kitty termux-api virglrenderer-android fontconfig-utils freetype xfce4 jq lxappearance neovim-nightly rust chafa -y")
    run(f"pkg install {apps} -y")
    run("pip install pyxdg pywal")
    run("cargo install pokeget")

    # 2. Creating base directories
    run("mkdir -p ~/.config")
    run("mkdir -p ~/.local/share/fonts")
    run("mkdir -p ~/.local/share/nvim")

    # 3. Deploy configurations (.config)
    config_items = [
        "audacious", "cava", "eww", "neofetch", "openbox",
        "picom", "rofi", "thunar", "tint2", "Wallpaper", "gtk-3.0"
    ]
    for item in config_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/.config/")

    # 4. Move Executables to /usr/bin/
    executables = ["colortest-slim", "panes", "lavat"]
    BIN_PATH = "/data/data/com.termux/files/usr/bin"
    for exe in executables:
        exe_path = f"config/{exe}"
        if os.path.exists(exe_path):
            run(f"cp {exe_path} {BIN_PATH}/")
            run(f"chmod +x {BIN_PATH}/{exe}")

    # 5. Fonts and Appearance
    if os.path.isdir("fonts"):
        run("cp -r fonts/* ~/.local/share/fonts/")
        run("fc-cache -fv > /dev/null")

    dot_items = [".themes", ".icons", ".cache"]
    for item in dot_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/")

    if os.path.exists("config/nvim"):
        run("cp -r config/nvim ~/.local/share/")

    # 6. Source for Termux
    font_src = "config/CaskaydiaCoveNerdFont-BoldItalic.ttf"
    if os.path.exists(font_src):
        run("mkdir -p ~/.termux")
        run(f"cp {font_src} ~/.termux/font.ttf")
        run("termux-reload-settings")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ctrl + C is captured and the script closes without console errors
        print(f"\n{Colors.PINK}[!] Installation cancelled {Colors.RESET}")
        sys.exit(0)
