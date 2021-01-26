FROM python:3.6.12

ARG bucket_name
ENV BUCKET_NAME=$bucket_name
ENV GOOGLE_APPLICATION_CREDENTIALS=gcp_key/key.json

ENV DOCKER=true

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app", "--timeout", "60"]