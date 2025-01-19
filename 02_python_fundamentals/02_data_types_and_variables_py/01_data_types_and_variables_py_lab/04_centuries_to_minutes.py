from math import floor

century = int(input())
years = century * 100
days = floor(years * 365.2422)
hours = floor(days * 24)
minutes = floor(hours * 60)
print(f"{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
