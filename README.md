🚀 SalesFlow - CRM con Django + DRF
SalesFlow es una plataforma CRM moderna y robusta construida con Django y Django REST Framework, diseñada para ayudar a equipos comerciales a gestionar clientes, tareas y ventas de forma eficiente.
Incluye autenticación con JWT, documentación interactiva, roles de usuario, API REST y soporte para despliegue en la nube.


🧰 Tecnologías utilizadas
⚙️ Django – Framework backend robusto y escalable.

🧩 Django REST Framework (DRF) – Creación de APIs RESTful.

🛢 PostgreSQL – Base de datos relacional.

🔐 JWT (SimpleJWT) – Autenticación segura.

📘 Swagger / ReDoc – Documentación interactiva de la API.

🐳 Docker + Docker Compose – Contenedores para desarrollo y producción.

🛠 GitHub Actions – CI/CD automatizado.

🧪 Instalación local
bash
Copy
Edit
git clone https://github.com/samuel-trujillo-234/SalesFlow.git
cd SalesFlow
python -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Configura tus variables
python manage.py migrate
python manage.py runserver
🔑 Autenticación
Solicita token JWT:

bash
Copy
Edit
curl -X POST http://127.0.0.1:8000/api/token/ \
-d "username=<tu_usuario>&password=<tu_contraseña>"
Usa el token:

bash
Copy
Edit
curl -H "Authorization: Bearer <token>" http://127.0.0.1:8000/api/clientes/
🔁 Funcionalidades principales
✅ Autenticación de usuarios (JWT)
✅ Registro, login y logout
✅ Gestión de clientes (CRUD)
✅ Gestión de tareas comerciales
✅ Gestión de ventas
✅ Roles y permisos
✅ API protegida
✅ Documentación Swagger/ReDoc
✅ Tests automatizados con pytest

📚 Endpoints principales
Recurso	Endpoint
Clientes	/api/clientes/
Tareas	/api/tareas/
Ventas	/api/ventas/

Documentación disponible en:

/swagger/

/redoc/

✅ Tests
Ejecuta los tests con:

bash
Copy
Edit
pytest
☁️ Despliegue (opcional)
Render
Crea un nuevo servicio.

Conecta el repositorio.

Configura .env en el panel.

Render detecta automáticamente Dockerfile.

Vercel (para frontend si aplica)
bash
Copy
Edit
npm install -g vercel
vercel
Railway
Conecta tu GitHub.

Crea nuevo proyecto.

Configura variables de entorno.

Railway detectará el Dockerfile y desplegará automáticamente.

✨ Capturas o Demo (opcional)
Agrega aquí imágenes o un GIF corto del funcionamiento.

📫 Contacto
¿Te interesa colaborar o contratarme?

Samuel Trujillo Montero
📧 samaletrumon@gmail.com
💼 (https://www.linkedin.com/in/samuel-trujillo-dev/)

📝 Licencia
Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.
