# Use uma imagem de exemplo com Python 3.12 (não é uma versão oficial)
FROM python:3.12-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Atualize o pip
RUN python -m pip install --upgrade pip

# Copie os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Configure a variável de ambiente para o Django
ENV DJANGO_SETTINGS_MODULE=setup.settings

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para iniciar o servidor do Django
CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
