#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        
        # Create cursor object
        cur = conn.cursor()
        
        # Execute SQL query to fetch states sorted by id
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        
        # Fetch all rows
        rows = cur.fetchall()
        
        # Print results
        for row in rows:
            print(row)
        
        # Close cursor and connection
        cur.close()
        conn.close()
        
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    list_states(username, password, database)
