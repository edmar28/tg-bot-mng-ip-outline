from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sqlite3
import asyncio

# Initialize the database
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

# Command to add or update an IP and outline key
async def add_ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        ip = context.args[0]
        outline_key = context.args[1]
        
        with sqlite3.connect('outline_keys.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR REPLACE INTO outline_keys (ip, outline_key) VALUES (?, ?)", (ip, outline_key))
            conn.commit()
        
        await update.message.reply_text(f"Added/Updated IP: {ip}")
    except IndexError:
        await update.message.reply_text("Usage: /add_ip <ip> <outline_key>")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Command to retrieve an outline key by IP
async def get_key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        ip = context.args[0]
        
        with sqlite3.connect('outline_keys.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT outline_key FROM outline_keys WHERE ip = ?", (ip,))
            result = cursor.fetchone()
        
        if result:
            await update.message.reply_text(f"Outline Key for IP {ip}: {result[0]}")
        else:
            await update.message.reply_text(f"No outline key found for IP: {ip}")
    except IndexError:
        await update.message.reply_text("Usage: /get_key <ip>")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Command to list all IPs and outline keys
async def list_ips(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        with sqlite3.connect('outline_keys.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT ip, outline_key FROM outline_keys")
            results = cursor.fetchall()
        
        if results:
            message = "Stored IPs and Outline Keys:\n\n"
            for ip, key in results:
                message += f"IP: {ip}\nKey: {key}\n\n"
            await update.message.reply_text(message)
        else:
            await update.message.reply_text("No IPs found.")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Command to delete an IP entry
async def delete_ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        ip = context.args[0]
        
        with sqlite3.connect('outline_keys.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM outline_keys WHERE ip = ?", (ip,))
            conn.commit()
        
        await update.message.reply_text(f"Deleted IP: {ip}")
    except IndexError:
        await update.message.reply_text("Usage: /delete_ip <ip>")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Main function to set up the bot
def main():
    init_db()  # Initialize database table on startup
    app = ApplicationBuilder().token("TOKEN HERE").build()
    
    app.add_handler(CommandHandler("add_ip", add_ip))
    app.add_handler(CommandHandler("get_key", get_key))
    app.add_handler(CommandHandler("list_ips", list_ips))
    app.add_handler(CommandHandler("delete_ip", delete_ip))
    
    # Start polling without asyncio.run()
    app.run_polling()

# Run the bot
if __name__ == "__main__":
    main()

