import requests
def trenutna_temp(lat, long):
    base_url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code&timezone=auto"
    call= requests.get(base_url).json()
    print(call["current"]["temperature_2m"])
#trenutna_temp(45.12, 14.5)

# izpis temperature za naslednjih 7 dni
def temp7(lat,lon):
    base_url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    call= requests.get(base_url).json()
    print(call["daily"]["temperature_2m_max"])
    print(call["daily"]["temperature_2m_min"])

#temp7(45.12, 14.5)

#Ugotovi, kateri dan bo najtoplejši oz. najhladnejši, in izpiši datum ter temperaturo.
def vaja3(lat,lon):
    base_url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    all= requests.get(base_url).json()
    print(call["daily"]["time"])
    print(call["daily"]["temperature_2m_max"])
    print(call["daily"]["temperature_2m_min"])

    najtemp=max_temp[0]
    mintemp=min_temp[0]
    datum_naj=datum[0]
    datum_min=datum[0]
def trenutna_temp2(lat, lon):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params={"latitude": lat,
            "longitude" : lon,
            "current": "temperature_2m",
            "timezone" : "auto",
            "forecast_days" : 1
            }
    call= requests.get(base_url, params=params)

    json= call.json()
    return json["current"]["temperature_2m"]

cities = [
    ("Ljubljana", 46.0511, 14.5051 ),
    ("Maribor", 46.5558, 15.6459),
    ("Celje", 46.2309, 15.2604),
    ("Kranj", 46.2389, 14.3556),
]

for c in cities[:4]:
    print(trenutna_temp2(c[1], c[2]), c[0])

        
