import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="postgres"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Define the SQL query to create the table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS high_scores (
        name varchar(50),
        score integer
    );
'''

# Execute the create table query
cur.execute(create_table_query)

# Commit the changes to the database
conn.commit()

cur.execute("SELECT * FROM high_scores")
rows = cur.fetchall()

for row in rows:
    print(row)


# Close the cursor and connection
cur.close()
conn.close()
