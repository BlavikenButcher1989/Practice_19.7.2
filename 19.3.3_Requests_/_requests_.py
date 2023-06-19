import json,requests

# --------------------------------------------------------

"""GET"""
status = 'available'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())

# ---------------------------------------------------------
"""POST"""
body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Rick"
  },
  "name": "Ben",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Jack"
    }
  ],
  "status": "available"
}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res2 = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(body))
print(res2.status_code)
print(res2.text)
print(res2.json())

# ----------------------------------------------------------

"""PUT"""
body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "Rocky"
  },
  "name": "Bobby",
  "photoUrls": [
    "https://w.wallhaven.cc/full/0p/wallhaven-0pwxdp.jpg"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Johnny"
    }
  ],
  "status": "available"
}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res3 = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(body))
print(res3.status_code)
print(res3.text)
print(res3.json())

# ---------------------------------------------------------

"""DELETE"""
pet_id = [str(i[1]) for i in res3.json().items()]
headers = {'accept': 'application/json'}
res4 = requests.delete(f'https://petstore.swagger.io/v2/pet/{pet_id[0]}', headers=headers)
print(res4.status_code)
print(res4.text)
print(res4.json())

# ---------------------------------------------------------