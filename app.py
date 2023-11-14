from flask import Flask,render_template,request
import requests

app=Flask(__name__)
#@app.route('/')
@app.route('/',methods=["POST","GET"])
def get_weatherdata():
    return render_template("index.html")

def get_weather_data():
    url= 'https://api.openweathermap.org/data/2.5/weather'
    #return render_template("index.html")

    param={'q':request.form.get("city"),
       'units':request.form.get("units"),
       'appid':request.form.get("appid")}

    response=requests.get(url,params=param)
    data=response.json()
    city=data['name']
    return f"data: {data} , city:{city}"

if __name__== "__main__":
    app.run(host="0.0.0.0",port=5004)