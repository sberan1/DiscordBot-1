import json
import requests
from datetime import datetime
import os

def getToken():
  url = "https://bakalari.ssps.cz/api/login"
  body = "client_id=ANDR&grant_type=password&username="+ os.getenv('USERNAME')+ "&password=" + os.getenv('PASSWORD')
  response = requests.post(url, data = body, headers = {"Content-Type":"application/x-www-form-urlencoded"})
  json_data = json.loads(response.text)
  token = json_data["access_token"]
  return token

def getSuplovani():
  url = "https://bakalari.ssps.cz/api/3/substitutions"
  response = requests.get(url, headers = {"Content-Type":"application/x-www-form-urlencoded", "Authorization":"Bearer " + getToken()})
  json_data = json.loads(response.text)
  returnString = ""
  for k in json_data["Changes"]:
    datum = k["Day"]
    datumFormatovane =  datetime.strptime(datum, "%Y-%m-%dT%H:%M:%S+01:00")
    denKdyOdpada = str(datumFormatovane.day) + "-" + str(datumFormatovane.month) + "-" + str(datumFormatovane.year)
    coOdpada = k["Hours"]
    casKdyOdpada = k["Time"]
    descriptionOdpada = k["Description"]
    returnString += denKdyOdpada + "\n" + coOdpada + "\n" + casKdyOdpada + "\n" + descriptionOdpada + "\n \n"
  return returnString