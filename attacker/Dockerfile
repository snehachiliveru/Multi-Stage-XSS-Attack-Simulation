FROM python:3.10-slim
WORKDIR /app
COPY attacker.py /app/
RUN pip install --no-cache-dir requests
CMD ["python", "attacker.py"]
