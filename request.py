import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'current_body_temp':100, 'fever_days':8, 'cough_days':9, 'travel_history':1, 'age':40, 'medical_ailment':0})

print(r.json())