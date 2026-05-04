#!/data/data/com.termux/files/usr/bin/bash

CACHE="/data/data/com.termux/files/home/.brightness_val"

# Si el archivo no existe, creamos uno al 50% (127)
if [ ! -f "$CACHE" ]; then
    echo "127" > "$CACHE"
fi

# Leemos el valor y lo convertimos a porcentaje para Eww
val=$(cat "$CACHE")
echo $(( val * 100 / 255 ))
