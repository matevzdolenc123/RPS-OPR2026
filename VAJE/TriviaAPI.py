import random
import requests
from pprint import pprint
import html
 
vpr = int(input("Koliko vprašanj želiš? "))
url = f"https://opentdb.com/api.php?amount={vpr}&category=28&difficulty=easy&type=multiple"
klic = requests.get(url).json()
 
vprasanja = klic["results"]
 
for v in vprasanja:
    print("-"*80)
    pprint(v)
    print("-"*80)
 
    print(html.unescape(v["question"]))  #odstrani HTML znake
    print(v["correct_answer"])
    print(v["incorrect_answers"])
 
odgovori = [v["correct_answer"]]+ v["incorrect_answers"]
random.shuffle(odgovori)

for i, odgovor in enumerate(odgovori):
    print(f"{i+1}-{html.unescape(odgovor)}")

izbira = int(input("odgovor: "))

pravilen= v["correct_answer"]

print(odgovori[izbira-1]== pravilen)
