#!/bin/bash

# Verifica si la ventana w_music está actualmente en la lista de ventanas activas
if eww --config ~/.config/eww/dashboard active-windows | grep -q "w_music"; then
    # Si está abierta, cerramos todas las ventanas
    eww --config ~/.config/eww/dashboard close w_music w_config w_system w_memory w_clock w_calendar
else
    # Si está cerrada, abrimos todas las ventanas
    eww --config ~/.config/eww/dashboard open-many w_music w_config w_system w_memory w_clock w_calendar
fi
