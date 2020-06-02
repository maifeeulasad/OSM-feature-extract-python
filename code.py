import requests
from lxml import html
from bs4 import BeautifulSoup

#link="https://wiki.openstreetmap.org/wiki/Map_Features"
link="E:/OSM-feature-extract-python/official.html"
perrow = 6

features={}

try:
    count = 0
    key = ''
    #r = requests.get(link)
    #soup = BeautifulSoup(page.read())
    soup = BeautifulSoup(open(link), "html.parser")
    #print(soup)
    #print(soup)
    #for table in soup.findAll("table", {"class": "wikitable taginfo-taglist"}):
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
