# Python code that demonstrates data pipelines using various techniques and libraries:
# Simple data pipeline using generators
def generate_data():
    for i in range(10):
        yield i

def square_data(data):
    for num in data:
        yield num ** 2

def print_data(data):
    for num in data:
        print(num)

# Usage
data_generator = generate_data()
squared_data = square_data(data_generator)
print_data(squared_data)

# Data pipeline using itertools
import itertools

def multiply_data(data):
    return (num * 3 for num in data)

data = [1, 2, 3, 4, 5]
multiplied_data = multiply_data(data)
print(list(multiplied_data))  # Output: [3, 6, 9, 12, 15]

# Data pipeline using pandas
import pandas as pd

# Load data from CSV
data = pd.read_csv('data.csv')

# Transform data
transformed_data = data.dropna()  # Drop rows with missing values
transformed_data = transformed_data[transformed_data['age'] > 30]  # Filter by age

# Save transformed data to a new CSV file
transformed_data.to_csv('transformed_data.csv', index=False)

# Data pipeline using Apache Beam (Google Cloud Dataflow)
import apache_beam as beam
import csv

def read_data(input_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            yield row

def filter_data(data):
    for row in data:
        if int(row[1]) > 30:
            yield row

def write_data(data, output_file):
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

with beam.Pipeline() as pipeline:
    input_data = pipeline | 'Read Data' >> beam.Create(read_data('input.csv'))
    filtered_data = input_data | 'Filter Data' >> beam.FlatMap(filter_data)
    filtered_data | 'Write Data' >> beam.Map(write_data, 'output.csv')

# Data pipeline using Apache Spark
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("DataPipeline").getOrCreate()

# Load data from CSV
data = spark.read.csv("data.csv", header=True, inferSchema=True)

# Transform data
transformed_data = data.filter(data.age > 30)

# Save transformed data to a new CSV file
transformed_data.write.csv("transformed_data.csv", mode="overwrite", header=True)
