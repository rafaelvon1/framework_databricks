df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/FileStore/tables/clientes.csv")

display(df)
from pyspark.sql.functions import col

df_limpo = df.dropna(subset=["id", "nome", "idade", "salario"])

display(df_limpo)
from pyspark.sql.functions import when, upper

df_transformado = df_limpo \
    .withColumn("nome_maiusculo", upper(col("nome"))) \
    .withColumn(
        "faixa_etaria",
        when(col("idade") < 18, "menor")
        .when(col("idade") <= 60, "adulto")
        .otherwise("idoso")
    )

display(df_transformado)
df_filtrado = df_transformado.filter(col("salario") > 3000)

display(df_filtrado)

df_agregado = df_filtrado.groupBy("faixa_etaria") \
    .count() \
    .withColumnRenamed("count", "qtd_clientes")



