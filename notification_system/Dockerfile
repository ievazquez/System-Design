FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todos nuestros scripts
COPY main.py .
COPY notification_worker.py .
COPY analytics_worker.py .
COPY event_bus.py . 

EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "main:app"]
