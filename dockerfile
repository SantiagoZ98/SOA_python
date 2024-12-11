# Usamos una imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos de la aplicación al contenedor
COPY . /app

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto que Flask usará
EXPOSE 5000

# Comando para ejecutar el servicio
CMD ["python", "greeting_service.py"]
