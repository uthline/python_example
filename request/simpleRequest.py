import requests
payload = {'key':'testkey', 'apply_type':'requests test'}

res = requests.post('http://httpbin.org/anything', data=payload)

print(res.text)

