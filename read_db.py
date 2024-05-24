import sqlite3

def read_data():
    conn = sqlite3.connect('potato_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM potato_plants")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    conn.close()

if __name__ == '__main__':
    read_data()