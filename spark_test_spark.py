spark/test_spark.py

from spark_session import create_spark_session

spark = create_spark_session()

print("Spark Version")

print(spark.version)

spark.stop()