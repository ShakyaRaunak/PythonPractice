# http://renien.com/blog/accessing-pyspark-pycharm/

import sys

# $ pip install pyspark

# Path for spark source folder
# os.environ['SPARK_HOME'] = "C:\\SDKs\\spark-2.3.0-bin-hadoop2.7"

# Append pyspark to Python Path
# sys.path.append("C:\\Users\\rauna\\Desktop\\PythonPractice\\venv\\Lib\\site-packages\\pyspark")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("Successfully imported Spark Modules")
except ImportError as e:
    print("Can not import Spark Modules", e)
    sys.exit(1)

# Initialize SparkContext
sc = SparkContext("local", "pyspark app")
words = sc.parallelize(["scala", "java", "hadoop", "spark", "akka"])

print(words.count())
