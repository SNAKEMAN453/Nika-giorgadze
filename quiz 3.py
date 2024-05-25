import requests
import json


filepath_json = "data.json"
filepath_base= "database.sqlite"
name = str(input("Enter your name: "))
api_url = f"https://api.funtranslations.com/translate/morse?text={name}"
api_response = requests.get(api_url)
statuscode = api_response.status_code
info = api_response.json()

print(info["contents"]["translated"])


#json ფორმატით შეინახება ინფორმაცია

with open(filepath_json, "w") as file:
    json.dump(info, file, indent=4)

import sqlite3

conn = sqlite3.connect(filepath_base)
cursor = conn.cursor()


#ინფორმაცია შეინახება მიწოდებული სახელისა და გადათარგმნილი სახელის შესახებ translations ცხრილში.


cursor.execute(" CREATE TABLE IF NOT EXISTS translations (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, morse_name Text) ")


data_tuple = (info["name"], info["morse_name"])

cursor.execute(""" INSERT INTO translations (name, morse_name) VALUES (?, ?)""", data_tuple)
conn.commit()
conn.close()