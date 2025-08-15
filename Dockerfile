# Usa una imagen base ligera
FROM python:3.12-slim

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto de Flask (por ejemplo 5000)
EXPOSE 8000

# Comando de inicio (mejor usar Gunicorn para producción)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "htmlserver:app"]
