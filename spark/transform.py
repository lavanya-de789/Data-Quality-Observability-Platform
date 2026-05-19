from pyspark.sql import SparkSession

spark=(SparkSession.builder
.appName(
'QualityTransform'
)
.getOrCreate())

df=spark.read.parquet(
'data/validated'
)

clean=df.dropDuplicates()

clean.write.mode(
'overwrite'
).parquet(
'data/final'
)

print(
'completed'
)
