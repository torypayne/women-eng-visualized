import gdata
from gdata.spreadsheet.service import SpreadsheetsService
import json

#Basic info to pull the sheet and start scraping.  Since this is a public sheet we can
#skip the whole authentication song and dance
key = '0AlZH8QBl60oodEJTdFA5TlZOcDJCMU02RkZoSHF5SHc'
client = SpreadsheetsService()
sheet_key = "od6"



#Step 1: get all the data from the sheets
#Step 2: Row by row, convert to dictionaries, then extract the key values and store it
#In our new dictionary
data = client.GetListFeed(key, sheet_key, visibility='public', projection='values').entry

cleaned_data = {}

for i in data:
	info = i.custom
	key = info["key"].text
	cleaned_data[key] = {}
	cleaned_data[key]["company"] = info["company"].text
	cleaned_data[key]["team"] = info["team"].text
	cleaned_data[key]["numfemaleeng"] = info["numfemaleeng"].text
	cleaned_data[key]["numeng"] = info["numeng"].text
	cleaned_data[key]["percentfemaleeng"] = info["percentfemaleeng"].text
	cleaned_data[key]["lastupdated"] = info["lastupdated"].text

del cleaned_data["all"]
# print cleaned_data

f = open("data.py", "w")

line = "data ="+str(cleaned_data)+"\n"

f.write(line)

f.close()

j = open("data.json", "w")
j.write(json.dumps(cleaned_data))


print "Success!"

