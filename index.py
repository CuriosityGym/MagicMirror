from flask import Response, Flask, request, current_app as app
import requests
import json
import re
import os
import urllib

errorText="Error In Parsing"
gCityID="1275339"
gAppID="15373f8c0b06b6e66e6372db065c4e46"
filename='temp.json'

app = Flask(__name__,  static_url_path='/static')


#print($apiResponse);

@app.route("/")
def indexPage():       	
        return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)




	

@app.route("/humidity")
def getHumidity():       
        
        requestURL="http://api.openweathermap.org/data/2.5/weather?id="+gCityID+"&appid="+gAppID        

       
        try:        
                response = download_file(requestURL, filename)
                return getData("main.humidity")
        except:
                return errorText
    
@app.route("/temperature")
def getTemperature():        

        requestURL="http://api.openweathermap.org/data/2.5/weather?id="+gCityID+"&appid="+gAppID        

       
        try:        
                response = download_file(requestURL, filename)
                temperatureK=getData("main.temp")                
                temperatureC=int(round(float(temperatureK)-273.15,0))
                
                return str(temperatureC)
                
        except:
                return errorText

@app.route("/weatherDescription")
def getWeatherDescription():
                
        requestURL="http://api.openweathermap.org/data/2.5/weather?id="+gCityID+"&appid="+gAppID        

       
        try:        
                response = download_file(requestURL, filename)
                return getData("weather.main")
        except:
                return errorText
				
@app.route("/forecast")
def getForecast():
        requestURL="http://api.openweathermap.org/data/2.5/forecast/daily?id="+gCityID+"&appid="+gAppID
        #try:
        #response = download_file(requestURL, filename)
        #return getData("")
        #except:
        #       return errorText

        r = requests.get(requestURL, stream=True)
        return r.content			
    

def getData(jsontree):    
    with open(filename) as data_file:    
        data = json.load(data_file)
    splittree=jsontree.split(".")    
    lastLeafIndex = len(splittree) - 1
    #jsontree="main.temp"
    
    for i, leaf in enumerate(splittree):
        if i == lastLeafIndex:
            continue
        else:
           leafDataIndex=0
           result =  re.findall(r'\[([^]]*)\]', leaf)
           if result:
              leafDataIndex=result[0]
              leaf=leaf.replace("["+leafDataIndex+"]","")
              leafDataIndex=int(leafDataIndex)
        
        try:        
            data=data[leaf][leafDataIndex]
        except(KeyError):
           try: 
               data=data[leaf]
           except (KeyError):
               return "Error"
               exit()

    leaf=splittree[lastLeafIndex]
    leafDataIndex=0
    result =  re.findall(r'\[([^]]*)\]', leaf)
    if result:
        leafDataIndex=result[0]
        leaf=leaf.replace("["+leafDataIndex+"]","")
        leafDataIndex=int(leafDataIndex)
        return (data[leaf][leafDataIndex])
    else:
       return str(data[leaf])  

        
def getDataList(jsontree):    
    with open(filename) as data_file:    
        data = json.load(data_file)
    return data
        

        

        

  
def download_file(url,filename):
    local_filename = filename
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)                
    return True

	   

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
