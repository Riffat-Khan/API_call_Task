import matplotlib.pyplot as plt
import datetime

def graph_plot(data):
    data_values = []
    for count in range(15):
        data_array = []
        for i in range(len(data)-1):
            record = data[i][2]
            values_plot = [[key, value] for key, value in record['diff'].items()]
            data_array.append((values_plot[count][1]))
        data_values.append(data_array)
        
    y_range = []
    for i in range(99):
        date = datetime.date.today() - datetime.timedelta(i)
        date_format = date.strftime('%Y-%m-%d')
        y_range.append(date_format)
    
        
    for i in range(len(data_values)):
        
        x_range = data_values[i]
        
        plt.plot(x_range, y_range)

        plt.xlabel('date')
        plt.ylabel('rate')
        
        keys = ['alex', 'aoa', 'blur', 'ant', 'core', 'imp' , 'joe', 'kgs', 'mad', 'magic', 'nexo', 'ocean', 'pkr', 'poly', 'comp']
        plt.title(keys[i] , 'currency rate change')
    
        plt.show()