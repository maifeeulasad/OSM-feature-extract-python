import requests
from lxml import html
from bs4 import BeautifulSoup
import asyncio
import threading
#from requests_html import HTMLSession


link="https://wiki.openstreetmap.org/wiki/Map_Features"
#link="E:/OSM-feature-extract-python/official.html"
perrow = 6

features={}

@asyncio.coroutine
async def extract_feature():
    try:
        count = 0
        key = ''
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, requests.get, link)
        soup = BeautifulSoup(response, "html.parser")
        for table in soup.findAll("table"):
            for td in table.findAll("td"):
                if count%6 is 0:
                    key = td.find("a").contents[0].lstrip()
                    if key in features:
                        pass
                    else:
                        features[key]=[]
                elif count%6 is 1:
                    try:
                        content=td.find("a").contents[0].lstrip()
                        print(key," --- ",content)
                        features[key].append(content)
                    except Exception as ie:
                        print(ie,"<<--encountered")
                    #print(content)
                count+=1
            print("------")
    except Exception as oe:
        print(oe)
    print(features)


loop = asyncio.get_event_loop()
result = loop.run_until_complete(extract_feature)

#asyncio.run(())
