# NPA2023 Final Example

- Name/Surname:
- Student ID:
- Github repository URL:

## Instruction

1. Fork this repository to your github repository.
2. Rename file name by appending your name to "npa2023-final-example.py" (e.g. npa2023-final-example-chotipat.py).
3. Clone your github repository to your local computer repository.
4. Complete all 12 tasks below by replacing code to all <!!!REPLACEME!!!!> in "npa2023-final-example-yourname.py".
5. Commit "npa2023-final-example-yourname.py" to your local repository once in a while or whenever you completed some of the 12 tasks. Be sure to make good commit messages.
6. Push your local repository to your github repository.

## This program

- Uses the hard-coded access token.
- Monitors the NPA2023 Webex Team room every second for "/yourname location" message.
- Extract the location (city name) from a message starting with “/yourname location” (e.g. /chotipat Washington, DC -> Washington, DC).
- Discovers GPS coordinates (latitude and longitude) for the "location" using openweather Geocoding API.
- Discovers the current weather description and temperature in degree Celsius of the specified latitude and longitude using openweathermap API.
- Formats and sends the results back to the NPA2023 Webex Teams room

## The examinee will

1. Import libraries for API requests, JSON formatting, and time.
2. Assign the Webex hard-coded access token to the variable accessToken.
3. Prepare GetParameters to get the latest message for messages API.
4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
5. Provide your openweather Geocoding APIGetParameters.
6. Provide the URL to the openweather Geocoding address API.
7. Provide the openweather Geocoding key values for latitude and longitude.
8. Prepare openweatherAPIGetParameters for OpenWeather API; current weather data for one location by geographic coordinates.
9. Provide the URL to the OpenWeather API; current weather data for one location.
10. Complete the code to get weather description and weather temperature.
11. Complete the code to format the response message.
12. Complete the code to post the message to the Webex Teams room.
