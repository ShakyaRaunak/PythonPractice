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


# foreach(f) - Returns only those elements which meet the condition of the function inside foreach.
def f(x):
    print(x)


fore = words.foreach(f)
