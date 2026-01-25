FROM python:3.14.2-slim

WORKDIR /app

# Install Node.js for Tailwind and build dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    nodejs \
    npm \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .


# Collect static files
RUN python manage.py collectstatic --noinput

# Make start.sh executable
RUN chmod +x /app/start.sh

# Expose the port (Railway uses PORT env var, but EXPOSE is good practice)
EXPOSE 8000

# Run the startup script
CMD ["/app/start.sh"]

