import requests

response = requests.get('https://lobby.ikariam.gameforge.com/pt_BR/')

print('Status code:', response.status_code)
print('↓↓ Header ↓↓')
print(response.headers)

print('\n↓↓ Content ↓↓')
print(response.content)