city_list = []

while True:
    city = input("Enter a city name (or 'done' when finished): ")
    if city == "done":
        break
    else:
        city_list.append(city)

print(city_list)