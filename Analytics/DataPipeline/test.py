import pyodbc
import time

# Define your database connection parameters
server='10.130.205.31',
database='IMS_Base',
username='ims_kmg_dev',
password='the5.Guide.jested.a.fact.fools.the1.vestibule',
driver = '{ODBC Driver 17 for SQL Server}'

# Connect to the database
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};'
conn = pyodbc.connect(driver=driver, 
                      host=server, database=database, trusted_connection='yes',
                      user=username, password=password)
cursor = conn.cursor()
cursor.execute("select * from dbo.tblQuotes")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Function to fetch and process updated data
def process_updated_data(cursor):
    # Fetch the total number of records in the table
    total_records_query = "SELECT COUNT(*) FROM ChangeLog"
    print(total_records_query)
    cursor.execute(total_records_query)
    total_records = cursor.fetchone()[0]
    print(f"Total records in the table: {total_records}")
    # Execute your SQL query to fetch the updated data
    query = """
            SELECT Column1, Column2, ... FROM ChangeLog
            """
    cursor.execute(query)
    
    # Fetch the updated data
    updated_data = cursor.fetchall()
    
    # Process the updated data
    for row in updated_data:
        # Perform your processing tasks here
        print(row)  # Example: printing the updated data
        
    # Commit the transaction
    conn.commit()

# Main loop to continuously check for updates
while True:
    try:
        # Check for updates every 'n' seconds
        process_updated_data(cursor=cursor)
        time.sleep(10)  # Adjust the interval as needed
    except KeyboardInterrupt:
        print("Process interrupted. Exiting...")
        break

# Close the database connection
conn.close()
