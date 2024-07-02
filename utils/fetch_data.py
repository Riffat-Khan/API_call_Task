import requests
import time
from functools import wraps

def retry():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return func(*args, **kwargs)
                except:
                    time.sleep(2)
        return wrapper
    return decorator

@retry()
def fetching_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response.status_code