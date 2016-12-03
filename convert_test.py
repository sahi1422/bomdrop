import csv

"""
with open('input_sample_1.txt') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Qty'], row['Value'], row['Parts'], row['Description'])
"""

input_file = 'input_sample_1.txt'
output_file = 'output_test.txt'

csvinput = open(input_file, 'rb')
csvoutput = open(output_file, 'wb')
reader = csv.DictReader(csvinput)
writer = csv.writer(csvoutput, delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL)
writer.writerow(['Quantity','Value', 'Parts', 'Description'])
for row in reader:
    writer.writerow([row['Qty'], row['Value'], row['Parts'], row['Description']])

