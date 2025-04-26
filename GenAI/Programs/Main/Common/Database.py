

from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine

def get_database_connection(server, database, username, password):
    """
    Creates and returns a SQLAlchemy engine and SQLDatabase object.

    Args:
        server (str): The database server name.
        database (str): The database name.
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        SQLDatabase: A LangChain SQLDatabase object.
    """
    connection_string = (
        f"mssql+pyodbc://{username}:{password}@{server}/{database}?"
        "driver=ODBC Driver 17 for SQL Server"
    )
    engine = create_engine(connection_string)
    return SQLDatabase(engine)

def get_db():
    """
    Returns a SQLAlchemy engine and SQLDatabase object.

    Returns:
        SQLDatabase: A LangChain SQLDatabase object.
    """
    SERVER = 'ANVIRYZEN\\SQLEXPRESS'
    DATABASE = 'BlogDB'
    USERNAME = 'sa'
    PASSWORD = 'sa%40123'

    return get_database_connection(SERVER, DATABASE, USERNAME, PASSWORD)

# Run a sample query
# print(db.run("SELECT * FROM Article;"))


# pip install langchain-community sqlalchemy
# pip install pyodbc
# pip install pymssql

# pip install -qU langchain-google-genai langchain-community sqlalchemy