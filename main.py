import requests
import datetime
import json
from argparser.argparser import ArgumentParser
from utils.fetch import fetch_data
from utils.enum_keys import Currency
from utils.parse_records import parse_15_records

from pdf.write_to_pdf import create_pdf
from pdf.graph_pdf import graph_plot

    
def records_15(url): 
    data = fetch_data(url)
    fifteen_records = {}
    fifteen_records['date'] = data['date']
    currency_record = data['usd']
    currency = ['alex', 'aoa', 'blur', 'ant', 'core', 'imp' , 'joe', 'kgs', 'mad', 'magic', 'nexo', 'ocean', 'pkr', 'poly', 'comp']
    currency_fifteen = {key : currency_record[key] for key in currency if key in currency_record} 
    fifteen_records['usd'] = currency_fifteen
    return fifteen_records

    
def history_record(data, Currency, days):    
    all_records = []
    for day in range(days):
        date = datetime.date.today() - datetime.timedelta(day)
        date_format = date.strftime('%Y-%m-%d')
        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date_format}/v1/currencies/usd.json'
        res = parse_15_records(Currency)
        resultant_array = [{key : value} for key, value in res.items()]
        if resultant_array:
            all_records.append(resultant_array)
    return all_records

def record_difference(days):
    records = history_record(days)
    for i in range(len(records)-1):
        prev_record = records[i][1]
        prev_currency = prev_record['usd']
        next_record = records[i+1][1]
        next_currency = next_record['usd']
        rate_diff = {}
        dict_rate_diff = {}
        keys = ['alex', 'aoa', 'blur', 'ant', 'core', 'imp' , 'joe', 'kgs', 'mad', 'magic', 'nexo', 'ocean', 'pkr', 'poly', 'comp']
        for key in keys:
            difference = next_currency[key] - prev_currency[key]
            rate_diff[key] = difference
        dict_rate_diff['diff'] = rate_diff    
        records[i].append(dict_rate_diff)
    
    return records
        
        
def main():
    parser = ArgumentParser()
    args = parser.parse_args()
    days = args.days
    
    url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json' 
    data = fetch_data(url)   
    content = parse_15_records(data, Currency)
    print(content)
    # print('\nlatest record', json.dumps(content[0]))
    
    # print(graph_plot(content))
    
    # create_pdf(content, 'record_currency.pdf')

    
if __name__ == '__main__':
    main()
    