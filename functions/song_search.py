import pandas as pd
from sqlalchemy import create_engine

# Relative path to the SQLite database file from the location of song_search.py
sqlite_db_path = '../database/taylor_swift.db'

# Update the connection string to use SQLAlchemy's format
connection_string = 'sqlite:///../database/taylor_swift.db'

def get_suggestions_with_pandas(search_query):
    engine = create_engine(connection_string)

    # Use pandas to execute the SQL query and fetch results
    query = "SELECT * FROM ts_tracks_and_images WHERE name LIKE ? LIMIT 5"
    results = pd.read_sql(query, engine, params=(f"%{search_query}%",))

    # Convert the DataFrame to JSON and return
    return results.to_json(orient='records')

print(get_suggestions_with_pandas(input("Please input a song: ")))