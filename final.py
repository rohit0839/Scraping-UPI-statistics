import requests
import tkinter as tk
from bs4 import BeautifulSoup
from collections import OrderedDict
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

root = tk.Tk()
root.title('''Top 'n' Apps in UPI Ecosystem''')
root.geometry('880x700')
root.resizable(False, False)

page = requests.get('https://www.npci.org.in/what-we-do/upi/upi-ecosystem-statistics')
soup = BeautifulSoup(page.content, 'html.parser')

def quit():
    root.quit()
    root.destroy()

def plot():
    month_data = month_entry.get()
    year_data = year_entry.get()
    num_data = int(num_entry.get())
    
    d = {}
    div_id = 'innerTabTwo' + month_data + year_data
    upi_table1 = soup.find('div', id=div_id)
    for apps in upi_table1.find_all('tbody'):
        rows = apps.find_all('tr')
        for row in rows:
            name = row.find_all('td')[1].text.strip()
            total = row.find_all('td')[11].text.strip()
            total = total.replace(',', '')
            try:
                total = float(total)
            except ValueError:
                continue
            d[name] = total
    
    d1 = OrderedDict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    first_n_app = dict(zip(list(d1.keys())[:num_data], list(d1.values())[:num_data]))
    print(first_n_app)
    myList = first_n_app.items()
    x, y = zip(*myList)
    figure = Figure(figsize=(8, 5), dpi=100)
    figure_canvas = FigureCanvasTkAgg(figure, master=root)
    figure_canvas.draw()
    plot_fig = figure.add_subplot()
    plot_fig.plot(x, y, marker='.', markersize=10)
    plot_fig.tick_params(axis='x', labelrotation=10)
    plot_fig.set_ylabel('Total Transactions Value (Cr)')
    figure_canvas.get_tk_widget().grid(row = 6, columnspan=2, sticky='nsew')

    toolbarFrame = tk.Frame(master=root)
    toolbarFrame.grid(row=10,column=0)
    toolbar = NavigationToolbar2Tk(figure_canvas, toolbarFrame)
    return None

month = tk.Label(root, text='Month (eg.Jan):').grid(row=0, column=0, padx=5, pady=5)
month_entry = tk.Entry(root, width=8)
month_entry.grid(row=0, column=1)

year = tk.Label(root, text='Year (eg.22):').grid(row=1, column=0, padx=5, pady=5)
year_entry = tk.Entry(root, width=8)
year_entry.grid(row=1, column=1)

num = tk.Label(root, text='No of UPI Apps:').grid(row=2, column=0, padx=5, pady=5)
num_entry = tk.Entry(root, width=8)
num_entry.grid(row=2, column=1)

button1 = tk.Button(root, text="plot", command=plot)
button1.grid(row=3, column=0)

button2 = tk.Button(root, text="quit", command=quit)
button2.grid(row=3, column=1)

source = tk.Label(text="Source: NPCI (https://www.npci.org.in/) ", font="monospace 14 italic")
source.grid(row=8, column=1)

root.mainloop()
