# Dockerfile
FROM python:3.11-slim

# Helpful env flags + Flask defaults
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    FLASK_APP=hello.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

# Work directory inside the container
WORKDIR /app

# Install Python deps first 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Expose the Flask port
EXPOSE 5000

# Start the dev server
CMD ["flask", "run"]
