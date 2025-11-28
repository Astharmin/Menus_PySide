# 🎯 PySide6 Menu Application - README

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![GUI](https://img.shields.io/badge/GUI_Application-FF6B35?style=for-the-badge)
![Desktop](https://img.shields.io/badge/Desktop_App-1572B6?style=for-the-badge)

**Aplicación de escritorio moderna** desarrollada con PySide6 que demuestra la creación de interfaces gráficas profesionales con menús y barras de herramientas.

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![PySide6](https://img.shields.io/badge/PySide6-Latest-green)](https://pypi.org/project/PySide6/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

</div>

## 📖 Descripción del Proyecto

Esta aplicación es una **demostración práctica** de cómo crear interfaces de usuario profesionales usando PySide6 (Qt for Python). El proyecto muestra la implementación de una ventana principal con barra de herramientas, menús interactivos y gestión de estados - componentes esenciales para aplicaciones de escritorio modernas.

## ✨ Características Principales

### 🎨 **Interfaz de Usuario**
- **Barra de herramientas personalizable** con iconos y texto
- **Múltiples estilos de botones** configurables
- **Barra de estado informativa** con tooltips
- **Iconos personalizados** para acciones comunes

### ⚡ **Funcionalidades**
- **Acciones de menú** completamente funcionales (Nuevo, Guardar, Información)
- **Sistema de tooltips** para mejor experiencia de usuario
- **Manejo de eventos** con señales y slots
- **Arquitectura modular** y escalable

### 🛠 **Técnicas Implementadas**
- **PySide6/Qt6** - Framework moderno para GUI
- **Programación orientada a objetos** con herencia de QMainWindow
- **Manejo de recursos** (iconos, imágenes)
- **Personalización de widgets** Qt

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
# Instalar PySide6
pip install pyside6

# O instalar desde requirements.txt
pip install -r requirements.txt
```

### Estructura del Proyecto
```
pyside-menu-app/
├── 📁 main.py                 # Archivo principal de la aplicación
├── 📁 Src/                   # Recursos de la aplicación
│   ├── 📁 nuevo.png          # Icono acción "Nuevo"
│   ├── 📁 guardar.png        # Icono acción "Guardar"
│   └── 📁 acerca.png         # Icono acción "Información"
└── 📄 README.md              # Este archivo
```

## 🎯 Uso de la Aplicación

### Ejecución Básica
```bash
python main.py
```

### Características de la Interfaz

#### 🎮 **Barra de Herramientas**
La aplicación incluye una barra de herramientas con tres acciones principales:

| Acción | Icono | Función | Tooltip |
|--------|-------|---------|---------|
| **Nuevo** | 📄 | Crear nuevo archivo | "Nuevo Archivo" |
| **Guardar** | 💾 | Guardar archivo actual | "Guardar Archivo" |
| **Información** | ℹ️ | Mostrar información | "Información" |

#### 🎨 **Estilos de Botones**
El código incluye múltiples estilos de botones (comentados para fácil experimentación):

```python
# Diferentes estilos disponibles:
barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # Actual
# barra.setToolButtonStyle(Qt.ToolButtonIconOnly)      # Solo icono
# barra.setToolButtonStyle(Qt.ToolButtonTextOnly)      # Solo texto
# barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) # Texto bajo icono
```

## 🔧 Personalización

### Agregar Nuevas Acciones
```python
# Ejemplo: Agregar nueva acción a la barra
boton_abrir = QAction(QIcon('Src/abrir.png'), 'Abrir', self)
barra.addAction(boton_abrir)
boton_abrir.setStatusTip('Abrir archivo existente')
boton_abrir.triggered.connect(self.clik_barraAbrir)
```

### Modificar Comportamiento de Acciones
```python
def clik_barraNuevo(self, s):
    # Personalizar la acción "Nuevo"
    print(f'Creando nuevo archivo... {s}')
    # Aquí puedes agregar lógica personalizada
```

## 📚 Aprendizajes y Buenas Prácticas

### 🏗 **Arquitectura Qt**
- **QMainWindow** como contenedor principal
- **QLabel** como widget central
- **QToolBar** para acciones rápidas
- **QStatusBar** para información de estado

### 🔄 **Manejo de Eventos**
- **Señales y Slots** para comunicación entre componentes
- **triggered.connect()** para vincular acciones a funciones
- **setStatusTip()** para información contextual

### 🎨 **Personalización Visual**
- **setIconSize()** para dimensionar iconos
- **setToolButtonStyle()** para estilos de botones
- **Iconos personalizados** para mejor experiencia visual

## 🐛 Solución de Problemas

### Error: No se encuentran los iconos
```python
# Solución: Verificar rutas o usar iconos del sistema
boton_nuevo = QAction(QIcon.fromTheme('document-new'), 'Nuevo', self)
```

### Error: Módulo PySide6 no encontrado
```bash
# Reinstalar PySide6
pip uninstall pyside6
pip install pyside6
```

## 🚀 Próximos Pasos y Mejoras Potenciales

- [x] **Agregar menús desplegables** tradicionales
- [ ] **Implementar diálogos de archivo** (QFileDialog)
- [x] **Agregar atajos de teclado** para acciones
- [ ] **Internacionalización** (soporte multiidioma)
- [ ] **Temas personalizables** (dark/light mode)
- [ ] **Sistema de plugins** para extensibilidad

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Astharmin**
- 🌐 [GitHub](https://github.com/Astharmin)
- 💼 Desarrollador Full Stack & DevOps

## 🙏 Agradecimientos

- **The Qt Company** por el excelente framework Qt
- **Python Software Foundation** por hacerlo todo posible
- **Comunidad PySide** por la documentación y soporte

---

<div align="center">

### ⭐ ¿Te gustó este proyecto?

**Dale una estrella al repositorio** si este código te fue útil para aprender PySide6.

**¡Happy Coding!** 🐍🎉

</div>
