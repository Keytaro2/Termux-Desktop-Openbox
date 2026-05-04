#!/data/data/com.termux/files/usr/bin/bash

# Obtener datos una sola vez para ahorrar recursos
stats=$(termux-volume)

# Extraer valores (quitamos los # y usamos jq)
vol=$(echo "$stats" | jq '.[] | select(.stream == "music") | .volume' 2>/dev/null)
max=$(echo "$stats" | jq '.[] | select(.stream == "music") | .max_volume' 2>/dev/null)

# Validar que obtuvimos números
if [[ -z "$vol" ]] || [[ -z "$max" ]] || [[ "$max" -eq 0 ]]; then
    echo "󰝟 0"
    exit 0
fi

# Calcular porcentaje
percent=$(( vol * 100 / max ))

# Elegir icono Nerd Font
#if [ "$percent" -eq 0 ]; then
 #   icon="󰝟"
#elif [ "$percent" -lt 33 ]; then
#    icon="󰕿"
#elif [ "$percent" -lt 66 ]; then
#    icon="󰖀"
#else
#    icon="󰕾"
#fi

echo "$percent"
