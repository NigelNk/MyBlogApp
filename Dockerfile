FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .


EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "MyBlogApp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
