# SalesFlow

SalesFlow es una plataforma CRM desarrollada con Django que permite a los equipos comerciales gestionar clientes, tareas y ventas. Incluye autenticación de usuarios, API REST, sistema de roles y funcionalidades pensadas para la productividad empresarial.

## Tecnologías utilizadas

- **Django**: Framework principal para el desarrollo web.
- **Django REST Framework (DRF)**: Para la creación de APIs RESTful.
- **PostgreSQL**: Base de datos relacional.
- **JWT (SimpleJWT)**: Para la autenticación segura.
- **Swagger y Redoc**: Documentación interactiva de la API.
- **Docker y Docker Compose**: Para la contenedorización y despliegue.
- **GitHub Actions**: Para CI/CD.

## Instalación local

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd SalesFlow
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:
   Copia el archivo `.env.example` a `.env` y ajusta los valores según tu entorno.

5. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Funcionalidades principales

- **Gestión de usuarios**: Registro, inicio de sesión y cierre de sesión con un modelo de usuario personalizado.
- **Gestión de clientes**: CRUD completo para clientes.
- **Gestión de tareas**: CRUD completo para tareas asignadas a clientes.
- **Gestión de ventas**: CRUD completo para ventas realizadas a clientes.
- **API protegida con JWT**: Todas las rutas están protegidas y requieren autenticación.
- **Documentación interactiva**: Disponible en `/swagger/` y `/redoc/`.

## Uso de la API

### Autenticación

1. Obtén un token JWT:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/token/ -d "username=<tu_usuario>&password=<tu_contraseña>"
   ```

   Respuesta:
   ```json
   {
       "access": "<token_de_acceso>",
       "refresh": "<token_de_actualización>"
   }
   ```

2. Usa el token de acceso para autenticarte:
   ```bash
   curl -H "Authorization: Bearer <token_de_acceso>" http://127.0.0.1:8000/api/clientes/
   ```

### Endpoints principales

- **Clientes**: `/api/clientes/`
- **Tareas**: `/api/tareas/`
- **Ventas**: `/api/ventas/`

## Correr los tests

Ejecuta los tests con pytest:
```bash
pytest
```

## Despliegue

### Render
1. Crea un nuevo servicio en Render y conecta el repositorio.
2. Configura las variables de entorno desde el archivo `.env`.
3. Render detectará automáticamente el archivo `Dockerfile` y desplegará la aplicación.

### Vercel
1. Instala el CLI de Vercel:
   ```bash
   npm install -g vercel
   ```
2. Ejecuta el comando de despliegue:
   ```bash
   vercel
   ```
3. Configura las variables de entorno en el panel de Vercel.

### Railway
1. Crea un nuevo proyecto en Railway y conecta el repositorio.
2. Configura las variables de entorno desde el archivo `.env`.
3. Railway detectará automáticamente el archivo `Dockerfile` y desplegará la aplicación.
