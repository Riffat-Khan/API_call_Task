import requests
import datetime
from argparser.argparser import ArgumentParser
from pdf.write_to_pdf import writing_to_pdf

def fetch_data(url, base_currency):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        records = data[base_currency]
        fifteen_records = {currency : records[currency] for currency in list(records)[:71:5]} 
        return fifteen_records
    else:
        return response.status_code
    
def history_record(base_currency, days):    
    all_records = []
    for day in range(days+1):
        date = datetime.date.today() - datetime.timedelta(day)
        date_format = date.strftime('%Y-%m-%d')
        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date_format}/v1/currencies/{base_currency}.json'
        res = fetch_data(url, base_currency)
        resultant_array = [{key : value} for key, value in res.items()]
        if resultant_array:
            all_records.append(resultant_array)
    return all_records

def record_difference(base_currency, days):
    records = history_record(base_currency, days)
    difference_record = []
    for i in range(len(records)-2):
        prev_record = records[i]
        next_record = records[i+1]
        for prev, next in zip(prev_record, next_record):
            key = list(prev.keys())[0]
            difference = next[key] - prev[key]
            prev['diff'] = difference
        difference_record.append(prev_record)
    return difference_record
        

def main():
    parser = ArgumentParser()
    args = parser.parse_args()

    base_currency = args.currency
    days = args.days
    
    content = record_difference(base_currency, days)
    print(content)
    latest = history_record(base_currency, days=0)
    print('latest record', latest)
    
    writing_to_pdf(content)

    
    
if __name__ == '__main__':
    main()