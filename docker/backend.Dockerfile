FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt

COPY backend .

ENV FLASK_APP=app
ENV FLASK_ENV=production

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]