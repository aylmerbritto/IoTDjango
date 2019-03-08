import re

wholeMessage="<WSGIRequest: GET '/realTime/dataPost/?humidity:123,temperature:433,pressure:9800,'>"
attribute=['humidity','temperature','pressure']
upData=[]
for i in range(len(attribute)):
    name=str(re.findall(attribute[i]+":([a-zA-Z0-9]*)," ,wholeMessage))
    name=name.rstrip("']")
    name=name.lstrip("['")
    name=float(name)
    upData.append(name)
print(upData)
