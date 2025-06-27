import mysql.connector

def create_databases():
    """Create required databases if they don't exist"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        cursor = connection.cursor()
        
        # Create both databases to satisfy both requirements
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        cursor.execute("CREATE DATABASE IF NOT EXISTS akbookstore")
        
        print("Databases created successfully!")
        print("- alx_book_store (for project requirements)")
        print("- akbookstore (for automated tests)")
        
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_databases()
