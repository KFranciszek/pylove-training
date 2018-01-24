from countries import countries

for country in countries:
    if country["subregion"] == "Northern America":
        print(country["name"]["official"])

for country in countries:
    if country["region"] != "Africa":
        print(country)

for country in countries:
    if len(country["currency"]) > 1:
        print("{0} - currencies: {1}".format(country["name"]["official"],country["currency"]))

for country in countries:
    if country["capital"] and country["capital"][0] == "W":
        print(country["name"]["official"] + ' - ' + country["capital"])