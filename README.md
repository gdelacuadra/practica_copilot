# practica_copilot

Aplicación de ejemplo con frontend en React para autenticación:

- `/frontend`: aplicación web con pantalla de login y pantalla de bienvenida.
- `DESIGN.md`: estándar visual aplicado en la interfaz.

## Funcionalidad implementada

1. **Login**
   - Formulario con usuario y contraseña.
   - Llama al backend en `POST /login` usando `application/x-www-form-urlencoded`.
   - Guarda el token de autenticación en `sessionStorage`.

2. **Bienvenida protegida**
   - La ruta `/welcome` solo se muestra si existe token en sesión.
   - Si no hay sesión activa, redirige automáticamente a `/login`.
   - Incluye botón de cierre de sesión.

## Ejecución del frontend

Desde la raíz del repositorio:

```bash
cd frontend
npm install
npm run dev
```

La app quedará disponible en `http://localhost:5173`.

## Configuración del backend

El frontend consume por defecto `http://localhost:8000/login`.
Si necesitas otro host, define:

```bash
VITE_API_BASE_URL=http://tu-backend:puerto
```

y luego ejecuta `npm run dev`.
