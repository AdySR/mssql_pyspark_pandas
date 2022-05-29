import pypyodbc # pip install pypyodbc
import pandas as pd # pip install pandas

SERVER_NAME = '<Server Name>'
DATABASE_NAME = '<Database Name>'

conn = pypyodbc.connect("""
    Driver={{SQL Server Native Client 11.0}};
    Server={0};
    Database={1};
    Trusted_Connection=yes;""".format(SERVER_NAME, DATABASE_NAME)
)

sql_query = """
SELECT TOP 5000 *
FROM [Table Name] WITH (NoLock)
"""

# With Headers
df1 = pd.read_sql(sql_query, conn)

# Without Headers
c = conn.cursor()
df2 = pd.DataFrame(c.execute(sql_query))