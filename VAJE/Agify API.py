import requests

imena=["Matevž", "Maj", "Nik", "Jakob", "Ažbe", "Matija"]

def podatki(ime):
    url = "https://api.agify.io"
    odgovor = requests.get(url, params={"name":ime})
    return odgovor.json()

najstarejše_ime = None
najstarejša_starost= 0

for ime in imena:
    ime = podatki(ime)
    starost=ime["age"]

    print(ime, starost)

    if starost> najstarejša_starost:
        najstarejša_starost= starost
        najstarejše_ime=ime

    print(f"Najstarejše ime je {najstarejše_ime}")
    print(f"Najvišja starost je {najstarejša_starost}")
