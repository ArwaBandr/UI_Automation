FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget curl gnupg ca-certificates \
    fonts-liberation libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    libxkbcommon0 libxshmfence1 libxss1 libxtst6 \
    libglib2.0-0 libgtk-3-0 libasound2 libdrm2 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN python -m playwright install
RUN apt-get update && apt-get install -y libgbm1

COPY . .

CMD ["behave"]

