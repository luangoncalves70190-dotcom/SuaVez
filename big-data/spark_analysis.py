from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

ROOT = Path(__file__).resolve().parents[1]
file = str(ROOT/'datasets/raw/atendimentos_1m.csv')
spark = SparkSession.builder.appName('SuaVez-BigData').getOrCreate()
df = spark.read.option('header',True).option('inferSchema',True).csv(file)
print('Total de registros:', df.count())
print('Atendimentos por hospital:')
df.groupBy('hospital').agg(F.count('*').alias('atendimentos'),F.round(F.avg('espera_min'),2).alias('espera_media')).orderBy(F.desc('atendimentos')).show(truncate=False)
print('Horários de pico:')
df.groupBy('hora').count().orderBy(F.desc('count')).show(10)
print('Taxa de abandono por especialidade:')
df.groupBy('especialidade').agg(F.round(F.avg('abandonou')*100,2).alias('abandono_pct')).show(truncate=False)
spark.stop()
