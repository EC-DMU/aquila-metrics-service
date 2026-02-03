# Stage 1: Requirements install

# used slim version to reduce image size
FROM python:3.11-slim AS requirements
WORKDIR /api

COPY requirements.txt .
# no cache used to reduces image size
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt

# Stage 2: Running Application

# used slim version to reduce image size
FROM python:3.11-slim
WORKDIR /api
COPY --from=requirements /usr/local /usr/local
ENV PATH=/usr/local/bin:$PATH

# copy flask code
COPY . .
# Set flask port
ENV PORT=5050
EXPOSE 5050

CMD ["python", "api/api.py"]