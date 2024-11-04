# Telegram Bot for Managing IPs and Outline Keys
This Python-based Telegram bot manages IP addresses and their associated outline keys using SQLite as the database backend. It provides commands to add, retrieve, list, and delete entries directly from a Telegram chat. This bot is designed for easy management and retrieval of outline keys by IP address.

###Features
- Add or Update IP and Key: Quickly add a new IP address with an associated outline key or update an existing IP's key.
- Retrieve Outline Key: Retrieve the outline key associated with a specific IP address.
- List All IPs and Keys: Get a list of all stored IP addresses and their outline keys.
- Delete IP: Remove an IP address and its associated key from the database

###Requirements
- Python 3.7+
- python-telegram-bot library
- sqlite3 (Python standard library)

Install the python-telegram-bot library:
`pip install python-telegram-bot==20.0a0`
