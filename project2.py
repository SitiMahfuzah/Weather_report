import requests
import smtplib

# define api key
API_KEY = "3953b94568a8e8e209ba43bf76e04460"
# Part 1: Pull Current Weather

# Step 1: Use requests lib to pull the current weather

current_weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Malacca&appid={}".format(API_KEY))


# Step 2: Convert the response as Dictionary and print out the current weather in format below:

current_weather_response = current_weather_response.json()
print(current_weather_response)

Weather = current_weather_response["weather"][0]["description"]
Temperature =  current_weather_response["main"]["temp"]
Humidity = current_weather_response["main"]["humidity"]
Feels_like = current_weather_response["main"]["feels_like"]
Wind_Speed =  current_weather_response["wind"]["speed"]



Temperature_in_celcius = float(Temperature) - 272.15

print("TODAY'S WEATHER")
print("================")
print("Weather :{}".format(Weather))
print("Temperature :{}".format(Temperature_in_celcius))
print("Humidity :{}".format(Humidity))
print("Feels Like :{}".format(Feels_like))
print("Wind Speed :{}".format(Wind_Speed))


# Part 2: Send email to the list of users


email_list = ['eloncook31@gmail.com', 'stevezuckerberg2018@gmail.com', 'jeffcookdata@gmail.com','sitimahfuzah0921@gmail.com']


# Step 1: Set up the SMTP Connection with Gmail
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()

# Step 2: Login with own account and app password
#try
conn.login('mahfuzahpythonclass@gmail.com','aspgbyhmpfvtncbf')

# Step 3: Complete the for loop for sending the emails one by one
for i in email_list:
    # Fill in the sender and recevier
    sender = "mahfuzahpythonclass@gmail.com"
    receivers = [i]

    # Fill out the message (including the From, To, Subject and email content)
    message = ("From : Siti Mahfuzah <mahfuzahpythonclass@gmail.com> \n"
    + "To : <" + i + " >\n"
    + "Subject : Weather Report \n" + "\nTODAY'S WEATHER \n" + "============== \n" 
    + "Weather :{}".format(Weather) + "\n" 
    + "Temperature :{}".format(Temperature_in_celcius) + " celcius \n" 
    + "Humidity :{}".format(Humidity) + " % \n"
    + "Feels Like :{}".format(Feels_like) + " celcius \n"
    + "Wind Speed :{}".format(Wind_Speed) + " meter/sec")

    # Actually sending out the email
#try
conn.sendmail(sender, receivers, message)