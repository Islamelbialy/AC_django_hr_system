FROM python:3.11-slim
WORKDIR /app
COPY ./requirements.txt /app
# Install core dependencies.
RUN apt-get update && apt-get install -y libpq-dev build-essential
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
# Define environment variable 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1
CMD ["python", "manage.py", "runserver"]
