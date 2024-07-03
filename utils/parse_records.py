from utils.fetch_data import fetching_data
from utils.enum_keys import Currency

def parse_15_records(url): 
    data = fetching_data(url)
    currency = [currency.value for currency in Currency]
    unnecessary_record = list(filter(lambda key: key not in currency, data['usd'].keys()))
    for key in unnecessary_record:
        del data['usd'][key]
        
    return data
