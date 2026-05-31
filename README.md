# Sistema de Gestión de Farmacia

Sistema de gestión de farmacia desarrollado con Django 6.0.5 siguiendo las mejores prácticas de arquitectura modular.

## Estructura del Proyecto

```
Farmacia_CANR/
├── venv/                          # Entorno virtual
├── farmacia_project/              # Configuración principal del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Configuración global
│   ├── urls.py                   # URLs principales
│   └── wsgi.py
├── core/                         # App: Funcionalidades base
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Formularios base
│   ├── migrations/
│   ├── models.py                 # Modelos base (usuarios, configuración)
│   ├── tests.py
│   ├── urls.py                   # URLs del core
│   └── views.py                  # Vistas base
├── inventario/                   # App: Gestión de inventario
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Formularios de inventario
│   ├── migrations/
│   ├── models.py                 # Modelos (productos, categorías, proveedores)
│   ├── tests.py
│   ├── urls.py                   # URLs de inventario
│   └── views.py                  # Vistas de inventario
├── ventas/                       # App: Gestión de ventas
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Formularios de ventas
│   ├── migrations/
│   ├── models.py                 # Modelos (ventas, clientes, facturas)
│   ├── tests.py
│   ├── urls.py                   # URLs de ventas
│   └── views.py                  # Vistas de ventas
├── db.sqlite3                    # Base de datos (SQLite)
├── manage.py                     # Script de gestión Django
└── requirements.txt              # Dependencias del proyecto
```

## Por qué esta estructura es MODULAR y ESCALABLE

### 1. **Separación de Responsabilidades (Principio SRP)**
- **core**: Contiene funcionalidades compartidas como autenticación, configuración del sistema, modelos base de usuarios, y utilidades comunes.
- **inventario**: Maneja exclusivamente la gestión de productos, categorías, proveedores, stock y movimientos de inventario.
- **ventas**: Se encarga del proceso de ventas, facturación, clientes y reportes de ventas.

Cada app tiene un propósito único y bien definido, lo que facilita el mantenimiento y evita el acoplamiento excesivo.

### 2. **Independencia de Apps**
- Cada app puede ser desarrollada, probada y mantenida de forma independiente.
- Las apps pueden ser reutilizadas en otros proyectos (por ejemplo, la app `inventario` podría usarse en otro sistema de gestión).
- Los cambios en una app no afectan necesariamente a las demás, siempre que se mantengan las interfaces definidas.

### 3. **Escalabilidad Horizontal**
- **Fácil agregar nuevas funcionalidades**: Si necesitas agregar gestión de compras, solo creas una app `compras` sin modificar las existentes.
- **Escalabilidad del equipo**: Diferentes desarrolladores pueden trabajar en diferentes apps simultáneamente sin conflictos.
- **Escalabilidad de código**: Cada app puede crecer en complejidad sin afectar la estructura general del proyecto.

### 4. **Mantenibilidad**
- **Código organizado**: La lógica de negocio está separada por dominios, facilitando la localización de funcionalidades.
- **Testing más sencillo**: Cada app puede tener sus propios tests independientes.
- **Migraciones controladas**: Las migraciones de base de datos se manejan por app, permitiendo versionado granular.

### 5. **Flexibilidad de Configuración**
- **Settings centralizados**: `settings.py` contiene la configuración global, pero cada app puede tener su propia configuración específica.
- **URLs modulares**: Cada app tiene su propio `urls.py`, permitiendo enrutamiento limpio y organizado.
- **Templates organizados**: Los templates pueden organizarse por app en la estructura `templates/app_name/`.

### 6. **Patrón MTV (Model-Template-View) por App**
Cada app sigue el patrón MTV de Django:
- **Models**: Definición de datos y estructura de base de datos.
- **Templates**: Presentación y UI específica de cada módulo.
- **Views**: Lógica de negocio y controladores.

### 7. **Preparado para Crecimiento**
Esta estructura permite:
- Integración con APIs REST (Django REST Framework)
- Implementación de microservicios en el futuro
- Agregar capas de servicios (service layer)
- Implementar patrones de diseño avanzados (Repository, Factory, etc.)

## Instalación y Configuración

### 1. Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario
```bash
python manage.py createsuperuser
```

### 5. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

## Tecnologías Utilizadas

- **Django 6.0.5**: Framework web principal
- **SQLite**: Base de datos (puede cambiarse a PostgreSQL/MySQL en producción)
- **Python 3.x**: Lenguaje de programación

## Próximos Pasos Recomendados

1. **Definir modelos** en cada app según los requisitos del negocio
2. **Configurar el admin de Django** para gestión de datos
3. **Implementar autenticación personalizada** en la app `core`
4. **Crear templates base** y estructura de UI
5. **Implementar APIs REST** para integración con frontend
6. **Configurar tests** para cada app
7. **Documentar las APIs** y funcionalidades

## Buenas Prácticas Aplicadas

- ✅ Separación de concerns por apps
- ✅ Estructura de carpetas organizada
- ✅ Uso de virtual environment
- ✅ Requirements.txt para reproducibilidad
- ✅ URLs modularizadas por app
- ✅ Formularios separados por app
- ✅ Preparado para testing independiente
