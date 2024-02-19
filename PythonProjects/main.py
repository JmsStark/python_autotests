import requests

HOST='https://api.pokemonbattle.me'

"""response = requests.post(url=f'{HOST}/pokemons', 
         json={
              "name": "generate",
              "photo": "generate"
              },
headers={'Content-Type': 'application/json', 'trainer_token': '330ccf91c608f02985a94ef7659131e3'}, timeout=5)
print(response)"""

"""response = requests.put(url=f'{HOST}/pokemons',
        json={
              "pokemon_id": 1493,
              "name": "Бульба",
              "photo": "https://dolnikov.ru/pokemons/albums/008.png"
              },
headers={'Content-Type': 'application/json', 'trainer_token': '330ccf91c608f02985a94ef7659131e3'}, timeout=5)"""

response = requests.post(url=f'{HOST}/trainers/add_pokeball',
        json={
             "pokemon_id": "1493"
             },
headers={'Content-Type': 'application/json', 'trainer_token': '330ccf91c608f02985a94ef7659131e3'}, timeout=5)
print(response)