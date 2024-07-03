import os
import shutil
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from io import BytesIO
from utils.enum_keys import Currency


def graph_plot(data, filename):
    buffer = BytesIO()
    folder_path = 'plots'
    os.makedirs(folder_path, exist_ok=True) 
    c = canvas.Canvas(buffer, pagesize=letter)  
    c.drawString(250, 750, 'CURRENCY HISTORY')  
    title = Currency.values()
    x_range = []
    date_range = []
    for i in range(0, len(data), 10):
        date_range.append(data[i]['date'])
        x_range.append(i)
            
    for i in range(15):
        rates_array = []
        diff_array = []
        for j in range(0, len(data), 10):
            rates_plot = [value for key, value in data[j]['usd'].items()]
            rates_array.append(rates_plot[i])
            if 'diff' in data[j]:
                rate_difference = [value for key, value in data[j]['diff'].items()]
                diff_array.append(rate_difference[i])
    
        plt.plot(x_range, rates_array)
        plt.xlabel('Days')
        plt.ylabel('Rate')
        plt.title(f"Currency Rate = {title[i]}")
        plt.tight_layout()
        plt.savefig(os.path.join(folder_path,f'rates_plot{i}.png'))
        plt.close()
        c.drawString(250, 720, f'{title[i]} currency record')  
        c.drawImage(os.path.join(folder_path,f'rates_plot{i}.png'), 10, 450, width=280, height=250)
        
        plt.plot(x_range, diff_array)
        plt.xlabel('Days')
        plt.ylabel('Difference')
        plt.title(f"Currency Rate Difference = {title[i]}")
        plt.tight_layout()
        plt.savefig(os.path.join(folder_path, f'diff_plot{i}.png'))
        plt.close()
        c.drawImage(os.path.join(folder_path, f'diff_plot{i}.png'), 300, 450, width=280, height=250)
        mydata = [[value_1, value_2, value_3] for value_1, value_2, value_3 in zip(date_range, rates_array, diff_array)]
        cols = ["Date", "Rate", "Difference"]

        plt.figure(figsize=(8, 4))
        the_table = plt.table(cellText=mydata,
                            colLabels=cols,
                            loc='center')
        the_table.auto_set_font_size(False)
        the_table.set_fontsize(12)
        the_table.scale(1, 2)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(os.path.join(folder_path,f'rate_table{i}.png'))
        plt.close()
        c.drawImage(os.path.join(folder_path,f'rate_table{i}.png'), 150, 170, width=300, height=250)
        c.showPage()
        
    c.save()
    buffer.seek(0)
    
    shutil.rmtree(folder_path)

    with open(filename, 'wb') as f:
        f.write(buffer.read())
