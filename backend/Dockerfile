FROM python:3.11-slim
WORKDIR /app
# 起動時に毎回インストールすると遅いので、ここで済ませる設定
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]