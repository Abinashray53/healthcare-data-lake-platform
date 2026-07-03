spark/spark_session.py

from pyspark.sql import SparkSession


def create_spark_session():

    spark = (
        SparkSession.builder
        .appName("HealthcareDataLake")
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "4")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark
