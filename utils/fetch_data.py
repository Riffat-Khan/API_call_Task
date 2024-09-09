import requests
# from main import retry

# @retry()
def fetching_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response.status_code