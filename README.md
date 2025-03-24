# Mock Bank Bot - Telegram

## Overview
This is a mock bank bot created for Telegram, designed to simulate basic banking operations. It uses MongoDB as the backend to store and manage user data. The bot allows users to perform operations such as checking balance, depositing, and withdrawing funds.

## Project Structure
The project is divided into four main modules:

### 1. **bot.py**
- Handles communication with Telegram.
- Receives messages from users and forwards them to `server.py`.
- Sends messages from `server.py` back to the user.
- Requires a file named `TOKEN.txt` in the root directory containing the Telegram bot token.

### 2. **server.py**
- The core of the system.
- Runs in a loop, continuously listening for new messages from `bot.py`.
- Interprets user commands and processes corresponding actions.

### 3. **client.py**
- Represents a client entity.
- Contains methods for performing operations such as deposit, withdrawal, and checking balance.

### 4. **database.py**
- Responsible for performing CRUD (Create, Read, Update, Delete) operations on the MongoDB database.
- Processes data from client operations and updates the database accordingly.
- While a function to delete users was implemented, it was intentionally left unused to avoid users deleting each other.

## Requirements
To run this project, ensure you have the following Python packages installed:

```bash
pip install -r requirements.txt
```

## How to Run
1. Clone the repository or download the source code.
2. Create a `TOKEN.txt` file in the root directory and paste your Telegram bot token inside.
3. Ensure your MongoDB database is running and properly configured.
4. If you have Docker installed, you can run a MongoDB instance using the following command:

```bash
docker run -d -p 27017:27017 --name mongodb mongo
```

5. Run the `server.py` file to start the bot:

```bash
python server.py
```

## With Docker
1. Clone the repository or download the source code.

2. Create a TOKEN.txt file in the root directory and paste your Telegram bot token inside.

3. Build the Docker image for the bot:
```bash
docker build -t mock-tele-bank .
```

4. Create a Docker network to connect the bot and MongoDB:
```bash
docker build -t mock-tele-bank .
```

5. Run a MongoDB container in the created network:
```bash
docker build -t mock-tele-bank .
```

6. Run the bot container in the same network:
```bash
docker run -d --name mock-bank-bot --network mock-bank-network -p 8000:8000 mock-tele-bank
```

7. The bot should now be running and connected to the MongoDB instance.

8. If the bot don't run, you can try to change the line 6 to:
```bash
self.client = MongoClient("mongodb://mongodb:27017")
```

## Features
- **Check Balance:** View the current balance and the last deposit or withdrawal details.
- **Deposit:** Add funds to the client's account.
- **Withdraw:** Remove funds from the client's account (if sufficient balance exists).

## Notes
- Deleting users is not enabled by design to maintain data integrity.
- Inline buttons could not be implemented due to the parameters required for the bot to function correctly. Instead, a menu button was added with the available commands and their usage.
- Make sure to keep your `TOKEN.txt` file secure and not share it publicly.
