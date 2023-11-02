from datetime import datetime
import requests
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get('/api/users/list')
def get_user_list():
    offset = 20
    user_data = fetch_user_data(offset)

    user_list = [
        {
            "username": user['username'],
            "userId": user['userId'],
            "firstSeen": datetime.utcfromtimestamp(user['firstSeen']).strftime('%Y-%m-%d %H:%M:%S')
        }
        for user in user_data
    ]

    return user_list

def fetch_user_data(offset):
    url = f'https://sef.podkolzin.consulting/api/users/lastSeen?offset={offset}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        return []

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
