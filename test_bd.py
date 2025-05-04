from config import Config
import os

print(f"Current working directory: {os.getcwd()}")
print(f"Database path: {Config.DATABASE_URI}")
print(f"Directory exists: {os.path.exists(os.path.dirname(Config.DATABASE_URI))}")
print(f"Can write to directory: {os.access(os.path.dirname(Config.DATABASE_URI), os.W_OK)}")

try:
    import sqlite3
    conn = sqlite3.connect(Config.DATABASE_URI)
    conn.close()
    print("Successfully connected to database!")
except Exception as e:
    print(f"Error connecting to database: {e}")