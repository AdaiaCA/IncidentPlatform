# Usa la imagen base de Debian
FROM debian:latest

# Establece la variable de entorno para evitar interacciones durante la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instala Python y pip
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación (opcional)
# COPY . /app/

# Comando por defecto
CMD ["python3"]
