# https://www.tutorialspoint.com/pyspark/pyspark_rdd.htm

"""
RDD (Resilient Distributed Dataset) are the elements that run and operate on multiple nodes to do parallel processing on
a cluster. They are immutable and fault tolerant.
"""

from pyspark import SparkContext

sc = SparkContext("local", "pyspark app")
# sc.setLogLevel("WARN")
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

# count() - Number of elements in the RDD is returned.
counts = words.count()
print("Number of elements in RDD -> %i" % counts)
print()

# collect() - All the elements in the RDD are returned.
coll = words.collect()
print("Elements in RDD -> %s" % coll)
print()
