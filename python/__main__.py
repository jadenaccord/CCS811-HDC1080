import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import numpy as np
import csv
import pandas

file_name = 'short-newFile.csv'

datetimes = []
temperatures = []
humidities = []
eCO2s = []
TVOCs = []

def show_all():
    fig = plt.figure()
    host = HostAxes(fig, [0.15, 0.1, 0.65, 0.8])
    par1 = ParasiteAxes(host, sharex=host)
    par2 = ParasiteAxes(host, sharex=host)
    host.parasites.append(par1)
    host.parasites.append(par2)

    host.set_ylabel("Temperature")
    host.set_xlabel("Datetime")
    host.axis["right"].set_visible(False)
    host.set_ylim(25, 35)

    par1.set_ylabel("eCO2")
    par1.axis["right"].set_visible(True)
    par1.axis["right"].major_ticklabels.set_visible(True)
    par1.axis["right"].label.set_visible(True)
    par1.set_ylim(400, 2000)

    par2.set_ylabel("TVOC")
    new_axisline = par2.get_grid_helper().new_fixed_axis
    par2.axis["right2"] = new_axisline(loc="right", axes=par2, offset=(60, 0))
    par2.set_ylim(0, 1000)

    fig.add_axes(host)

    p1, = host.plot(temperatures, label="Temperature")
    p2, = par1.plot(eCO2s, label="eCO2")
    p3, = par2.plot(TVOCs, label="TVOC")

    host.axis["left"].label.set_color(p1.get_color())
    par1.axis["right"].label.set_color(p2.get_color())
    par2.axis["right2"].label.set_color(p3.get_color())

    plt.show()

def show_correlation(_x, _y, _xlim, _ylim, _xlabel, _ylabel):
    x = _x
    y = _y
    plt.xlabel(_xlabel)
    plt.xlim(_xlim)
    plt.ylabel(_ylabel)
    plt.ylim(_ylim)

    coef = np.polyfit(x, y, 1)
    print('Correlation coefficient:')
    print(coef)
    poly1d_fn = np.poly1d(coef)
    plt.plot(x, y, 'ro', x, poly1d_fn(x), '--k', markersize=1)
    plt.show()

def load_data():
    with open(file_name,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            datetimes.append(pandas.to_datetime(row[0] + ' ' + row[1]))
            temperatures.append(float(row[2]))
            humidities.append(float(row[3]))
            eCO2s.append(float(row[4]))
            TVOCs.append(float(row[5]))

def user_prompt():
    print('Please select an option below:')
    print('1. All data')
    print('2. eCO2 vs TVOC')
    print('3. Temperature vs Humidity')
    print('4. Temperature vs eCO2')

    while True:
        print(' ')

        user_input = input()
        if user_input == '1':
            print('Plotting all...')
            show_all()
        elif user_input == '2':
            print('Plotting eCO2 vs TVOC...')
            show_correlation(eCO2s, TVOCs, (400, 2000), (0, 1000), 'eCO2 (ppm)', 'TVOC')
        elif user_input == '3':
            print('Plotting temperature vs humidity...')
            show_correlation(temperatures, humidities, (20, 35), (0, 100), 'Temperature (C)', 'Humidity (%)')
        elif user_input == '4':
            print('Plotting temperature vs eCO2...')
            show_correlation(temperatures, eCO2s, (20, 35), (400, 2000), 'Temperature (C)', 'eCO2 (ppm)')
        else:
            print('Selection not valid!')

if __name__ == "__main__":
    load_data()
    user_prompt()