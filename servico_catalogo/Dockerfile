# 1. Escolha a base: Vamos usar um Python leve (versão 3.9 slim)
FROM python:3.9-slim

# 2. Defina o local de trabalho: Vamos criar uma pasta /app dentro da caixa
WORKDIR /app

# 3. Copie os ingredientes: Pega tudo da pasta atual e joga dentro da caixa
COPY . .

# 4. Prepare o ambiente: Instala o Flask e o Requests (as ferramentas necessárias)
RUN pip install flask requests


# Definir a variável de ambiente para ativar o modo de desenvolvimento do Flask
ENV FLASK_APP=catalogo_service.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5002
ENV FLASK_ENV=development


# Expor a porta padrão do Flask
EXPOSE 5002

# Rodar o aplicativo Flask
CMD ["flask", "run", "--host=0.0.0.0"]
