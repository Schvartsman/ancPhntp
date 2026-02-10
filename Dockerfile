FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
COPY data/ ./data/
COPY input_output/ ./intput_output
ENTRYPOINT ["python", "src/calling.py"]
