from time import sleep
import requests
from os import getenv

def simple_task(task_arg):
    token=getenv('tg_secret')
    chat_id= getenv('chat_id')
    text=task_arg
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
    "chat_id": chat_id,
    "text": text,
        'parse_mode':'Markdown'
    }
    resp = requests.get(url, params=params)
    sleep(60)
    return "prefix___"+task_arg