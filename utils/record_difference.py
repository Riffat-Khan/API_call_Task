from utils.history_record import history_record
from utils.enum_keys import Currency

def record_difference(days):
    records = history_record(days)
    currency = [currency.value for currency in Currency]
    for i in range(0, len(records)-1):
        prev_record = records[i]['usd']
        next_record = records[i+1]['usd']
        rate_diff = {value: round((next_record[value] - prev_record[value]), 5) for value in currency} 
        records[i]['diff'] = rate_diff
    
    return records