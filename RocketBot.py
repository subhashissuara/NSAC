# --------------------
# RocketBot by BruteForce
# --------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
import sys
import requests
import launchlibrary as ll
import json

# To get the target
#Your_Name = input("Enter your WhatsApp Profile Name:")
Target = input(
    "Type your Target's name which should be same as the contact name stored in your phone:")
Target_Capitalize = Target.title()
Target_Upper = Target.upper()
Target_Lower = Target.lower()

Target_Split = Target_Capitalize.split()

# To make the bot respond to author by first name only
if len(Target_Split) > 1:
    Target_Firstname = Target_Split[0]
else:
    Target_Firstname = Target_Capitalize

# Defines chrome as the webdriver and opens the whatsapp web link
Driver = webdriver.Chrome()
wait = WebDriverWait(Driver, 20)
Driver.get('https://web.whatsapp.com/')

# Waits for any input to proceed further
input('Press Enter after scanning the QR Code...')

try:
    # Searches for target in recent chats
    Target_XML = Driver.find_element_by_xpath(
        '//span[@title = "{}"]'.format(Target_Capitalize))
    Target_XML.click()
except:
    try:
        # Searches for target in recent chats
        Target_XML = Driver.find_element_by_xpath(
            '//span[@title = "{}"]'.format(Target_Upper))
        Target_XML.click()
    except:
        try:
            # Searches for target in recent chats
            Target_XML = Driver.find_element_by_xpath(
                '//span[@title = "{}"]'.format(Target_Lower))
            Target_XML.click()
        except:
            try:
                # Searches for target in contact list
                Search_Bar = Driver.find_element_by_class_name('_2MSJr')
                Search_Bar.click()
                time.sleep(1)
                Search_Type = Search_Bar.find_element_by_xpath(
                    '//input[@class = "jN-F5 copyable-text selectable-text"]')
                Search_Type.send_keys(Target_Capitalize)
                time.sleep(2)
                Target_XML = Driver.find_element_by_xpath(
                    '//span[@title = "{}"]'.format(Target_Capitalize))
                Target_XML.click()
            except:
                try:
                    Target_XML = Driver.find_element_by_xpath(
                        '//span[@title = "{}"]'.format(Target_Upper))
                    Target_XML.click()
                except:
                    try:
                        Target_XML = Driver.find_element_by_xpath(
                            '//span[@title = "{}"]'.format(Target_Lower))
                        Target_XML.click()
                    except:
                        # If target is not found in any of the above cases
                        print(
                            "Target not found in contacts! Quitting bot in 5... 4... 3... 2... 1...")
                        time.sleep(5)
                        sys.exit()

Msg_For_Info = (f"Greetings {Target_Firstname}! I am RocketBot and I can help with rocket launch info!")
Msg_For_Info1 = "_Following are the rocket launches happening soon ->_"

launchlibrary_api = ll.Api()

# Function to send messages in selected chat


def SendStringMessage(Msg):
    Msg_Box = Driver.find_elements_by_xpath(
        '//div[@class="_3u328 copyable-text selectable-text"]')
    Msg_Box[0].send_keys(Msg)
    Send_Button = Driver.find_elements_by_xpath('//button[@class="_3M-N-"]')
    Send_Button[0].click()

# Function to get and reply weather of city requested


def getweather(City_Name):
    Api_key = '2580d00cea5b8a68bdb7c07a72f1ffbb'
    Base_url = "http://api.openweathermap.org/data/2.5/weather?"
    Complete_url = Base_url + "appid=" + Api_key + "&q=" + City_Name
    Response = requests.get(Complete_url)
    Response_JSON = Response.json()
    if Response_JSON["cod"] != "404":
        Response_JSON_Main = Response_JSON["main"]
        Current_Temperature = round((Response_JSON_Main["temp"] - 273.15), 2)
        Current_Pressure = Response_JSON_Main["pressure"]
        Current_Humidiy = Response_JSON_Main["humidity"]
        Weather = Response_JSON["weather"]
        Weather_Description = Weather[0]["description"]
        Msg_Temp = ("Temperature -> " + "*" +
                    str(Current_Temperature) + "°C" + "*")
        Msg_Pressure = ("Atmospheric pressure -> " + "*" +
                        str(Current_Pressure) + " mbar" + "*")
        Msg_Humidiy = ("Humidity -> " + "*" + str(Current_Humidiy) + "%" + "*")
        Msg_Description = ("Condition: " + "*" +
                           str(Weather_Description).capitalize() + "*")
        SendStringMessage(Msg_Temp)
        SendStringMessage(Msg_Pressure)
        SendStringMessage(Msg_Humidiy)
        SendStringMessage(Msg_Description)


def rocketinfo(number):
    url = f"https://launchlibrary.net/1.4/launch?next={number}&mode=summary"
    Response = requests.get(url)
    Response_JSON = Response.json()
    Response_JSON = Response_JSON["launches"]
    website = "https://launchlibrary.net/"
    for i in range(int(number)):
        Name = Response_JSON[i]["name"]
        Start = Response_JSON[i]["windowstart"]
        End = Response_JSON[i]["windowend"]
        T0 = Response_JSON[i]["net"]
        SendStringMessage(f"_Name of the Rocket:_ *{Name}*")
        SendStringMessage(f"_Start of launch protocol:_ *{Start}*")
        SendStringMessage(f"_End of launch protocol:_ *{End}*")
        SendStringMessage(f"_Launch time T-0:_ *{T0}*")
        SendStringMessage(f"_More information at:_ {website}")
        SendStringMessage("*--------------------------------------------------------*")


# Continues searching for keywords in messages received till script is exited by the user
while True:
    try:
        # Gets the last 2 messages in the selected chat
        try:
            Msg_Div = Driver.find_elements_by_xpath('//div[@class="FTBzM"]')
        except:
            Msg_Div = Driver.find_elements_by_xpath(
                '//div[@class="FTBzM _17BiH"]')

        Msg_Span = Msg_Div[0].find_elements_by_xpath(
            '//span[@class="selectable-text invisible-space copyable-text"]')
        Size_of_Msg_Span = len(Msg_Span)
        Last_Msgs_Received_List = []
        Last_Msg = (Msg_Span[Size_of_Msg_Span - 1].text).lower()
        #Second_Last_Msg = (Msg_Span[Size_of_Msg_Span - 2].text).lower()
        # Last_Msgs_Received_List.append(Second_Last_Msg)
        Last_Msgs_Received_List.append(Last_Msg)

        # Loops through the last 2 messages in selected chat and searches for keywords
        for i in range(len(Last_Msgs_Received_List)):
            Last_Msg_Received_Split = Last_Msgs_Received_List[i].split()
            if Last_Msg_Received_Split[0] == ".info" or Last_Msg_Received_Split[0] == ".rocketinfo":
                SendStringMessage(Msg_For_Info)
                SendStringMessage(Msg_For_Info1)
                rocketinfo(Last_Msg_Received_Split[1])

    except Exception as err:
        print(f"Script Error:{err}")
        time.sleep(0.5)
        pass
