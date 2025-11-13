# 1. Imagen base
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo
WORKDIR /app

# 3. Copiar y restaurar dependencias primero (para caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el código de la aplicación
COPY main.py .

# 5. Exponer el puerto en el que corre la app
EXPOSE 8000

# 6. Comando de producción
#    Usamos Gunicorn para gestionar los 'workers' de Uvicorn.
#    -w 4 = 4 workers (ajusta según tu CPU)
#    -k uvicorn.workers.UvicornWorker = El tipo de worker
#    -b 0.0.0.0:8000 = Escucha en todas las IPs en el puerto 8000
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app"]
