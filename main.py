#!/usr/bin/env python3

import subprocess


def mostrar_menu():
    """Muestra el menú principal y devuelve la opción seleccionada"""
    print("\n" + "=" * 50)
    print("🔍 LINUX PACKAGE SEARCH TOOL")
    print("=" * 50)
    print("1. Buscar paquetes Pacman")
    print("2. Buscar aplicaciones Flatpak")
    print("0. Salir")
    print("=" * 50)
    return input("Seleccioná una opción: ")


def buscar_pacman():
    """Busca paquetes instalados con pacman"""
    print("\n--- 🔍 BÚSQUEDA CON PACMAN ---")

    # Ejecutar comando pacman -Q
    resultado = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)

    if resultado.returncode != 0:
        print("❌ Error al ejecutar pacman -Q")
        return

    # Limpiar líneas vacías
    todas_las_lineas = [
        linea for linea in resultado.stdout.split("\n") if linea.strip()
    ]

    print(f"Total de paquetes instalados: {len(todas_las_lineas)}")

    # Input del usuario
    buscar = input("Filtra el paquete para saber si está instalado: ").lower()

    if buscar == "":
        # Mostrar primeros 10
        print("\n📋 Primeros 10 paquetes instalados:")
        for i, linea in enumerate(todas_las_lineas[:10], 1):
            print(f"{i:2d}. {linea}")
    else:
        # Filtrar y mostrar resultados
        paquetes_filtrados = [
            linea for linea in todas_las_lineas if buscar in linea.lower()
        ]
        print(f"\n🔍 Buscando '{buscar}': {len(paquetes_filtrados)} resultados")
        for i, linea in enumerate(paquetes_filtrados[:10], 1):
            print(f"{i:2d}. {linea}")


def buscar_flatpak():
    """Busca aplicaciones instaladas con flatpak"""
    print("\n--- 🔍 BÚSQUEDA CON FLATPAK ---")

    # Ejecutar comando flatpak list --app
    resultado = subprocess.run(
        ["flatpak", "list", "--app"], capture_output=True, text=True
    )

    if resultado.returncode != 0:
        print("❌ Error al ejecutar flatpak list --app")
        return

    # Limpiar líneas vacías
    lineas_limpias = [linea for linea in resultado.stdout.split("\n") if linea.strip()]

    # Extraer nombre y versión
    apps_formateadas = []
    for linea in lineas_limpias:
        partes = linea.split("\t")
        if len(partes) >= 3:
            nombre = partes[0]
            version = partes[2]
            apps_formateadas.append(f"{nombre} {version}")

    print(f"Total de aplicaciones Flatpak: {len(apps_formateadas)}")

    # Input del usuario
    buscar = input("Filtra la app de flatpak: ").lower()

    if buscar == "":
        # Mostrar todas las apps
        print(f"\n📋 Todas las apps Flatpak ({len(apps_formateadas)}):")
        for i, app in enumerate(apps_formateadas[:10], 1):
            print(f"{i:2d}. {app}")
    else:
        # Filtrar y mostrar resultados
        apps_filtradas = [app for app in apps_formateadas if buscar in app.lower()]
        print(f"\n🔍 Buscando '{buscar}': {len(apps_filtradas)} resultados")
        for i, app in enumerate(apps_filtradas[:10], 1):
            print(f"{i:2d}. {app}")


def main():
    """Función principal del programa"""
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            buscar_pacman()
        elif opcion == "2":
            buscar_flatpak()
        elif opcion == "0":
            print("\n¡Chau! 👋")
            break
        else:
            print("\n❌ Opción inválida. Intentá de nuevo.")


if __name__ == "__main__":
    main()
