import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'income':2, 'age':9, 'rooms':6,'bedrooms':5,'population':40000})
#Avg area income 60000
# Avg area house
# age 5
#Rooms 8
#Vedrooms 5
#Area population 40000
# model.predict([[60000,5,9,100,40000]])

print(r.json())