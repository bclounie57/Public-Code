import csv
import json
#add comment

csvfile = open('bruce-routetags-zone.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("subnet","name")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, indent=1)
    jsonfile.write('\n')
