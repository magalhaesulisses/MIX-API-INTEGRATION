import requests
import json
import base64
import requests.utils

BaseUrl = "https://api.open-meteo.com/v1"

##Identity Server
print("1. Get Identity server configuration")
ConfigUrl = BaseUrl + "/forecast"
Params = "?latitude=52.52&longitude=13.419998"
ConfigUrl = ConfigUrl + Params
print("Request: " + ConfigUrl)
ConfigResponse = requests.get(ConfigUrl)
print("Response Status Code: " + str(ConfigResponse.status_code), ConfigResponse.reason)
Response = json.loads(ConfigResponse.content)

print("Latitude: " + str(Response["latitude"]))
print("Longitude: " + str(Response["longitude"]))
print("Gen: " + str(Response["generationtime_ms"]))
print("UTF: " + str(Response["utc_offset_seconds"]))
print("Timezone: " + str(Response["timezone"]))