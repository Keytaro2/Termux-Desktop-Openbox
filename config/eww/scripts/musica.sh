#!/data/data/com.termux/files/usr/bin/bash

# Ruta fija donde Eww buscará SIEMPRE la imagen actual
COVER_TMP="/data/data/com.termux/files/home/.config/eww/assets/current_cover.jpg"
# Imagen por defecto (puedes usar tu gato aquí)
DEFAULT_IMG="/data/data/com.termux/files/home/.config/eww/assets/digital-art-cat-pattern.jpg"

mkdir -p "$(dirname "$COVER_TMP")"

# 1. Obtener la URL del arte desde audacious
# Suele devolver algo como "file:///ruta/a/la/imagen.jpg"
raw_url=$(audtool current-song-tuple-data art-url 2>/dev/null)

# 2. Limpiar la URL (quitar el file:// del principio)
real_path=${raw_url#file://}

# 3. Si el archivo existe, lo copiamos a la ruta fija
if [[ -f "$real_path" ]]; then
    cp "$real_path" "$COVER_TMP" 2>/dev/null
    echo "$COVER_TMP"
else
    # Si no hay portada en la canción, mostramos tu imagen de gato
    echo "$DEFAULT_IMG"
fi
