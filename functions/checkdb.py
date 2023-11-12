import sqlite3

# Path to the SQLite database file
sqlite_db_path = '../database/taylor_swift.db'
table_name = 'ts_albums'  # The name of the table to check for

# Connect to the SQLite database
conn = sqlite3.connect(sqlite_db_path)

# Create a cursor object
cur = conn.cursor()

# Query to check for the existence of the table
table_check_query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';"

# Execute the query
cur.execute(table_check_query)

# Fetch the results
result = cur.fetchone()

# Close the cursor and connection
cur.close()
conn.close()

# Check if the table exists
if result:
    print(f"The table '{table_name}' exists in the database.")
else:
    print(f"The table '{table_name}' does not exist in the database.")
