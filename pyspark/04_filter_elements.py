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

# filter(f) - A new RDD is returned containing the elements, which satisfies the function inside the filter.
words_filter = words.filter(lambda x: 'spark' in x)  # filter out the strings containing ''spark"
filtered = words_filter.collect()
print("Fitered RDD -> %s" % filtered)
print()

# map(f, preservesPartitioning = False) - A new RDD is returned by applying a function to each element in the RDD.
words_map = words.map(lambda x: (x, 1))  # We form a key value pair and map every string with a value of 1.
mapping = words_map.collect()
print("Key value pair -> %s" % mapping)
print()

# reduce(f) - After performing the specified commutative and associative binary operation, the element in the RDD is
# returned.
# Here, we are importing add package from the operator and applying it on ‘num’ to carry out a simple addition
# operation.
from operator import add

nums = sc.parallelize([1, 2, 3, 4, 5])
adding = nums.reduce(add)

print("Adding all the elements -> %i" % adding)
