#!/usr/bin/python3
"""
Python script to create akbookstore database in MySQL
"""

import mysql.connector

def create_database():
    """Create MySQL database if it doesn't exist"""
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS akbookstore")
        print("Database 'akbookstore' created successfully!")
        
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
