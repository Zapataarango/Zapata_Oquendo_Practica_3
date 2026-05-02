# Sistema de Gestión de Laboratorios - Backend

## Características Principales

* Gestión de laboratorios
* Gestión de servicios técnicos
* Gestión de tickets de soporte
* Control de acceso basado en roles (RBAC)
* Autenticación mediante JWT

---

## Tecnologías Utilizadas

El proyecto se apoya en un stack moderno enfocado en rendimiento, seguridad y validación de datos.

### Núcleo del Sistema

* **Python (v3.10+)**
* **FastAPI (v0.135.1)**: Framework de alto rendimiento basado en OpenAPI
* **SQLAlchemy (v2.0.48)**: ORM para persistencia de datos
* **Uvicorn (v0.41.0)**: Servidor ASGI

### Validación y Datos

* **Pydantic (v2.12.5)**: Validación de datos
* **PostgreSQL / Psycopg2 (v2.9.11)**: Base de datos relacional

### Seguridad y Autenticación

* **Python-Jose (v3.5.0)**: Manejo de JWT
* **Passlib (v1.7.4)** + **Bcrypt (v4.0.1)**: Hashing de contraseñas
* **Cryptography (v47.0.0)**: Funciones criptográficas

### Utilidades

* **Python-Dotenv (v1.2.2)**: Variables de entorno
* **Python-Multipart (v0.0.22)**: Manejo de formularios
* **Httpx (v0.28.1)**: Cliente HTTP async

---

## Integrantes

* **Felipe Zapata Arango**
* **Samuel Oquendo Quintero**

---

## Fecha

02/05/2026

---

## Configuración del Entorno

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
uvicorn app.main:app --reload
```

Accede a la documentación en:
http://127.0.0.1:8000/docs

---

# Documentación de API

---

# Módulo de Laboratorios

Gestiona los espacios físicos donde se prestan servicios técnicos.

## Permisos

| Acción    | Endpoint             | Método | Scope               | Acceso |
| --------- | -------------------- | ------ | ------------------- | ------ |
| Crear     | `/laboratorios/`     | POST   | laboratorios:create | Admin  |
| Listar    | `/laboratorios/`     | GET    | laboratorios:read   | Todos  |
| Consultar | `/laboratorios/{id}` | GET    | laboratorios:read   | Todos  |
| Eliminar  | `/laboratorios/{id}` | DELETE | laboratorios:delete | Admin  |

---

## Endpoints

### 1. Crear Laboratorio

```json
POST /laboratorios/
Authorization: Bearer <token>

{
  "nombre": "Laboratorio de IA",
  "ubicacion": "Bloque M, Oficina 301",
  "descripcion": "Investigación en IA"
}
```

### 2. Listar Laboratorios

```json
GET /laboratorios/
```

### 3. Obtener por ID

```json
GET /laboratorios/{id}
```

### 4. Eliminar

```json
DELETE /laboratorios/{id}
```

---

## Errores Comunes

| Código | Descripción     |
| ------ | --------------- |
| 401    | Token inválido  |
| 403    | Sin permisos    |
| 422    | Datos inválidos |

---

# Módulo de Servicios

Gestiona el catálogo de servicios técnicos.

## Permisos

| Acción    | Endpoint          | Método | Scope            | Acceso |
| --------- | ----------------- | ------ | ---------------- | ------ |
| Crear     | `/servicios/`     | POST   | servicios:create | Admin  |
| Listar    | `/servicios/`     | GET    | servicios:read   | Todos  |
| Consultar | `/servicios/{id}` | GET    | servicios:read   | Todos  |
| Eliminar  | `/servicios/{id}` | DELETE | servicios:delete | Admin  |

---

## Endpoints

### 1. Crear Servicio

```json
POST /servicios/

{
  "nombre": "Mantenimiento Preventivo",
  "descripcion": "Optimización de hardware",
  "id_laboratorio": 1
}
```

### 2. Listar Servicios

```json
GET /servicios/
```

### 3. Obtener por ID

```json
GET /servicios/{id}
```

### 4. Eliminar

```json
DELETE /servicios/{id}
```

---

## Consideraciones

Al eliminar un servicio, asegúrate de que no tenga tickets asociados para evitar errores de integridad referencial.

---

# Módulo de Tickets

Gestiona el ciclo de vida de los requerimientos.

## Permisos

| Acción     | Endpoint               | Método | Scope          | Roles              |
| ---------- | ---------------------- | ------ | -------------- | ------------------ |
| Crear      | `/tickets/`            | POST   | tickets:create | Solicitante, Admin |
| Listar     | `/tickets/`            | GET    | tickets:read   | Todos              |
| Consultar  | `/tickets/{id}`        | GET    | tickets:read   | Todos              |
| Actualizar | `/tickets/{id}/estado` | PATCH  | tickets:update | Técnicos/Admin     |
| Eliminar   | `/tickets/{id}`        | DELETE | tickets:delete | Admin              |

---

## Endpoints

### 1. Crear Ticket

```json
POST /tickets/

{
  "titulo": "Falla de red",
  "descripcion": "No hay IP",
  "prioridad": "Alta",
  "id_laboratorio": 1,
  "id_servicio": 2,
  "id_solicitante": 5
}
```

Estado inicial: `solicitado`

---

### 2. Listar Tickets

```json
GET /tickets/
```

---

### 3. Actualizar Estado

```json
PATCH /tickets/{id}/estado

{
  "estado": "en_proceso",
  "observacion_tecnico": "Revisión de cableado",
  "id_asignado": 3
}
```

Estados permitidos:

* solicitado
* recibido
* en_proceso
* en_revision
* terminado

---

### 4. Eliminar

```json
DELETE /tickets/{id}
```

---

## Flujo de Estados

1. Solicitado
2. Recibido
3. Asignado
4. En revisión
5. Terminado

---

## Errores

* 403: Sin permisos
* 422: Estado inválido

---

# Evidencias

## Admin

### Listar Tickets

![Listar tickets](image.png)

### Crear Usuario

![Crear usuario](image-4.png)

### Listar Usuarios

![Listar usuarios](image-5.png)

### Asignar Ticket

![Asignar ticket](image-1.png)

### Crear Ticket

![Crear ticket](image-2.png)

### Listar Servicios

![Listar servicios](image-3.png)

---

# Base de Datos

* Motor: PostgreSQL
* ORM: SQLAlchemy
* Schema: `jwt_grupo_2`
