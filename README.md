# Sistema de Gestión de Laboratorios - Backend

## Características Principales

## Tecnologías Utilizadas

El proyecto se apoya en un stack tecnológico moderno centrado en la velocidad de desarrollo, la seguridad y la validación de datos.

### Núcleo del Sistema
* **Python (v3.10+)**: Lenguaje de programación base del ecosistema.
* **FastAPI (v0.135.1)**: Framework web de alto rendimiento para la construcción de la API, basado en estándares OpenAPI.
* **SQLAlchemy (v2.0.48)**: Toolkit SQL y mapeador objeto-relacional (ORM) para la gestión de la persistencia de datos.
* **Uvicorn (v0.41.0)**: Servidor ASGI de alta velocidad utilizado para la ejecución y despliegue de la aplicación.

### Validación y Datos
* **Pydantic (v2.12.5)**: Motor de validación de datos y gestión de configuraciones mediante modelos de datos rigurosos.
* **PostgreSQL / Psycopg2 (v2.9.11)**: Sistema de gestión de bases de datos relacional y adaptador binario para la comunicación con Python.

### Seguridad y Autenticación
* **Python-Jose (v3.5.0)**: Implementación de JOSE (JSON Object Signing and Encryption) para la generación y validación de tokens JWT.
* **Passlib (v1.7.4)** y **Bcrypt (v4.0.1)**: Librerías especializadas en el hashing seguro de contraseñas y gestión de esquemas de cifrado.
* **Cryptography (v47.0.0)**: Soporte de primitivas criptográficas para asegurar la integridad de las comunicaciones y datos.

### Utilidades y Entorno
* **Python-Dotenv (v1.2.2)**: Gestión de variables de entorno para la configuración segura de credenciales mediante archivos `.env`.
* **Python-Multipart (v0.0.22)**: Requerido para el procesamiento de datos de formularios y carga de archivos en peticiones HTTP.
* **Httpx (v0.28.1)**: Cliente HTTP de última generación para realizar peticiones asíncronas entre servicios.

## Integrantes
* **FELIPE ZAPATA ARANGO**
* **SAMUEL OQUENDO QUINTERO**
## Aplicaciones y Servicios Web 
## 02/05/2026

## Pasos para configurar el entorno virtual
* Descargar e instalar una versión Python 3.+
* En otro caso, instalar por medio del archivo requeriments.txt en la raíz del proyecto por medio del comando pip install -r requirements.txt
* Ejecutar el comando python /m venv venv para crear el entorno virtual
* Ejecutar el comando venv\Scripts\activate
* Teniendo las dependencias instaladas, ejecutar uvicorn app.main:app --reload y abrir el navegador de preferencia en http://127.0.0.1:8000/docs

### Documentación de Endpoints: