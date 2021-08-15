#Dictionary comprehension

cities_in_F = {"New York": 32, "Boston":75, "Los Angeles":100, "Chicago":50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)
for i in cities_in_F.keys():
    print(i)
print(cities_in_F.values())
print(cities_in_F.items())


#IF
weather = {"New York":"snowing","Boston":"sunny","Los Angeles":"sunny","Chicago":"cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)



#IF ELSE
cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_weather = {key: "WARM" if value >= 50 else "Cold" for (key,value) in cities.items()}
print(desc_weather)

#Function
def check_temp(value):
    if value >=70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"

cities = {"New York": 32, "Boston": 75, "Los Angeles": 100, "Chicago": 50}
desc_weather = {key: check_temp(value) for (key,value) in cities.items()}
print(desc_weather)
