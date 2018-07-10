# https://www.tutorialspoint.com/pyspark/pyspark_rdd.htm

from pyspark import SparkContext

sc = SparkContext("local", "pyspark app")

# Here, there are two pair of elements in two different RDDs. After joining these two RDDs, we get an RDD with elements
# having matching keys and their values.
x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])

# join(other, numPartitions = None) - returns RDD with a pair of elements with the matching keys and all the values for
# that particular key.
joined = x.join(y)
final = joined.collect()

print("Join RDD -> %s" % final)
