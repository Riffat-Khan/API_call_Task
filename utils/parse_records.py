def parse_15_records(data, currencies): 
    currency = [currency.value for currency in currencies]
    deleting_unnecessary_record = [key for key in data['usd'].keys() if key not in currency]
    for key in deleting_unnecessary_record:
        del data['usd'][key]
        
    return data
