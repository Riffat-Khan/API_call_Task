import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
import datetime
from utils.enum_keys import Currency

def graph_plot(data, filename):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    c.drawString(250, 750, 'CURRENCY HISTORY')
    x_range = [currency.value for currency in Currency]
    
    for index, record in enumerate(data):
        c.drawString(230, 710, f"Currency Record - {record['date']}")
        
        rates_plot = [value for key, value in record['usd'].items()]
        plt.plot(x_range, rates_plot)
        plt.xlabel('Currency')
        plt.ylabel('Rate')
        plt.title(f"Currency Rate => {record['date']}")
        plt.tight_layout()
        plt.savefig(f'rates_plot{index}.png')
        plt.close()
        
        c.drawImage(f'rates_plot{index}.png', 10, 450, width=280, height=250)
        
        if 'diff' in record:
            rate_difference = [value for key, value in record['diff'].items()] 
            plt.plot(x_range, rate_difference)
            plt.xlabel('Currency')
            plt.ylabel('Rate difference')
            plt.title(f"Currency Rate Difference => {record['date']}")
            plt.tight_layout()
            plt.savefig(f'rate_diff_plot{index}.png')
            plt.close()       
            
            c.drawImage(f'rate_diff_plot{index}.png', 300, 450, width=280, height=250)
        
        c.drawString(200, 400, f"Currency Record - {record['date']}")

        c.drawString(50, 380, "'USD[Rate]':")
        y_position = 360
        for currency, value in record['usd'].items():
            if y_position < 20:
                c.showPage()
                y_position = 360
            c.drawString(70, y_position, f"'{currency}': {value}")
            y_position -= 20

        if 'diff' in record:
            c.drawString(350, 380, "Rate Diff:")
            y_position = 360
            for currency, diff in record['diff'].items():
                if y_position < 20:
                    c.showPage()
                    y_position = 360
                c.drawString(370, y_position, f"'{currency}': {diff}")
                y_position -= 20
        c.showPage()
        
    c.save()
    buffer.seek(0)
    
    with open(filename, 'wb') as f:
        f.write(buffer.read())
        
    # for i in range(len(data_array)):
        
    #     y_range = data_array[i]
        
    #     plt.plot(x_range, y_range)

    #     plt.xlabel('rate')
    #     plt.ylabel('date')
        
    #     # plt.title(f'{keys[i]} currency rate')
    
    #     plt.show()
        
        
    # data_values = []
    # for count in range(15):
    #     data_array = []
    #     for i in range(len(data)-1):
    #         record = data[i][2]
    #         values_plot = [[key, value] for key, value in record['diff'].items()]
    #         data_array.append((values_plot[count][1]))
    #     data_values.append(data_array)
        
    # y_range = []
    # for i in range(99):
    #     date = datetime.date.today() - datetime.timedelta(i)
    #     date_format = date.strftime('%Y-%m-%d')
    #     y_range.append(date_format)
    
        
    # for i in range(len(data_values)):
        
    #     x_range = data_values[i]
        
    #     plt.plot(x_range, y_range)

    #     plt.xlabel('rate')
    #     plt.ylabel('date')
        
    #     keys = ['alex', 'aoa', 'blur', 'ant', 'core', 'imp' , 'joe', 'kgs', 'mad', 'magic', 'nexo', 'ocean', 'pkr', 'poly', 'comp']
    #     plt.title(f'{keys[i]} currency rate')
    
    #     plt.show()