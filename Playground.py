# Import the launchlibrary lib
import launchlibrary as ll
import requests
import json

# Create an instance of the API
api = ll.Api()  # You can also specify api url, api version...

# And request the next 5 launches, for example.
# Any argument after "api" is not constrained (w/ kwargs).
number = 1
url = f"https://launchlibrary.net/1.4/launch?next={number}"
Response = requests.get(url)
Response_JSON = Response.json()
Response_JSON = Response_JSON["launches"]
#print(Response_JSON[1]["name"])
print(Response_JSON)

x = Response_JSON[0]["id"]
url = (f"https://launchlibrary.net/1.4/mission/{x}")
Response = requests.get(url)
Response_JSON = Response.json()
#Response_JSON = Response_JSON["missions"]
#print(Response_JSON[1]["name"])
print(Response_JSON)
"""[Launch(id=1603,name=LauncherOne | Test Flight,tbddate=1,tbdtime=1,status=2,inhold=0,windowstart=2019-08-19 00:00:00+00:00,windowend=2019-08-19 00:00:00+00:00,net=2019-08-19 00:00:00+00:00,info_urls=[],vid_urls=[],holdreason=None,failreason=None,probability=-1,hashtag=None,agency=Agency(id=199,name=Virgin Orbit,abbrev=VO,type=3,country_code=USA,wiki_url=https://en.wikipedia.org/wiki/Virgin_Orbit,info_urls=['https://virginorbit.com/', 'https://twitter.com/virgin_orbit', 'https://www.youtube.com/channel/UCpz2PZJHMLcK7rH_1oup7Sw'],is_lsp=None,changed=2017-02-21 00:00:00),changed=2019-07-16 11:40:56,location=Location(id=39,name=Air launch to orbit,country_code=None,wiki_url=,info_urls=None,pads=[Pad(id=181,name=Mojave Air and Space Port,pad_type=None,latitude=35.059444,longitude=-118.151667,map_url=https://www.google.com/maps/place/35°03'34.0"N+118°09'06.0"W/,retired=None,locationid=None,agencies=None,wiki_url=https://en.wikipedia.org/wiki/Mojave_Air_and_Space_Port,info_urls=None)]),rocket=Rocket(id=173,name=LauncherOne,default_pads=None,family=None,wiki_url=https://en.wikipedia.org/wiki/LauncherOne,info_urls=[],image_url=https://s3.amazonaws.com/launchlibrary/RocketImages/placeholder_1920.png,image_sizes=[320, 480, 640, 720, 768, 800, 960, 1024, 1080, 1280, 1440, 1920]),missions=[{'id': 851, 'name': 'Test Flight', 'description': 'Payload-free test flight of the LauncherOne vehicle.', 'type': 13, 'wikiURL': '', 'typeName': 'Test Flight', 'agencies': [{'id': 199, 'name': 'Virgin Orbit', 'abbrev': 'VO', 'countryCode': 'USA', 'type': 3, 'infoURL': None, 'wikiURL': 'https://en.wikipedia.org/wiki/Virgin_Orbit', 'changed': '2017-02-21 00:00:00', 'infoURLs': ['https://virginorbit.com/', 'https://twitter.com/virgin_orbit', 'https://www.youtube.com/channel/UCpz2PZJHMLcK7rH_1oup7Sw']}], 'payloads': []}])]"""
