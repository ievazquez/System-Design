import os
import time
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

# 1. Inicializar el Limiter
#    - 'get_remote_address' usa la IP del cliente como clave.
#    - 'storage_uri' le dice que use Redis.

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_URL  = f"redis://{REDIS_HOST}:6379"

print(f"**********************************************")
print(f"DEBUG: Conectando a Redis en: {REDIS_URL}")
print(f"**********************************************")

limiter = Limiter(key_func=get_remote_address, 
                  storage_uri=REDIS_URL)
                  #storage_uri="redis://localhost:6379")

# 2. Inicializar la aplicación FastAPI
app = FastAPI()

# 3. Registrar el limiter en el "estado" de la app
#    (Así, FastAPI sabe que existe)
app.state.limiter = limiter

# 4. Registrar el manejador de excepciones
#    (Esto le dice a FastAPI qué hacer cuando se lanza un error 429)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# --- Rutas de la API ---

@app.get("/publico")
async def ruta_publica():
    """Una ruta sin límite, para comparar."""
    return {"mensaje": "Hola! Soy una ruta pública. Llámame todo lo que quieras."}


@app.get("/protegido")
@limiter.limit("5/minute")  # ¡Aquí está la magia!
async def ruta_protegida(request: Request):
    """
    Ruta protegida por el Rate Limiter.
    Importante: La ruta DEBE recibir 'request: Request' como argumento.
    
    Implementa un "Token Bucket" con:
    - Capacidad (Burst): 5 tokens
    - Relleno (Rate): 5 tokens por minuto
    """
    return {
        "mensaje": "Hola! Soy una ruta protegida. Tienes 5 peticiones por minuto.",
        "timestamp": time.time()
    }

# --- Ejecutar la app (Opcional, para desarrollo) ---
if __name__ == "__main__":
    import uvicorn
    # Ejecútalo con: uvicorn main:app --reload
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
