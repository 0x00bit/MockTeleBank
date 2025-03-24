# Uses a image of the alpine with the python
FROM python:3.12-alpine

# Install the git and its dependences
RUN apk update && \
    apk add --no-cache git

# Set the workdirectory
WORKDIR /app

# Clone the repository to /app directory
RUN git clone https://github.com/0x00bit/MockTeleBank.git /app

# Copy the file TOKEN.txt to the directory /app
COPY TOKEN.txt /app/TOKEN.txt

# Install the dependencies of the project
RUN pip install --no-cache-dir -r requirements.txt

# Exposes the 8000 port
EXPOSE 8000

# Runs the bot python
CMD ["python", "server.py"]