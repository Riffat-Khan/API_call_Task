from utils.fetch_data import fetching_data
from utils.enum_keys import Currency

def parse_15_records(url): 
    data = fetching_data(url)
    currency = [currency.value for currency in Currency]
    deleting_unnecessary_record = [key for key in data['usd'].keys() if key not in currency]
    for key in deleting_unnecessary_record:
        del data['usd'][key]
        
    return data
