import datetime
from utils.parse_records import parse_15_records

def history_record(days):    
    all_records = []
    for day in range(days):
        date = datetime.date.today() - datetime.timedelta(day)
        date_format = date.strftime('%Y-%m-%d')
        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date_format}/v1/currencies/usd.json'
        parsed_data = parse_15_records(url)
        if parsed_data:
            all_records.append(parsed_data)
    return all_records