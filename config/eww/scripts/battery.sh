#!/bin/bash
# Obtiene el porcentaje de batería
termux-battery-status | jq '.percentage'
