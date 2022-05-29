import pypyodbc as pyodbc
import pandas as pd

ServerName = 'ICEN472'
DatabaseName = 'feederDB'

conn = pyodbc.connect("""
    Driver={{SQL Server Native Client 11.0}};
    Server={0};
    Database={1};
    Trusted_Connection=yes;
""".format(ServerName, DatabaseName))

sql_query ="""
SELECT TOP (1000) [id]
  FROM [dbo].[adityaTest]
"""

df_sql_query = pd.read_sql(sql_query,conn)

print(df_sql_query.head(10))