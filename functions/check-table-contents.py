import sqlite3

# Path to your SQLite database file
sqlite_db_path = '../database/taylor_swift.db'
table_name = 'ts_tracks_and_images'  # replace with your table name

# Connect to the SQLite database
conn = sqlite3.connect(sqlite_db_path)

# Create a cursor object
cur = conn.cursor()

# Execute a query to select all rows from the table
cur.execute(f"SELECT * FROM {table_name}")

# Fetch all rows from the result of the query
rows = cur.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()