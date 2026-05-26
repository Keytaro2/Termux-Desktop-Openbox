#!/data/data/com.termux/files/usr/bin/bash

# 1. Intentamos leer los sensores de hardware directamente (rápido y siempre exacto)
if [ -f /sys/class/leds/lcd-backlight/brightness ]; then
    val=$(cat /sys/class/leds/lcd-backlight/brightness)
    max=$(cat /sys/class/leds/lcd-backlight/max_brightness)
elif [ -f /sys/class/backlight/panel0-backlight/brightness ]; then
    val=$(cat /sys/class/backlight/panel0-backlight/brightness)
    max=$(cat /sys/class/backlight/panel0-backlight/max_brightness)
else
    # 2. Si no hay acceso al hardware, usamos el lector nativo de Android
    val=$(content query --uri content://settings/system --where "name='screen_brightness'" | grep -o 'value=[0-9]*' | cut -d'=' -f2)
    max=255
fi

# Si por alguna razón extrema todo falla, mostramos 50% para que Eww no se rompa
if [ -z "$val" ]; then
    echo 50
    exit 0
fi

# Evitar divisiones por cero en caso de error
if [ -z "$max" ] || [ "$max" -eq 0 ]; then
    max=255
fi

# Convertimos el valor crudo al porcentaje (0 a 100)
echo $(( val * 100 / max ))

