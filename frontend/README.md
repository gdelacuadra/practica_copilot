# Frontend (React)

Aplicación web en React con:

- **/login**: formulario de autenticación contra el backend.
- **/welcome**: página protegida solo para usuarios con sesión activa.

## Flujo de autenticación

1. El login envía `username` y `password` a `POST /login`.
2. Si el backend responde correctamente, el token se guarda en `sessionStorage`.
3. La ruta `/welcome` verifica token antes de renderizar.
4. Si no hay token, redirige a `/login`.

## Ejecución

```bash
npm install
npm run dev
```

Por defecto el frontend usa `http://localhost:8000` como backend.
Puedes cambiarlo con:

```bash
VITE_API_BASE_URL=http://tu-backend:puerto npm run dev
```

## Validación local

```bash
npm run lint
npm run build
```
