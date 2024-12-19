FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]