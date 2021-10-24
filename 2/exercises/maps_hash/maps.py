# Task 1 - Solution
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# Task 2 - Solution
# Part 1 - A list of all cities in the USA in alphabetic order.
print (1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print (city)

# Part 2 - All cities in Asia, in alphabetic order
print (2)
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print (city)