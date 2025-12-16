#!/usr/bin/env python3

import subprocess

print("Hola, vamos a buscar paquetes de pacman")

# Ejecutamos el comando pacman -Q y capturamos la salida
resultado = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)

print(f"El comando retornó: {resultado.returncode}")

# 1. Limpiar todas las líneas (quitar vacías)
todas_las_lineas = [linea for linea in resultado.stdout.split("\n") if linea.strip()]

print(f"Total de paquetes instalados: {len(todas_las_lineas)}")

# 2. Filtrar los paquetes que el usuario decida con input()
buscar = input("Filtra el paquete para saber si esta instalado: ").lower()

if buscar == "":
    # Si no escribe nada, mostrar primeros 10
    print("\n📋 Primeros 10 paquetes instalados:")
    for i, linea in enumerate(todas_las_lineas[:10], 1):
        print(f"{i:2d}. {linea}")
else:
    # Si busca algo, filtrar y mostrar resultados
    paquetes_filtrados = [
        linea for linea in todas_las_lineas if buscar in linea.lower()
    ]
    print(f"\n🔍 Buscando '{buscar}': {len(paquetes_filtrados)} resultados")
    for i, linea in enumerate(paquetes_filtrados[:10], 1):
        print(f"{i:2d}. {linea}")
