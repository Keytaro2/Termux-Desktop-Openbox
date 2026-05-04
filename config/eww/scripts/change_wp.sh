#!/bin/bash

# Directorio donde tienes tus imágenes
WP_DIR="$HOME/.config/Wallpaper"
# Lista de fondos (puedes añadir los que quieras)
WPS=("purple-tree.jpg" "wallhaven-3lvqq6.png" "water-anime-style.jpg" "a-wolf-in-the-cave-wallpaper-2560x1600_7.jpg" "moon-illuminating-sea.jpg" "a.png" "b.png" "test.png" "s4vitar.png")

# Obtener el índice actual
CACHE="$HOME/.cache/wp_index"
[ ! -f $CACHE ] && echo 0 > $CACHE
INDEX=$(cat $CACHE)

# Cambiar al siguiente
NEXT_INDEX=$(( (INDEX + 1) % ${#WPS[@]} ))
echo $NEXT_INDEX > $CACHE

# 1. Animación con Eww (Notificación)
eww update wall_text="Cambiando a ${WPS[$NEXT_INDEX]}"
eww open notifier
(sleep 1.5 && eww close notifier) &

# 2. Aplicar fondo con feh
feh --bg-fill "$WP_DIR/${WPS[$NEXT_INDEX]}"
