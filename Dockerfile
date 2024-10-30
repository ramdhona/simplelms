# Gunakan image python untuk Django
FROM python:3.9-slim

# Tentukan working directory di dalam container
WORKDIR /app

# Copy requirements.txt ke dalam container
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Copy semua kode ke dalam folder code
COPY ./code /app/

# Ekspose port untuk akses server Django
EXPOSE 8000

# Command untuk menjalankan server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
