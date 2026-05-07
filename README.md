# Repuestos API

API REST construida con FastAPI para gestionar repuestos, categorías y usuarios.

Este proyecto está estructurado con una separación clara de responsabilidades: modelos, esquemas, rutas, servicios y acceso a datos.

## 📁 Estructura principal

- `main.py` - punto de entrada de la aplicación FastAPI.
- `database.py` - configuración de SQLAlchemy y la conexión a la base de datos PostgreSQL.
- `models.py` - definiciones de las tablas de la base de datos.
- `schemas.py` - definiciones de esquemas Pydantic para validación y serialización.
- `routes/` - rutas HTTP organizadas por recursos.
- `services/` - lógica de negocio y validaciones específicas.
- `crud/` - operaciones CRUD sobre la base de datos.
- `auth.py` - gestión de hashing de contraseñas y tokens JWT.
- `requirements.txt` - dependencias del proyecto.

## 🧩 Modelos principales

- `UsuarioDB` - usuarios registrados con `username`, `email` y `hashed_password`.
- `RepuestoDB` - repuestos con `marca`, `modelo`, `precio`, `stock` y relación con `CategoriaDB`.
- `CategoriaDB` - categorías de repuestos y relación uno a muchos con repuestos.

## 🚀 Cómo ejecutar el proyecto

1. Activar el entorno virtual:

```bash
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar la app con Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

4. Abrir la documentación automática en:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

> Al iniciar, `main.py` crea automáticamente las tablas de la base de datos con `Base.metadata.create_all(bind=engine)`.

## 🔧 Configuración de la base de datos

Actualmente la conexión se define en `database.py` como:

```python
DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/repuestodb"
```

Si deseas usar tu propia base de datos, reemplaza esta cadena con tu URL de PostgreSQL.

## 🔐 Autenticación

El proyecto usa JWT para autenticación.

- `/usuarios/login` - recibe `username` y `password` via `OAuth2PasswordRequestForm`.
- Devuelve un `access_token` tipo `bearer`.
- `/usuarios/me` - obtiene el usuario actual validando el token.

## 🛠 Endpoints principales

### Usuarios

- `POST /usuarios/` - crear usuario
- `GET /usuarios/` - listar usuarios
- `GET /usuarios/{usuario_id}` - obtener usuario por id
- `PUT /usuarios/{usuario_id}` - actualizar usuario
- `DELETE /usuarios/{usuario_id}` - eliminar usuario
- `POST /usuarios/login` - iniciar sesión y generar token
- `GET /usuarios/me` - obtener datos del usuario autenticado

### Repuestos

- `POST /repuestos/` - crear repuesto
- `GET /repuestos/` - listar repuestos
- `GET /repuestos/{repuesto_id}` - obtener repuesto por id
- `PUT /repuestos/{repuesto_id}` - actualizar repuesto
- `DELETE /repuestos/{repuesto_id}` - eliminar repuesto

### Categorías

- `POST /categoria/` - crear categoría
- `GET /categoria/` - listar categorías
- `GET /categoria/{categoria_id}` - obtener categoría por id
- `GET /categoria/{categoria_id}/repuestos` - listar repuestos de una categoría

## ✅ Flujo del proyecto

- `routes/` define las rutas HTTP.
- `schemas.py` valida las solicitudes y respuestas.
- `services/` contiene la lógica de negocio y control de errores.
- `crud/` interactúa con la base de datos.
- `auth.py` gestiona contraseñas y JWT.

## 📝 Notas finales

Este README describe el proyecto completo y su ejecución. Está diseñado para que quede claro que el desarrollo fue realizado por mí, con una arquitectura organizada y una API funcional para gestionar repuestos, categorías y usuarios.
