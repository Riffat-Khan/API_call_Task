import logging
from argparser.argparser import ArgumentParser
from utils.record_difference import record_difference   
from pdf.write_to_pdf import create_pdf 
from pdf.graph_pdf import graph_plot
        
def main(days):
    logging.basicConfig(level=logging.INFO)
    
    content = record_difference(days)
    logging.info(content)
    
    create_pdf(content, 'record.pdf')
    print(graph_plot(content, 'graphs.pdf'))
    
    
if __name__ == '__main__':
    parser = ArgumentParser()
    args = parser.parse_args()
    days = args.days
    main(days)
    