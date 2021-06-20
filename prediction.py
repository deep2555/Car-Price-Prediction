import json
import requests
from werkzeug.datastructures import Headers
from werkzeug.wrappers import response

# user input
name = [input("enter your name: ")]
year = [int(input("enter the year: "))]
km_driven = [int(input("enter the kilometer driven: "))]
fuel = [input("enter the fuel: ")]
seller_type = [input("enter the seller_type: ")]
transmission = [input("enter the transmission: ")]
owner = [input("enter the owner: ")]
engine = [int(input("enter thr engine cc: "))]
seat = [int(input("enter the seat: "))]





url = "http://127.0.0.1:5000/"
data = {
    "name":name, "year":year, "km_driven":km_driven, "fuel":fuel ,"seller_type":seller_type,"transmission":transmission, "owner":owner ,"engine":engine, "seats":seat
}

JSON_data = json.dumps(data)
headers = {"Content-type": "application/json"}
response = requests.post(url = url , data=JSON_data, headers=headers)
print(response)
output = json.loads(response.text)
print(output)
prediction = output["prediction"]
print("according to your specification your car price will be : " ,prediction)