
# Backend API con FastAPI para la Gestión de Productos, Marcas y Categorías

Este proyecto es una API RESTful desarrollada con **FastAPI** que permite gestionar productos, marcas y categorías. Implementa operaciones CRUD, autenticación con OAuth2 y está configurada para utilizar una base de datos SQLite. La API está diseñada para ser consumida por una aplicación móvil y cuenta con pruebas unitarias para cada endpoint.

## Estructura del Proyecto

```plaintext
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada de la API
│   ├── models.py              # Modelos ORM de SQLAlchemy (Product, Brand, Category)
│   ├── schemas.py             # Esquemas Pydantic para validación (ProductCreate, BrandCreate, etc.)
│   ├── crud.py                # Operaciones CRUD
│   ├── dependencies.py        # Dependencias para autenticación OAuth2
│   ├── database.py            # Configuración de la base de datos SQLite
│   └── routers/
│       ├── products.py        # Rutas para operaciones de productos
│       ├── brands.py          # Rutas para operaciones de marcas
│       └── categories.py      # Rutas para operaciones de categorías
├── tests/
│   ├── test_products.py       # Pruebas unitarias para productos
│   ├── test_brands.py         # Pruebas unitarias para marcas
│   └── test_categories.py     # Pruebas unitarias para categorías
└── requirements.txt           # Dependencias de Python
```

## Instalación y Configuración

### Requisitos Previos

- Python 3.7 o superior.
- [pip](https://pip.pypa.io/en/stable/installation/) para la instalación de dependencias.

### Instalación

1. Clona el repositorio o descarga los archivos del proyecto:

   ```bash
   git clone https://github.com/Skpow1234/BackendDeepSeaDevelopment
   cd backend
   ```

2. Crea un entorno virtual para manejar las dependencias de Python:

   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:

   - En Windows:

     ```bash
     venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Configuración de la Base de Datos

El proyecto está configurado para utilizar SQLite como base de datos. La base de datos se crea automáticamente cuando se ejecuta el servidor por primera vez. No se requieren configuraciones adicionales para la base de datos.

### Ejecución del Servidor

1. Asegúrate de estar en el directorio `backend`.
2. Ejecuta el servidor con el siguiente comando:

   ```bash
   uvicorn app.main:app --reload
   ```

3. La API estará disponible en `http://127.0.0.1:8000`.

### Documentación de la API

FastAPI genera documentación automáticamente. Puedes acceder a la documentación interactiva de la API en:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Pruebas Unitarias

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
pytest
```

Esto ejecutará todas las pruebas ubicadas en la carpeta `tests/` y mostrará un resumen de los resultados.

### Estructura de Archivos y Descripción

- **app/main.py**: El archivo principal que inicia la aplicación y define las rutas principales.
- **app/models.py**: Contiene los modelos de la base de datos utilizando SQLAlchemy.
- **app/schemas.py**: Define los esquemas de datos (usando Pydantic) para validación de entrada y salida de datos.
- **app/crud.py**: Funciones de CRUD para manejar la lógica de negocio de cada modelo.
- **app/database.py**: Configuración de la base de datos SQLite.
- **app/dependencies.py**: Define las dependencias, como la autenticación OAuth2.
- **app/routers/**: Contiene las rutas de productos, marcas y categorías.
- **tests/**: Pruebas unitarias para cada módulo.

## Funcionalidades Implementadas

1. **CRUD de Productos**:
   - Crear, listar, buscar, actualizar y eliminar productos.
   - URL: `/products/`

2. **CRUD de Marcas**:
   - Crear, listar, buscar, actualizar y eliminar marcas.
   - URL: `/brands/`

3. **CRUD de Categorías**:
   - Crear, listar, buscar, actualizar y eliminar categorías.
   - URL: `/categories/`

4. **Autenticación con OAuth2**:
   - Cada endpoint está protegido mediante autenticación básica utilizando OAuth2 para asegurar que solo usuarios registrados puedan acceder a la información.

## Ejemplo de Endpoints

### Crear un Producto

- **URL**: `http://127.0.0.1:8000/products/`
- **Método**: POST
- **Body**:

  ```json
  {
    "name": "Example Product",
    "description": "A sample description",
    "brand_id": 1,
    "category_id": 1,
    "price": 100.0,
    "rating": 4.5
  }
  ```

### Listar Productos

- **URL**: `http://127.0.0.1:8000/products/`
- **Método**: GET

## Autor

```bash
Juan Felipe Hurtado
```
