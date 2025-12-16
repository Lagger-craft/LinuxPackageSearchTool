# 🔍 Linux Package Search Tool

Herramienta simple y eficiente para buscar paquetes instalados en tu sistema Linux mediante pacman.

## 📋 ¿Qué hace?

Esta herramienta te permite:
- Buscar paquetes instalados en tu sistema Arch Linux
- Realizar búsquedas case-insensitive (no distingue mayúsculas/minúsculas)
- Ver los primeros 10 paquetes si no especificas una búsqueda
- Obtener resultados numerados y fáciles de leer

## 🛠️ Requisitos

- **Python 3.6+** instalado
- **Distribución basada en Arch Linux** (con pacman)
- **Permisos de ejecución** para el script

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone <URL-del-repositorio>
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

## 💡 Ejemplos de Uso

### Buscar un paquete específico
```
Filtra el paquete para saber si esta instalado: vivaldi

🔍 Buscando 'vivaldi': 1 resultados
 1. vivaldi 7.7.3851.61-2.1
```

### Ver primeros paquetes (búsqueda vacía)
```
Filtra el paquete para saber si esta instalado: 

📋 Primeros 10 paquetes instalados:
 1. a52dec 0.8.0-2.1
 2. aalib 1.4rc5-19.1
 3. aardvark-dns 1.17.0-1.1
 ...
```

### Búsqueda case-insensitive
```
Filtra el paquete para saber si esta instalado: VIVALDI

🔍 Buscando 'vivaldi': 1 resultados
 1. vivaldi 7.7.3851.61-2.1
```

## 🚧 Próximas Mejoras

- [ ] Soporte para **yay** (paquetes AUR)
- [ ] Soporte para **paru** (paquetes AUR)
- [ ] Soporte para **flatpak**
- [ ] Búsqueda fuzzy (similitud de texto)
- [ ] Interfaz con colores
- [ ] Exportar resultados a archivo
- [ ] Compatibilidad con otras distribuciones Linux

## 📝 Notas Técnicas

- Utiliza `subprocess.run()` para ejecutar comandos del sistema de forma segura
- Procesa la salida de `pacman -Q` para obtener la lista de paquetes
- Implementa filtrado case-insensitive mediante `.lower()`
- Limita los resultados a 10 para mejor legibilidad

---

**Creado con ❤️ para facilitar la gestión de paquetes en Linux**