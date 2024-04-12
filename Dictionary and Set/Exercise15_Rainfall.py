def get_rainfall():
    rainfall = {}
    total_rainfall = 0
    city_count = 0

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break
        mm_rain = int(input('Enter mm rain: '))
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)
        total_rainfall +=mm_rain
        city_count += 1

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')

    if city_count != 0:
        average_rainfall = total_rainfall / city_count
        print("Average rainfall:", average_rainfall)
    else:
        print("No data entered.")

get_rainfall()