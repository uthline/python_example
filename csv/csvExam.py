import csv

f = open('test.csv', 'r')
reader = csv.reader(f)

for row in reader:
    print("%s는 %s원입니다." % (row[0], row[1]))

f.close()