import csv

with open('example.csv','r') as file_handler:
    csv_reader=csv.reader(file_handler)
    print(file_handler.read())

