# Databricks notebook source
# MAGIC %run ../../Includes/_common

# COMMAND ----------

my_name = "Some name"

# COMMAND ----------

example_df = spark.range(16)


# COMMAND ----------

print(my_name)
display(example_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`${DA.paths.datasets}/nyctaxi-with-zipcodes/data`

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/nyctaxi-with-zipcodes/subsampled")
display(files)
