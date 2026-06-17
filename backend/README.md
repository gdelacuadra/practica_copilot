# Backend JWT API

API REST construida con **FastAPI** y **Python 3.11** que implementa autenticación mediante **JSON Web Tokens (JWT)**.

## Características

- Endpoint de login (`POST /token`) que valida credenciales y devuelve un JWT con expiración de **300 segundos**.
- Endpoint de refresco (`POST /token/refresh`) que acepta un token válido y emite uno nuevo con una ventana de expiración renovada.
- Hashing de contraseñas con `passlib[bcrypt]` (bcrypt ≥3.2, <4.0).
- Gestión de dependencias con **Poetry**.
- Despliegue con **Docker** y **Docker Compose**.

## Credenciales por defecto

| Campo    | Valor     |
|----------|-----------|
| username | `admin`   |
| password | `admin123`|

## Requisitos previos

- [Docker](https://docs.docker.com/get-docker/) y [Docker Compose](https://docs.docker.com/compose/install/) instalados, **o bien**
- Python 3.11+ y [Poetry](https://python-poetry.org/docs/#installation).

## Ejecución con Docker Compose

```bash
cd backend
docker compose up --build
```

La API quedará disponible en `http://localhost:8000`.

## Ejecución en local (sin Docker)

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

## Endpoints

### `POST /token`

Obtiene un token JWT enviando las credenciales como form data.

**Body** (`application/x-www-form-urlencoded`):

| Campo      | Descripción        |
|------------|--------------------|
| `username` | Nombre de usuario  |
| `password` | Contraseña         |

**Ejemplo con `curl`:**

```bash
# Reemplaza <usuario> y <contrasena> con las credenciales correspondientes
curl -X POST http://localhost:8000/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=<usuario>&******"
```

**Respuesta:**

```json
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

---

### `POST /token/refresh`

Refresca un token JWT existente y válido, devolviendo uno nuevo con 300 segundos de expiración.

**Header:** `Authorization: ******

**Ejemplo con `curl`:**

```bash
curl -X POST http://localhost:8000/token/refresh \
  -H "Authorization: ******"
```

**Respuesta:**

```json
{
  "access_token": "<new_jwt_token>",
  "token_type": "bearer"
}
```

## Documentación interactiva

FastAPI genera documentación automática disponible en:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`
