# 🔍 Linux Package Search Tool

Herramienta profesional y personalizable para buscar paquetes instalados en tu sistema Linux con soporte para múltiples gestores de paquetes y temas personalizables.

## 🌟 Características Principales

- 🎨 **Sistema de temas dual** (Nier Automata + Slime Rancher 2)
- 🔍 **Múltiples gestores**: Pacman, Flatpak, Yay, Paru
- 💾 **Configuración persistente** con JSON
- 🔄 **Reinicio automático** al cambiar temas
- 🎯 **Búsquedas case-insensitive**
- 📋 **Resultados numerados** y formateados
- 🛠️ **Temas personalizables** (tutorial incluido)

## 🛠️ Requisitos

- **Python 3.6+** instalado
- **Distribución basada en Arch Linux** (con pacman)
- **Gestores opcionales**: flatpak, yay, paru
- **Permisos de ejecución** para el script

## 🚀 Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/Lagger-craft/LinuxPackageSearchTool.git
cd searchAppInstalled-Linux
```

### 2. Dar permisos de ejecución (opcional)

```bash
chmod +x main.py
```

### 3. Ejecutar la herramienta

```bash
# Opción 1: Con Python
python3 main.py

# Opción 2: Directamente (si diste permisos)
./main.py
```

## 🎨 Temas Disponibles

### 🌌 Nier Automata (Default)
*Elegante y sombrío - estilo futurista*

**Paleta de colores:**
- Menú: Cian suave (`\033[36m`)
- Títulos: Amarillo suave (`\033[33m`)
- Éxitos: Verde oscuro (`\033[32m`)
- Resultados: Magenta oscuro (`\033[35m`)
- Errores: Rojo oscuro (`\033[31m`)

**Vista previa:**
```
═════════════════════════════════════════════════
🔍 LINUX PACKAGE SEARCH TOOL
═════════════════════════════════════════════════
1. Buscar paquetes Pacman
2. Buscar aplicaciones Flatpak
3. Buscar paquetes Yay (AUR)
4. Buscar paquetes Paru (AUR)
5. Cambiar tema de colores
0. Salir
═════════════════════════════════════════════════
```

### 🌈 Slime Rancher 2
*Vibrante y colorido - estilo aventura*

**Paleta de colores:**
- Menú: Cian brillante (`\033[96m`)
- Títulos: Amarillo brillante (`\033[93m`)
- Éxitos: Verde brillante (`\033[92m`)
- Resultados: Magenta brillante (`\033[95m`)
- Errores: Rojo brillante (`\033[91m`)

**Vista previa:**
```
═════════════════════════════════════════════════
🔍 LINUX PACKAGE SEARCH TOOL
═════════════════════════════════════════════════
1. Buscar paquetes Pacman
2. Buscar aplicaciones Flatpak
3. Buscar paquetes Yay (AUR)
4. Buscar paquetes Paru (AUR)
5. Cambiar tema de colores
0. Salir
═════════════════════════════════════════════════
```

## 🛠️ Crear Temas Personalizados

### Paso 1: Definir tu paleta de colores

Crea tu tema personalizado siguiendo esta estructura:

```python
mi_tema_personalizado = {
    'name': 'Mi Tema Personalizado',
    'description': 'Descripción única de mi tema',
    'menu': '\033[96m',      # Color para menús y opciones
    'title': '\033[93m',     # Color para títulos principales
    'success': '\033[92m',   # Color para mensajes de éxito
    'results': '\033[95m',   # Color para resultados de búsqueda
    'error': '\033[91m',     # Color para mensajes de error
    'input': '\033[97m',     # Color para inputs del usuario
    'highlight': '\033[93m', # Color para texto destacado
    'reset': '\033[0m'       # Reset de color (obligatorio)
}
```

### Paso 2: Agregar tu tema a colors.py

Abre el archivo `colors.py` y agrega tu tema al diccionario `THEMES`:

```python
THEMES = {
    'nier_automata': { ... },
    'slime_rancher': { ... },
    'mi_tema_personalizado': {  # ← Tu nuevo tema
        'name': 'Mi Tema Personalizado',
        'description': 'Descripción única de mi tema',
        'menu': '\033[96m',
        'title': '\033[93m',
        'success': '\033[92m',
        'results': '\033[95m',
        'error': '\033[91m',
        'input': '\033[97m',
        'highlight': '\033[93m',
        'reset': '\033[0m'
    }
}
```

### Paso 3: Actualizar el menú de temas

En `main.py`, agrega tu tema al menú de selección:

```python
elif opcion == "3":  # Siguiente número disponible
    self.theme.show_preview('mi_tema_personalizado')
    confirmar = input(c.format_menu_item('¿Aplicar este tema? (s/n): ')).lower()
    if confirmar == 's':
        self.theme.switch_theme('mi_tema_personalizado')
        self.config.set_theme('mi_tema_personalizado')
        print(c.format_success('✅ Mi Tema Personalizado aplicado'))
        self.reiniciar_aplicacion()
        break
```

## 🎨 Referencia de Colores ANSI

### Colores Básicos
```python
NEGRO    = '\033[30m'  # Negro
ROJO     = '\033[31m'  # Rojo
VERDE    = '\033[32m'  # Verde
AMARILLO = '\033[33m'  # Amarillo
AZUL     = '\033[34m'  # Azul
MAGENTA  = '\033[35m'  # Magenta
CIAN     = '\033[36m'  # Cian
BLANCO   = '\033[37m'  # Blanco
```

### Colores Brillantes
```python
NEGRO_BRILLANTE    = '\033[90m'  # Gris oscuro
ROJO_BRILLANTE     = '\033[91m'  # Rojo brillante
VERDE_BRILLANTE    = '\033[92m'  # Verde brillante
AMARILLO_BRILLANTE = '\033[93m'  # Amarillo brillante
AZUL_BRILLANTE     = '\033[94m'  # Azul brillante
MAGENTA_BRILLANTE  = '\033[95m'  # Magenta brillante
CIAN_BRILLANTE     = '\033[96m'  # Cian brillante
BLANCO_BRILLANTE   = '\033[97m'  # Blanco brillante
```

### Estilos de Texto
```python
NEGRITA   = '\033[1m'   # Texto en negrita
SUBRAYADO = '\033[4m'   # Texto subrayado
INVERTIDO = '\033[7m'   # Colores invertidos
RESET     = '\033[0m'   # Reset de todos los estilos
```

## ⚙️ Configuración Avanzada

### Archivo config.json

El archivo `config.json` se crea automáticamente y contiene:

```json
{
  "theme": "nier_automata",
  "last_search": "python",
  "max_results": 10
}
```

### Opciones de configuración

- **theme**: Tema actual (`nier_automata` o `slime_rancher`)
- **last_search**: Última búsqueda realizada
- **max_results**: Máximo de resultados a mostrar (futuro)

### Editar configuración manualmente

Puedes editar directamente `config.json` para personalizar:

```json
{
  "theme": "slime_rancher",
  "last_search": "",
  "max_results": 20
}
```

## 💡 Ejemplos de Uso

### Menú principal
```
═════════════════════════════════════════════════
🔍 LINUX PACKAGE SEARCH TOOL
═════════════════════════════════════════════════
1. Buscar paquetes Pacman
2. Buscar aplicaciones Flatpak
3. Buscar paquetes Yay (AUR)
4. Buscar paquetes Paru (AUR)
5. Cambiar tema de colores
0. Salir
═════════════════════════════════════════════════
Seleccioná una opción:
```

### Búsqueda con resultados
```
--- 🔍 BÚSQUEDA CON PACMAN ---
Total de paquetes instalados: 1382
Filtra el paquete para saber si está instalado: python

🔍 Buscando "python": 56 resultados
 1. illogical-impulse-python 1.1-4
 2. lib32-python311-bin 3.11.8-6
 3. python 3.13.11-2
 4. python-annotated-types 0.7.0-2
 ...
```

### Cambio de tema
```
--- 🎨 MENÚ DE TEMAS ---

🎨 TEMAS DISPONIBLES:
1. Nier Automata - Elegante y sombrío - estilo futurista
2. Slime Rancher 2 - Vibrante y colorido - estilo aventura
0. Volver al menú principal
Seleccioná un tema: 2

🎨 VISTA PREVIA: Slime Rancher 2
Vibrante y colorido - estilo aventura

╔═══════════════════════════════════════╗
║     🔍 LINUX PACKAGE SEARCH TOOL     ║
╠═══════════════════════════════════════╣
║ ✅ Búsqueda exitosa: 56 resultados     ║
║   1. python 3.13.11-2               ║
║   2. vivaldi 7.7.3851.61-2.1        ║
║ ❌ Error: Comando no encontrado        ║
╚═══════════════════════════════════════╝
¿Aplicar este tema? (s/n): s
✅ Tema Slime Rancher 2 aplicado
🔄 Reiniciando aplicación...
```

## 🚧 Próximas Mejoras

- [ ] **Búsqueda fuzzy** (similitud de texto)
- [ ] **Más temas predefinidos** (Dracula, Gruvbox, etc.)
- [ ] **Exportar resultados** a archivo (JSON, CSV, TXT)
- [ ] **Búsqueda por categoría** de paquetes
- [ ] **Integración con otros gestores** (dnf, apt, etc.)
- [ ] **Interfaz web** opcional
- [ ] **Plugin system** para extensiones

## 📝 Notas Técnicas

### Arquitectura del Proyecto

```
searchAppInstalled-Linux/
├── main.py          # Aplicación principal con clases
├── colors.py        # Sistema de temas y colores
├── config.py        # Gestión de configuración persistente
├── config.json      # Configuración del usuario (auto-creado)
└── README.md        # Documentación completa
```

### Tecnologías Utilizadas

- **Python 3.6+** - Lenguaje principal
- **subprocess.run()** - Ejecución segura de comandos
- **JSON** - Configuración persistente
- **Códigos ANSI** - Colores y estilos de terminal
- **OOP** - Programación Orientada a Objetos

### Patrones de Diseño

- **Single Responsibility** - Cada clase tiene una responsabilidad clara
- **Configuration Pattern** - Configuración externa en JSON
- **Theme Pattern** - Sistema de temas intercambiables
- **Error Handling** - Manejo robusto de errores

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el repositorio
2. Creá una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrí un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mirá el archivo [LICENSE](LICENSE) para detalles.

---

**Creado con ❤️ y 🎨 para facilitar la gestión de paquetes en Linux**

*Versión 3.1 - Documentación completa y tutorial de temas personalizados*