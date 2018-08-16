import csv

def manhattan_distance():
    pass

k = 3
instances = []
new_instance = ('nova',0.3,0.7)

with open('base-knn.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        instances.append(row[1:])

instances.pop(0)
for value in instances:
    print(value)
