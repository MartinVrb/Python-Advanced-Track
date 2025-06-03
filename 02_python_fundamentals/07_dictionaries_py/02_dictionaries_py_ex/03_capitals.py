my_countries = input().split(", ")
my_capitals = input().split(", ")
countries_dict = {print(f"{country} -> {capital}") for country, capital in dict(zip(my_countries, my_capitals)).items()}
