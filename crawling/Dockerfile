# ✅ Python 3.9 환경 사용
FROM python:3.9-slim

# ✅ 작업 디렉터리 설정
WORKDIR /app

# ✅ 필수 패키지 및 Chrome + Chromedriver 설치
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# ✅ 환경 변수 설정 (Selenium이 Chrome을 찾을 수 있도록)
ENV PATH="/usr/lib/chromium:$PATH"
ENV CHROME_BIN="/usr/lib/chromium/chrome"
ENV CHROMEDRIVER_BIN="/usr/bin/chromedriver"

# ✅ 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ 소스 코드 복사
COPY . .
FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    wget curl unzip chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*  # 캐시 정리
ENV PATH="/usr/lib/chromium:$PATH"
ENV CHROME_BIN="/usr/lib/chromium/chrome"
ENV CHROMEDRIVER_BIN="/usr/bin/chromedriver"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & celery -A workers.scraping_tasks worker --loglevel=info"]


