# Selecciona una imagen ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias e instala los paquetes necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente del proyecto
COPY . .

# Expon el puerto usado (ajustar si usas la API Flask, por ejemplo 5000)
EXPOSE 5000

# Comando de ejecución por defecto (puede ser main.py o app.py)
CMD ["python", "main.py"]
# Si usas la API Flask/FastAPI activa, puedes cambiar por:
# CMD ["python", "app.py"]
