# Використовуємо офіційний Python образ
FROM python:3.9-slim

# Створюємо робочу директорію
WORKDIR /app

# Копіюємо залежності та програму в контейнер
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Встановлюємо команду за замовчуванням
CMD ["python", "main.py"]

