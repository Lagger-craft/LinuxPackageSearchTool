#!/usr/bin/env python3

import subprocess
import sys
import os
from colors import ThemeManager
from config import ConfigManager


class PackageSearchTool:
    """Herramienta de búsqueda de paquetes con sistema de temas"""

    def __init__(self):
        """Inicializa la herramienta con configuración y temas"""
        self.config = ConfigManager()
        self.theme = ThemeManager(self.config.get_theme())

    def mostrar_menu(self):
        """Muestra el menú principal con colores"""
        c = self.theme

        print(f"\n{c.format_title('═' * 50)}")
        print(f"{c.format_title('🔍 LINUX PACKAGE SEARCH TOOL')}")
        print(f"{c.format_title('═' * 50)}")
        print(f"{c.format_menu_item('1. Buscar paquetes Pacman')}")
        print(f"{c.format_menu_item('2. Buscar aplicaciones Flatpak')}")
        print(f"{c.format_menu_item('3. Buscar paquetes Yay (AUR)')}")
        print(f"{c.format_menu_item('4. Buscar paquetes Paru (AUR)')}")
        print(f"{c.format_menu_item('5. Cambiar tema de colores')}")
        print(f"{c.format_menu_item('0. Salir')}")
        print(f"{c.format_title('═' * 50)}")

        return input(f"{c.format_menu_item('Seleccioná una opción: ')}").lower()

    def buscar_pacman(self):
        """Busca paquetes instalados con pacman"""
        c = self.theme
        print(f"\n{c.format_title('--- 🔍 BÚSQUEDA CON PACMAN ---')}")

        resultado = subprocess.run(["pacman", "-Q"], capture_output=True, text=True)

        if resultado.returncode != 0:
            print(c.format_error("❌ Error al ejecutar pacman -Q"))
            return

        todas_las_lineas = [
            linea for linea in resultado.stdout.split("\n") if linea.strip()
        ]

        print(
            c.format_success(f"Total de paquetes instalados: {len(todas_las_lineas)}")
        )

        buscar = input(
            c.format_menu_item("Filtra el paquete para saber si está instalado: ")
        ).lower()

        # Guardar última búsqueda
        self.config.set_last_search(buscar)

        if buscar == "":
            print(f"\n{c.format_title('📋 Primeros 10 paquetes instalados:')}")
            for i, linea in enumerate(todas_las_lineas[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {linea}')}")
        else:
            paquetes_filtrados = [
                linea for linea in todas_las_lineas if buscar in linea.lower()
            ]
            print(
                f"\n{c.format_success(f'🔍 Buscando "{buscar}": {len(paquetes_filtrados)} resultados')}"
            )
            for i, linea in enumerate(paquetes_filtrados[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {linea}')}")

    def buscar_flatpak(self):
        """Busca aplicaciones instaladas con flatpak"""
        c = self.theme
        print(f"\n{c.format_title('--- 🔍 BÚSQUEDA CON FLATPAK ---')}")

        resultado = subprocess.run(
            ["flatpak", "list", "--app"], capture_output=True, text=True
        )

        if resultado.returncode != 0:
            print(c.format_error("❌ Error al ejecutar flatpak list --app"))
            return

        lineas_limpias = [
            linea for linea in resultado.stdout.split("\n") if linea.strip()
        ]

        apps_formateadas = []
        for linea in lineas_limpias:
            partes = linea.split("\t")
            if len(partes) >= 3:
                nombre = partes[0]
                version = partes[2]
                apps_formateadas.append(f"{nombre} {version}")

        print(
            c.format_success(f"Total de aplicaciones Flatpak: {len(apps_formateadas)}")
        )

        buscar = input(c.format_menu_item("Filtra la app de flatpak: ")).lower()

        if buscar == "":
            print(
                f"\n{c.format_title(f'📋 Todas las apps Flatpak ({len(apps_formateadas)}):')}"
            )
            for i, app in enumerate(apps_formateadas[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {app}')}")
        else:
            apps_filtradas = [app for app in apps_formateadas if buscar in app.lower()]
            print(
                f"\n{c.format_success(f'🔍 Buscando "{buscar}": {len(apps_filtradas)} resultados')}"
            )
            for i, app in enumerate(apps_filtradas[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {app}')}")

    def buscar_yay(self):
        """Busca paquetes instalados con yay (AUR)"""
        c = self.theme
        print(f"\n{c.format_title('--- 🔍 BÚSQUEDA CON YAY (AUR) ---')}")

        resultado = subprocess.run(["yay", "-Qm"], capture_output=True, text=True)

        if resultado.returncode != 0:
            print(c.format_error("❌ Error al ejecutar yay -Q"))
            return

        todas_las_lineas = [
            linea for linea in resultado.stdout.split("\n") if linea.strip()
        ]

        print(c.format_success(f"Total de paquetes AUR: {len(todas_las_lineas)}"))

        buscar = input(c.format_menu_item("Filtra el paquete AUR: ")).lower()

        if buscar == "":
            print(f"\n{c.format_title('📋 Primeros 10 paquetes AUR:')}")
            for i, linea in enumerate(todas_las_lineas[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {linea}')}")
        else:
            paquetes_filtrados = [
                linea for linea in todas_las_lineas if buscar in linea.lower()
            ]
            print(
                f"\n{c.format_success(f'🔍 Buscando "{buscar}": {len(paquetes_filtrados)} resultados')}"
            )
            for i, linea in enumerate(paquetes_filtrados[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {linea}')}")

    def buscar_paru(self):
        """Busca paquetes instalados con paru (AUR)"""
        c = self.theme
        print(f"\n{c.format_title('--- 🔍 BÚSQUEDA CON PARU (AUR) ---')}")

        resultado = subprocess.run(["paru", "-Qmq"], capture_output=True, text=True)

        if resultado.returncode != 0:
            print(c.format_error("❌ Error al ejecutar paru -Q"))
            return

        todas_las_lineas = [
            linea for linea in resultado.stdout.split("\n") if linea.strip()
        ]

        print(c.format_success(f"Total de paquetes AUR: {len(todas_las_lineas)}"))

        buscar = input(c.format_menu_item("Filtra el paquete AUR: ")).lower()

        if buscar == "":
            print(f"\n{c.format_title('📋 Primeros 10 paquetes AUR:')}")
            for i, linea in enumerate(todas_las_lineas[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {linea}')}")
        else:
            paquetes_filtrados = [
                linea for linea in todas_las_lineas if buscar in linea.lower()
            ]
            print(
                f"\n{c.format_success(f'🔍 Buscando "{buscar}": {len(paquetes_filtrados)} resultados')}"
            )
            for i, linea in enumerate(paquetes_filtrados[:10], 1):
                print(f"{c.format_results(f'{i:2d}. {linea}')}")

    def menu_temas(self):
        """Muestra el menú de cambio de temas"""
        c = self.theme

        while True:
            print(f"\n{c.format_title('--- 🎨 MENÚ DE TEMAS ---')}")
            self.theme.list_themes()
            print(f"{c.format_menu_item('0. Volver al menú principal')}")

            opcion = input(c.format_menu_item("Seleccioná un tema: ")).lower()

            if opcion == "0":
                break
            elif opcion == "1":
                self.theme.show_preview("nier_automata")
                confirmar = input(
                    c.format_menu_item("¿Aplicar este tema? (s/n): ")
                ).lower()
                if confirmar == "s":
                    self.theme.switch_theme("nier_automata")
                    self.config.set_theme("nier_automata")
                    print(c.format_success("✅ Tema Nier Automata aplicado"))
                    self.reiniciar_aplicacion()
                    break
            elif opcion == "2":
                self.theme.show_preview("slime_rancher")
                confirmar = input(
                    c.format_menu_item("¿Aplicar este tema? (s/n): ")
                ).lower()
                if confirmar == "s":
                    self.theme.switch_theme("slime_rancher")
                    self.config.set_theme("slime_rancher")
                    print(c.format_success("✅ Tema Slime Rancher 2 aplicado"))
                    self.reiniciar_aplicacion()
                    break
            else:
                print(c.format_error("❌ Opción inválida"))

    def reiniciar_aplicacion(self):
        """Reinicia la aplicación para aplicar cambios"""
        print(self.theme.format_success("🔄 Reiniciando aplicación..."))
        os.execv(sys.executable, ["python3"] + sys.argv)

    def main(self):
        """Función principal del programa"""
        while True:
            opcion = self.mostrar_menu()

            if opcion == "1":
                self.buscar_pacman()
            elif opcion == "2":
                self.buscar_flatpak()
            elif opcion == "3":
                self.buscar_yay()
            elif opcion == "4":
                self.buscar_paru()
            elif opcion == "5":
                self.menu_temas()
            elif opcion == "0":
                print(f"\n{self.theme.format_success('¡Chau! 👋')}")
                break
            else:
                print(
                    f"\n{self.theme.format_error('❌ Opción inválida. Intentá de nuevo.')}"
                )


if __name__ == "__main__":
    tool = PackageSearchTool()
    tool.main()
