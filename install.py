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
    apps = " audacious cava eww rofi openbox thunar picom tint2 neofetch feh starship kitty"
    print(f"{Colors.BLUE}[+] Installing necessary packages...{Colors.RESET}")
    run("pkg install x11-repo python python-pip git wget curl termux-x11-nightly pulseaudio firefox tur-repo zsh kitty termux-api virglrenderer-android fontconfig-utils freetype xfce4 jq lxappearance neovim-nightly rust -y")
    run(f"pkg install {apps} -y")
    run(f"pip install pyxdg pywal")
    run(f"cargo install pokeget")

    # 2. Creating base directories
    run("mkdir -p ~/.config")
    run("mkdir -p ~/.local/share/fonts")

    # 3. Deploying configuration files (.config)
    config_items = [
        "audacious", "cava", "eww", "neofetch", "openbox",
        "picom", "rofi", "thunar", "tint2", "Wallpaper", "starship.toml"
    ]

    print(f"{Colors.GREEN}[+] Installing folders in ~/.config...{Colors.RESET}")
    for item in config_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/.config/")
            print(f"  -> {item} configurado.")
        else:
            print(f"  {Colors.PINK}[!] Omitted: {item} not found in config folder{Colors.RESET}")

    # 4. Moving Executables to /usr/bin/
    executables = ["colortest-slim", "panes", "lavat"]
    BIN_PATH = "/data/data/com.termux/files/usr/bin"

    print(f"{Colors.BLUE}[+] Configuring global executables...{Colors.RESET}")
    for exe in executables:
        exe_path = f"config/{exe}"
        if os.path.exists(exe_path):
            run(f"cp {exe_path} {BIN_PATH}/")
            run(f"chmod +x {BIN_PATH}/{exe}")
            print(f"  -> {exe} moved to {BIN_PATH}")
        else:
            print(f"  {Colors.PINK}[!] Executable not found: {exe}{Colors.RESET}")

    # 5. Installation of Fonts
    if os.path.isdir("fonts"):
        print(f"{Colors.BLUE}[+] Installing fonts on the system...{Colors.RESET}")
        run("cp -r fonts/* ~/.local/share/fonts/")
        run("fc-cache -fv > /dev/null")
        print(f"  -> Updated sources.")

    # 6. Display Themes, Icons, Zsh and Cache on the HOME (~)
    dot_items = [".themes", ".icons", ".cache", ".zsh", ".zshrc"]

    print(f"{Colors.BLUE}[+] Installing system files from config/ to ~...{Colors.RESET}")
    for item in dot_items:
        path = f"config/{item}"
        if os.path.exists(path):
            run(f"cp -r {path} ~/")
            print(f"  -> {item} deployed in ~")
        else:
            print(f"{Colors.PINK}[!] Omitted: {item} was not found in config/ folder.{Colors.RESET}")

    print(f"\n{Colors.GREEN}Installation completed successfully!{Colors.RESET}")
    print(f"{Colors.BLUE}You can now use your commands: colortest-slim, panes and lavat.{Colors.RESET}")

if __name__ == "__main__":
    main()
