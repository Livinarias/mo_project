# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /mo_project

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación al contenedor
COPY . .

# Expone el puerto en el que correrá tu aplicación
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python", "mo_project/manage.py", "runserver", "0.0.0.0:8000"]
