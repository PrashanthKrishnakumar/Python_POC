
Task_1 1.
Get a file (csv/ text) from online which contains multi line record.
Convert that multi line record into single line record using python code

import csvjshcklsgjs

with open("C:/Users/prasanth.venugopal/Downloads/datasetss/hollywood_2025_hype_sentiment.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        flitering = row[9]
        single_line_record = "".join(flitering.strip())
        print(single_line_record)

2. Get a Fixed Width File as an input and convert it into a CSV file using python


with open("C:/Users/prasanth.venugopal/Downloads/datasetss/Fixed_Width_ File.txt","r") as input_file, open("Out_put_file_after_reading.csv","w") as output_flie:

    for line  in input_file:

        print(line.strip() )
        output_flie.write(line)


3.	Write a generic python code which converts xml file to csv file
import xml.etree.ElementTree as ET
import csv

tree = ET.parse('students.xml')
root = tree.getroot()
data = []

for student in root.findall('student'):
    row = {
        'id' : student.get('id'),
        'name' : student.find('name').text,
        "age" : student.find("age").text,
        "grade": student.find("grade").text
    }

    data.append(row)

headers = ["id","name","age","grade"]

with open('students.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

with open("students.csv","r") as f:
    for files in f:
        print(files)



4.	Get a JSON file(It should be a complex one(nested JSON , List in List)) convert it into CSV using Python

import json
import csv


with open('employees.json', 'r') as file:
    data = json.load(file)

employees = data['employees']

csv_rows = []


for emp in employees:

    row = {

        'ID': emp['employee_id'],
        'Name': emp['name'],
        'Age': emp['age'],
        'Email': emp['email'],


        'Street': emp['address']['street'],
        'City': emp['address']['city'],
        'Zipcode': emp['address']['zipcode'],

        'Department': emp['job']['department'],
        'Position': emp['job']['position'],
        'Salary': emp['job']['salary'],


        'Skills': ', '.join(emp['skills']),


        'Project1_Name': emp['projects'][0]['name'],
        'Project1_Role': emp['projects'][0]['role'],
        'Project1_Hours': emp['projects'][0]['hours'],

        'Project2_Name': emp['projects'][1]['name'],
        'Project2_Role': emp['projects'][1]['role'],
        'Project2_Hours': emp['projects'][1]['hours'],
    }

    csv_rows.append(row)


print(csv_rows)


with open('simple_employees.csv', 'w', newline='') as file:

    column_names = csv_rows[0].keys()

    writer = csv.DictWriter(file, fieldnames=column_names)
    writer.writeheader()
    writer.writerows(csv_rows)



5.	Prepare a data quality metrics function that is generic functions,
 it should get csv file as input ,code should give more information about file like  nulls , duplicates along with row and column where null and duplicates exists, and count of records , what is the file size, word count, any PII data of column, i need a parameter as list ,if i specify a primary key as a list to that function it should tell me any duplicates in that columns or not if exist then they row and column number should get , similar for not null column as parameter , list of non null values , we need to print primary key and column which has null value.


import pandas as pd
import os
from collections import Counter


def counter(data):
    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0

    data_str = data.to_string()
    num_lines = len(data)

    for line in data_str.split('\n'):
        words = line.split()
        num_words += len(words)
        num_spaces += line.count(' ')

        for char in line:
            if char != ' ' and char != '\n':
                num_charc += 1

    return num_words, num_lines, num_charc, num_spaces


file_path = "C:/Users/prasanth.venugopal/Downloads/datasetss/youtube_recommendation_dataset.csv"
data = pd.read_csv(file_path)

num_words, num_lines, num_charc, num_spaces = counter(data)

datainfo = data.info()

datadescribe = data.describe()

duplicate_records = data[data.duplicated(keep=False)]

row_count = len(data)

file_size_bytes = os.path.getsize(file_path)

word_counts = Counter()
for column in data.select_dtypes(include=['object']):
    for value in data[column].dropna():
        word_counts.update(str(value).lower().split())

print(sum(word_counts.values()))










