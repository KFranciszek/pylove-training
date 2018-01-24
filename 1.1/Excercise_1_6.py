from countries import countries

max_area = 0
max_country = ""
for country in countries:
    if country["area"] > max_area:
        max_area = country["area"]
        max_country = country["name"]["official"]
print(max_country + " with area of " + str(max_area))

max_borders = []
max_country = ""
for country in countries:
    if len(country["borders"]) > len(max_borders):
        max_borders = country["borders"]
        max_country = country["name"]["official"]
print("{0} has {1} neighbours - {2}".format(max_country, len(max_borders),max_borders))
