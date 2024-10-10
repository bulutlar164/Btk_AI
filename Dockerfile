# Base image olarak Python 3.9 kullanıyoruz
FROM python:3.9-slim

# Çalışma dizinini belirliyoruz
WORKDIR /app

# Gereksinim dosyasını kopyalıyoruz ve bağımlılıkları yüklüyoruz
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalıyoruz
COPY . .

# Uygulama çalıştırma komutunu belirliyoruz
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
