#######################################################################################
# FirstName/Surname: Kwannate Theethuan
# Student ID: 65070027
# Github repository URL: https://github.com/yingnoon/IPA2024-Final-example-Kwannate.git
#######################################################################################
# Instruction
# Reads README.md in https://github.com/chotipat/NPA2023-Final-Example for more information.
#######################################################################################
 
#######################################################################################
# 1. Import libraries for API requests, JSON formatting, and time.

import requests  # สำหรับการทำ API requests
import json      # สำหรับการจัดการกับข้อมูล JSON
import time      # สำหรับการหน่วงเวลา (sleep)

#######################################################################################
# 2. Assign the Webex hard-coded access token to the variable accessToken.


accessToken = "Bearer YWVhMWUwMzMtYzk5Ny00NGYzLWE4MWEtNjQzNmYyZTFjNGY4YzRmMjUwZWYtYWU1_P0A1_1ad92174-dfe2-4740-b008-57218895946c" 

#######################################################################################
# 3. Prepare GetParameters to get the latest message for messages API.

# Defines a variable that will hold the roomId 
roomIdToGetMessages = "Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi" 

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    GetParameters = {
                            "roomId": roomIdToGetMessages,
                            "max": 1
                        }

#######################################################################################
# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get("https://webexapis.com/v1/messages",  # นี่คือ URL สำหรับดึงข้อความจากห้อง
                 params=GetParameters, 
                 headers={"Authorization": accessToken}
                )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception( "Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))
    
    # get the JSON formatted returned data
    json_data = r.json()
    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")
    
    # store the array of messages
    messages = json_data["items"]
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)
    
    # check if the text of the message starts with the magic character "/" and yourname followed by a location name
    # e.g.  "/chotipat San Jose"
    if message.find("/Kwannate") == 0:
    # ดึงชื่อเมืองจากข้อความ เช่น "/yourname San Jose" -> San Jose
        location = message.split(" ", 1)
    print(location[1]) 

#######################################################################################  
# 5. Prepare openweather Geocoding APIGetParameters..
        # Openweather Geocoding API GET parameters:
        # - "q" is the the location to lookup
        # - "limit" is always 1
        # - "key" is the openweather API key, https://home.openweathermap.org/api_keys
    openweatherGeoAPIGetParameters = {
            "q": location[1],
            "limit": 1,
            "appid": "2380568fc434753b5dfbaa59f9f10118",
        }

#######################################################################################       
# 6. Provide the URL to the OpenWeather Geocoding address API.
        # Get location information using the OpenWeather Geocoding API geocode service using the HTTP GET method
    r = requests.get("http://api.openweathermap.org/geo/1.0/direct", 
                             params = openweatherGeoAPIGetParameters
                        )
        # Verify if the returned JSON data from the OpenWeather Geocoding API service are OK
    json_data = r.json()
    print(json.dumps(json_data, indent=4))
        # check if the status key in the returned JSON data is "0"
    if not r.status_code == 200:
            raise Exception("Incorrect reply from OpenWeather Geocoding API. Status code: {}".format(r.statuscode))

#######################################################################################
# 7. Provide the OpenWeather Geocoding key values for latitude and longitude.
        # Set the lat and lng key as retuned by the OpenWeather Geocoding API in variables
    locationLat = json_data[0]["lat"]
    locationLng = json_data[0]["lon"]

#######################################################################################
# 8. Prepare openweatherAPIGetParameters for OpenWeather API, https://openweathermap.org/api; current weather data for one location by geographic coordinates.
        # Use current weather data for one location by geographic coordinates API service in Openweathermap
    # Prepare the OpenWeather API parameters
    openweatherAPIGetParameters = {
        "lat": locationLat,  # ละติจูดที่ได้จาก OpenWeather Geocoding API
        "lon": locationLng,  # ลองจิจูดที่ได้จาก OpenWeather Geocoding API
        "appid": "2380568fc434753b5dfbaa59f9f10118",  # ใส่ OpenWeather API Key ของคุณ
        "units": "metric"  # กำหนดให้เป็นหน่วยเมตริก (องศาเซลเซียส)
}

#######################################################################################
# 9. Provide the URL to the OpenWeather API; current weather data for one location.
    rw = requests.get("https://api.openweathermap.org/data/2.5/weather", 
                             params = openweatherAPIGetParameters
                        )
    json_data_weather = rw.json()
    print(json.dumps(json_data_weather, indent=4))

    if not "weather" in json_data_weather:
            raise Exception("Incorrect reply from openweathermap API. Status code: {}. Text: {}".format(rw.status_code, rw.text))

#######################################################################################
# 10. Complete the code to get weather description and weather temperature
    # ดึงข้อมูลคำอธิบายสภาพอากาศและอุณหภูมิ
    weather_desc = json_data_weather["weather"][0]["description"]  # รายละเอียดสภาพอากาศ
    weather_temp = json_data_weather["main"]["temp"]  # อุณหภูมิในหน่วยองศาเซลเซียส


#######################################################################################
# 11. Complete the code to format the response message.
        # Example responseMessage result: In Austin, Texas (latitude: 30.264979, longitute: -97.746598), the current weather is clear sky and the temperature is 12.61 degree celsius.
    responseMessage = "In {} (latitude: {}, longitude: {}), the current weather is {} and the temperature is {} degree celsius.\n".format(location[1], locationLat, locationLng, weather_desc, weather_temp)
    print("Sending to Webex Teams: " + responseMessage)

#######################################################################################
# 12. Complete the code to post the message to the Webex Teams room.         
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
       # Webex Teams HTTP headers
    HTTPHeaders = {
            "Authorization": accessToken,
            "Content-Type": "application/json"
        }

        # ข้อมูลที่จะโพสต์กลับไปยัง Webex Teams
    PostData = {
            "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNTFmNTJiMjAtNWQwYi0xMWVmLWE5YTAtNzlkNTQ0ZjRkNGZi",  # Room ID ที่ต้องการส่งข้อความกลับ
            "text": responseMessage  # ข้อความที่จัดรูปแบบแล้ว
        }

        # โพสต์ข้อความกลับไปยัง Webex Teams room
    r = requests.post("https://webexapis.com/v1/messages", 
                        data=json.dumps(PostData), 
                        headers=HTTPHeaders
                        )

        # ตรวจสอบว่าการโพสต์สำเร็จหรือไม่
    if r.status_code != 200:
            raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))
