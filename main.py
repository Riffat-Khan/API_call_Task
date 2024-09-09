import logging
import time
from functools import wraps
from argparser.argparser import ArgumentParser
from utils.record_difference import record_difference
from pdf.data_graph_pdf import graph_plot

def retry(retry=5, sleep=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts <= retry:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    attempts += 1
                    if attempts > retry:
                        raise err
                    time.sleep(sleep)
        return wrapper
    return decorator

logging.basicConfig(level=logging.INFO)
        
def main(days):    
    content = record_difference(days)
    logging.info(content)
    print(graph_plot(content, 'graphs.pdf'))
    
    
if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_args()
    days = args.days
    main(days)
    