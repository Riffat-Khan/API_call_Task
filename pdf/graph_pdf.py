import matplotlib.pyplot as plt

def graph_plot(data):
    data_values = []
    for count in range(16):
        data_array = []
        for i in range(len(data)-1):
            record = data[i][count]
            values_plot = [[key, value] for key, value in record.items()]
            data_array.append((values_plot[0][1]))
            
        data_values.append(data_array)
        
    for i in range(len(data_values)):
        y_range = [y for y in range(len(data_values[i]))]

        plt.plot(data_values[i], y_range)

        plt.xlabel('date')
        plt.ylabel('rate')
        plt.title('currency rate change')
    
        plt.show()