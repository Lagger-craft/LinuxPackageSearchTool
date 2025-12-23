#!/usr/bin/env python3

# Linux Package Search Tool - Sistema de configuración
# Copyright (C) 2025  Lagger-craft
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import json
import os


class ConfigManager:
    """Maneja la configuración persistente de la aplicación"""

    def __init__(self, config_file="config.json"):
        """Inicializa el gestor de configuración"""
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        """Carga la configuración desde el archivo JSON"""
        default_config = {
            "theme": "nier_automata",
            "last_search": "",
            "max_results": 10,
        }

        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    loaded_config = json.load(f)
                    # Combinar con defaults para claves faltantes
                    return {**default_config, **loaded_config}
            except (json.JSONDecodeError, IOError):
                print("Error al cargar configuración, usando valores por defecto")
                return default_config
        else:
            # Crear archivo de configuración con valores por defecto
            self._save_config(default_config)
            return default_config

    def _save_config(self, config=None):
        """Guarda la configuración en el archivo JSON"""
        if config is None:
            config = self.config

        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            return True
        except IOError:
            print("Error al guardar configuración")
            return False

    def get(self, key, default=None):
        """Obtiene un valor de configuración"""
        return self.config.get(key, default)

    def set(self, key, value):
        """Establece un valor de configuración"""
        self.config[key] = value
        return self._save_config()

    def get_theme(self):
        """Obtiene el tema actual"""
        return self.get("theme", "nier_automata")

    def set_theme(self, theme_name):
        """Establece el tema actual"""
        return self.set("theme", theme_name)

    def get_last_search(self):
        """Obtiene la última búsqueda"""
        return self.get("last_search", "")

    def set_last_search(self, search_term):
        """Establece la última búsqueda"""
        return self.set("last_search", search_term)

    def get_max_results(self):
        """Obtiene el máximo de resultados a mostrar"""
        return self.get("max_results", 10)

    def set_max_results(self, max_results):
        """Establece el máximo de resultados"""
        return self.set("max_results", max_results)

    def reset_to_defaults(self):
        """Restablece la configuración a valores por defecto"""
        default_config = {
            "theme": "nier_automata",
            "last_search": "",
            "max_results": 10,
        }
        self.config = default_config
        return self._save_config(default_config)
