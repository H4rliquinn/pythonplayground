import csv


class City:
    def __init__(self, city, lat, lon):
        self.city = city
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f'{self.city} is at lat:{self.lat} lon:{self.lon}'


csv_file = open('cities.csv')
# reader = csv.reader(csv_file, delimiter=',')
reader = csv.DictReader(csv_file)

# next(reader)
citylist = []

for line in reader:
    # print(line)
    # citylist.append(City(line[0], line[3], line[4]))
    citylist.append(City(line['city'], line['lat'], line['lng']))

print(citylist)
print(citylist[0].city)
