#!/usr/bin/env python3
"""
Sistema de temas para Linux Package Search Tool
Inspirado en Slime Rancher 2 y Nier Automata
"""


class ThemeManager:
    """Maneja los temas de colores para la aplicación"""

    # Definición de temas
    THEMES = {
        "nier_automata": {
            "name": "Nier Automata",
            "description": "Elegante y sombrío - estilo futurista",
            "menu": "\033[36m",  # Cian suave
            "title": "\033[33m",  # Amarillo suave
            "success": "\033[32m",  # Verde oscuro
            "results": "\033[35m",  # Magenta oscuro
            "error": "\033[31m",  # Rojo oscuro
            "input": "\033[37m",  # Blanco
            "highlight": "\033[33m",  # Amarillo para destacar
            "reset": "\033[0m",
        },
        "slime_rancher": {
            "name": "Slime Rancher 2",
            "description": "Vibrante y colorido - estilo aventura",
            "menu": "\033[96m",  # Cian brillante
            "title": "\033[93m",  # Amarillo brillante
            "success": "\033[92m",  # Verde brillante
            "results": "\033[95m",  # Magenta brillante
            "error": "\033[91m",  # Rojo brillante
            "input": "\033[97m",  # Blanco brillante
            "highlight": "\033[93m",  # Amarillo brillante
            "reset": "\033[0m",
        },
    }

    def __init__(self, theme_name="nier_automata"):
        """Inicializa con un tema específico"""
        self.current_theme = theme_name
        self.colors = self.THEMES.get(theme_name, self.THEMES["nier_automata"])

    def get_color(self, color_name):
        """Obtiene un color específico del tema actual"""
        return self.colors.get(color_name, "")

    def show_preview(self, theme_name):
        """Muestra vista previa de un tema específico"""
        if theme_name not in self.THEMES:
            return False

        theme = self.THEMES[theme_name]
        c = theme  # Alias para más corto

        print(f"\n{c['title']}🎨 VISTA PREVIA: {theme['name']}{c['reset']}")
        print(f"{c['description']}")
        print(f"\n{c['menu']}╔═══════════════════════════════════════╗{c['reset']}")
        print(
            f"{c['menu']}║{c['title']}     🔍 LINUX PACKAGE SEARCH TOOL     {c['menu']}║{c['reset']}"
        )
        print(f"{c['menu']}╠═══════════════════════════════════════╣{c['reset']}")
        print(
            f"{c['menu']}║{c['success']} ✅ Búsqueda exitosa: 56 resultados     {c['menu']}║{c['reset']}"
        )
        print(
            f"{c['menu']}║{c['results']}   1. python 3.13.11-2               {c['menu']}║{c['reset']}"
        )
        print(
            f"{c['menu']}║{c['results']}   2. vivaldi 7.7.3851.61-2.1        {c['menu']}║{c['reset']}"
        )
        print(
            f"{c['menu']}║{c['error']} ❌ Error: Comando no encontrado        {c['menu']}║{c['reset']}"
        )
        print(f"{c['menu']}╚═══════════════════════════════════════╝{c['reset']}")

        return True

    def list_themes(self):
        """Lista todos los temas disponibles"""
        print(
            f"\n{self.get_color('title')}🎨 TEMAS DISPONIBLES:{self.get_color('reset')}"
        )
        for i, (key, theme) in enumerate(self.THEMES.items(), 1):
            print(
                f"{self.get_color('menu')}{i}.{self.get_color('reset')} {theme['name']} - {theme['description']}"
            )

    def switch_theme(self, theme_name):
        """Cambia al tema especificado"""
        if theme_name in self.THEMES:
            self.current_theme = theme_name
            self.colors = self.THEMES[theme_name]
            return True
        return False

    def format_menu_item(self, text, color_name="menu"):
        """Formatea texto para menús"""
        return f"{self.get_color(color_name)}{text}{self.get_color('reset')}"

    def format_success(self, text):
        """Formatea texto de éxito"""
        return f"{self.get_color('success')}{text}{self.get_color('reset')}"

    def format_error(self, text):
        """Formatea texto de error"""
        return f"{self.get_color('error')}{text}{self.get_color('reset')}"

    def format_title(self, text):
        """Formatea texto de título"""
        return f"{self.get_color('title')}{text}{self.get_color('reset')}"

    def format_results(self, text):
        """Formatea texto de resultados"""
        return f"{self.get_color('results')}{text}{self.get_color('reset')}"
