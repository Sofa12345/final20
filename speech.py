import requests
from config import *
from creds import get_creds  

FOLDER_ID, IAM_TOKEN = get_creds()


def speech_to_text(data):

    params = "&".join([
        "topic=general",  
        f"folderId={FOLDER_ID}",
        "lang=ru-RU"  
    ])

    headers = {
        'Authorization': f'Bearer {IAM_TOKEN}',
    }

    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data
    )

    decoded_data = response.json()

    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")  
    else:
        return False, "При запросе в SpeechKit возникла ошибка"
    
def text_to_speech(text):
    headers = {'Authorization': f"Bearer {IAM_TOKEN}"}
    data = {
        'text': text,
        'emotion': 'good',
        'lang': 'ru-RU',
        'voice': 'jane',
        'folderId': FOLDER_ID}
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit возникла ошибка"