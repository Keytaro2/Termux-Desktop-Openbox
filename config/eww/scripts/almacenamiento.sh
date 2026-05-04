#!/data/data/com.termux/files/usr/bin/bash

case $1 in
    root)
        # Porcentaje de uso de la memoria interna
        df -h / | awk 'NR==2 {print $5}' | sed 's/%//'
        ;;
    free_root)
        # GB libres en memoria interna
        df -h / | awk 'NR==2 {print $4}'
        ;;
    cloud)
        echo "81"
        ;;
    free_cloud)
        echo "737 GB"
        ;;
esac
