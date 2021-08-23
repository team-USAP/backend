from center.models import City
import csv
i = 0
with open('city.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        c = City.objects.create(name=row[0], state=row[1])
        c.save()
        i = i+1
        print(i)
