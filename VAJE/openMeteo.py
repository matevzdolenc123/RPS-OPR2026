import requests
def trenutna_temp(lat, long):
    base_url=f"https://api.open-meteo.com/v1/forecast?latitude=(lat)&longitude=(long)&current=temperature_2m&timezone=auto&forecast_days=1"
    call= requests.get(base_url).json()
    print(call["current"]["temperature_2m"])
trenutna_temp(45.12, 14.5)