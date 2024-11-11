import mariadb
import sys

DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'samplecrud_db'
}

# https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
def get_db_connection():
    try:
        conn = mariadb.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        print(f'Connected to {DB_CONFIG["database"]} successfully!')
        return conn
    except mariadb.Error as e:
        print(f'Error connected to {DB_CONFIG["database"]}: {e}')
        sys.exit(1)

# test database connection
if __name__ == '__main__':
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("show tables")
    tables = cursor.fetchall()
    print("Tables in the database: ", tables)

    cursor.close()
    conn.close()