#!/bin/bash

# Capture the argument sent by Eww (logout, reboot, poweroff)
ACTION="$1"

case "$ACTION" in
    "logout")
        # Close Openbox cleanly using its native exit command
        openbox --exit
        ;;

    "reboot")
        # Close the current Openbox instance and launch the startup script
        # Note: Openbox also has 'openbox --restart' if you ever just want to reload the WM
        pkill -9 openbox
        ~/startopenbox_termux.sh &
        ;;

    "poweroff")
        # Close the entire graphical environment in Termux-X11
        pkill -9 openbox
        pkill -9 termux-x11
        ;;

    *)
        echo "Correct use: $0 {logout|reboot|poweroff}"
        exit 1
        ;;
esac

