import requests
import json

endpoint = "https://api.foursquare.com/v3/places/search"

city = input("Введите название города (ENG/РУС): ")
fields = "categories,name,rating,location"
params = {"near": city,
          "fields": fields,
          "limit": 50}

headers = {
    "Accept": "application/json",
    "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)

if response.status_code == 200:
    
    data = json.loads(response.text)

    venues = data["results"]
    categories = set(venue["categories"][0]["name"] for venue in venues)
    print(f"В городе {city} есть:")
    print()
    print(*categories, sep='\n')
    print()
    user_choise = input("Введите название категории для поиска: ").title()
    print()

    print(f'В выбранной категории {user_choise} найдено:')
    print()
    for venue in venues:
        if venue["categories"][0]["name"] == user_choise:
            print("Название:", venue["name"])
            print("Рейтинг:", venue["rating"])
            print("Адрес:", venue["location"]["formatted_address"])
            print()
    
else:
    print("Запрос API завершился неудачей с кодом состояния:", response.status_code)
    print(response.text)