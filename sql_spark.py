from typing import get_origin
from pyspark.sql import SparkSession
import findspark
findspark.init() 

connector_type ='com.microsoft.sqlserver.jdbc.spark'
sql_username ='aditya'
sql_password ='Tiger@90'
sql_dbName ='feederDB'
sql_serverName = 'jdbc:sqlserver://{ICEN472}'
sql_url = sql_serverName + ";" + "databaseName=" + sql_dbName + ";"
sql_tableName ='dbo.feederDB'
spark = SparkSession.builder.appName('Pyspark sql demo').getOrCreate()

jdbcDF = spark.read \
        .format(connector_type) \
        .option("url", sql_url) \
        .option("dbtable", sql_tableName) \
        .option("user", sql_username) \
        .option("password", sql_password).load()


print(jdbcDF.head(2))