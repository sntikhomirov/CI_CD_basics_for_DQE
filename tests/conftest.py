import pytest
import pymssql


@pytest.fixture
def connection():
    conn = pymssql.connect(
        server='localhost:1433',
        user='Test',
        password='Password1234',
        database='TRN'
    )
    cursor = conn.cursor()
    return cursor


@pytest.fixture
def execute_sql(connection, query):
    connection.execute(query)
    row = connection.fetchone()
    while row:
        print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]))
        row = connection.fetchone()
