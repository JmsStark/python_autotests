import requests
import pytest

HOST='https://api.pokemonbattle.me'

def test_status_code():
    response=requests.get(url=f'{HOST}/trainers', params={'trainer_id': 172}, timeout=5)
    assert response.status_code == 200
    assert response.json()['trainer_name'] == 'JmsStark'