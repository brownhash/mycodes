import csv
import sys
#code
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
 
next(csv_reader)

with open('new-file.csv', 'w') as new_file:
	csv_writer = csv.writer(new_file, delimiter='\t')
