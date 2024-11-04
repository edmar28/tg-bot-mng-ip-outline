# Telegram Bot for Managing IPs and Outline Keys
This Python-based Telegram bot manages IP addresses and their associated outline keys using SQLite as the database backend. It provides commands to add, retrieve, list, and delete entries directly from a Telegram chat. This bot is designed for easy management and retrieval of outline keys by IP address.

## Features
- Add or Update IP and Key: Quickly add a new IP address with an associated outline key or update an existing IP's key.
- Retrieve Outline Key: Retrieve the outline key associated with a specific IP address.
- List All IPs and Keys: Get a list of all stored IP addresses and their outline keys.
- Delete IP: Remove an IP address and its associated key from the database

## Requirements
- Python 3.7+
- python-telegram-bot library
- sqlite3 (Python standard library)

Install the python-telegram-bot library:
```bash
pip install python-telegram-bot==20.0a0
```

## Bot Commands

### /add_ip <ip> <outline_key>
Adds a new IP and outline key or updates an existing entry.

- Usage: /get_key 192.168.1.1
- Response: Returns the outline key if it exists; otherwise, informs the user that no entry was found.

### /get_key <ip>
Retrieves the outline key associated with the specified IP.

- Usage: /get_key 192.168.1.1
- Response: Returns the outline key if it exists; otherwise, informs the user that no entry was found.

### /list_ips
Lists all stored IP addresses and their associated outline keys.

-Response: Provides a formatted list of all IPs and keys in the database.

### /delete_ip <ip>
Deletes an IP entry from the database.

- Usage: /delete_ip 192.168.1.1
- Response: Confirms the IP has been deleted if it exists.


## Code Structure

1. Database Initialization
The init_db() function initializes the SQLite database, creating the table if it doesn’t exist:
```bash
def init_db():
    conn = sqlite3.connect('outline_keys.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS outline_keys (
            ip TEXT PRIMARY KEY,
            outline_key TEXT
        )
    ''')
    conn.commit()
    conn.close()

```

2. Command Handlers
Each command has its own handler function to manage the relevant action:

- add_ip(): Inserts or updates an IP and key in the database.
- get_key(): Retrieves a key by IP.
- list_ips(): Lists all IPs and keys.
- delete_ip(): Deletes an IP from the database.


3. Main Function
The main() function initializes the database, sets up the bot, and starts polling:
```bash
def main():
    init_db()  # Initialize database table on startup
    app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
    
    app.add_handler(CommandHandler("add_ip", add_ip))
    app.add_handler(CommandHandler("get_key", get_key))
    app.add_handler(CommandHandler("list_ips", list_ips))
    app.add_handler(CommandHandler("delete_ip", delete_ip))
    
    app.run_polling()

```

## Running the Bot
1. Replace "YOUR_TELEGRAM_BOT_TOKEN" with your actual bot token from BotFather.
2. Run the script:
```bash
python3 outline-view-key.py
```

## Example Usage

- Adding a Key:
User types /add_ip 192.168.1.1 ABCD1234 in the Telegram chat. The bot responds with Added/Updated IP: 192.168.1.1.

- Retrieving a Key:
User types /get_key 192.168.1.1. The bot responds with Outline Key for IP 192.168.1.1: ABCD1234.

- Listing All Keys:
User types /list_ips. The bot displays all stored IPs and keys.

- Deleting an IP:
User types /delete_ip 192.168.1.1. The bot responds with Deleted IP: 192.168.1.1.
