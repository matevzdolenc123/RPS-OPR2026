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

    for i in range(len(datumi)):
        if max_temp[i]> najtemp:
            najtemp=i
        
