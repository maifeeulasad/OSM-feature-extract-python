from lxml import html
from bs4 import BeautifulSoup
from requests_futures.sessions import FuturesSession


link="https://wiki.openstreetmap.org/wiki/Map_Features"
#link="E:/OSM-feature-extract-python/official.html"
perrow = 6

features={}

try:
    count = 0
    key = ''
    session = FuturesSession()
    future = session.get(link)
    response = future.result()
    print(response)
    soup = BeautifulSoup(response.content, "html.parser")
    for table in soup.findAll("table"):
        for tr in table.findAll("tr"):
            perrow=len(tr.findAll("td"))
            for td in tr.findAll("td"):
                if count%perrow is 0:
                    try:
                        key = td.find("a").contents[0].lstrip()
                        if key in features:
                            pass
                        else:
                            features[key]=[]
                    except Exception as ieu:
                        print(ieu,"<<>>")
                elif count%perrow is 1:
                    try:
                        content=td.find("a").contents[0].lstrip()
                        print(key," --- ",content)
                        features[key].append(content)
                    except Exception as ie:
                        print(ie,"<<--encountered")
                count+=1
            print("------")
except Exception as oe:
    print(oe)
    
print(features)

