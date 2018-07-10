# https://www.tutorialspoint.com/pyspark/pyspark_rdd.htm

from pyspark import SparkContext

sc = SparkContext("local", "pyspark app")
words = sc.parallelize(
    ["scala",
     "java",
     "hadoop",
     "spark",
     "akka",
     "spark vs hadoop",
     "pyspark",
     "pyspark and spark"]
)

# cache() persists the RDD with the default storage level (MEMORY_ONLY). You can also check if the RDD is cached or not.
words.cache()
caching = words.persist().is_cached

print("Words got cached > %s" % caching)
