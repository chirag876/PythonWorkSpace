# ------------------------------------------------------------------ Database connectivity using mysql.connector 
# SQLAlchemy for SQL toolkit and Object-Relational Mapping
import mysql.connector
import pandas as pd
# MySQL database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'chirag',
    'database': 'world',
    'port': 3306,  # replace with the actual port number
}

try:
    # Establishing a connection to the MySQL database
    conn = mysql.connector.connect(**db_config)

    # SQL query to select all data from the table
    query = "SELECT * FROM city"

    # Fetching data into a Pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Displaying the first few rows of the DataFrame
    print(df.head())

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Closing the database connection in the 'finally' block to ensure it's closed even if an exception occurs
    if conn.is_connected():
        conn.close()
        
        
        
########################################################## Database connectivity using sqlalchemy 

from sqlalchemy import create_engine

# MySQL database connection parameters
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'chirag',
    'database': 'world',
    'port': 3306,  # replace with the actual port number
}

# Create a SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

try:
    # SQL query to select all data from the table
    query = "SELECT * FROM city"

    # Fetching data into a Pandas DataFrame using SQLAlchemy engine
    df = pd.read_sql_query(query, engine)
    
    # Displaying the first few rows of the DataFrame
    print(df.head())

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # No need to close the connection explicitly with SQLAlchemy
    pass


