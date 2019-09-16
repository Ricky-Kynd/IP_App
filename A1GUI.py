import tkinter as tk
from tkinter import ttk
from A1 import A1
from Histogram import Histogram
from Table import Table
import sys

def redirector(inputStr):
	textbox.insert(tk.END, inputStr)

def load_file():
	pass #modify this - display all statistics info

def click():
	pass #modify this
	if comboData.current() == 0:
		# get sum
		my_unit = 100
	elif  comboData.current() == 1: 
		# get freq
		my_unit = 1
	else: 
		#get average
		my_unit = 10
	if comboOutput.current() == 0:
		#create table
		pass
	elif comboOutput.current() == 1:
		#create histogram (horizontal)
		pass
	else:
		#create histogram (vertical)
		pass
		
app = tk.Tk() 
app.title("COMPSCI130 A1")
app.geometry('900x500')

label1 = tk.Label(app, text = "File:")
label1.grid(column=0, row=0)

entry_file = tk.Entry(app)
entry_file.grid(column=1, row=0)
entry_file.insert(tk.END, 'trace40.txt')

load_file_button = ttk.Button(app, text="Load", command=load_file) 
load_file_button.grid(column=2, row=0)

entry_ip = tk.Entry(app)
entry_ip.grid(column=3, row=0)
entry_ip.insert(tk.END, '192.168.0.24')

label2 = tk.Label(app, text = "Choose type:")
label2.grid(column=4, row=0)

comboData = ttk.Combobox(app,  values=["Sum","Freq", "Average"])
comboData.grid(column=5, row=0)
comboData.current(0)

label3 = tk.Label(app, text = "Choose output:")
label3.grid(column=6, row=0)

comboOutput = ttk.Combobox(app,  values=["Table", "H Histogram", "V Histogram"])
comboOutput.grid(column=7, row=0)
comboOutput.current(1)

action = ttk.Button(app, text="Run", command=click)  
action.grid(column=8,row=0) 

textbox = tk.Text(app)
textbox.grid(column=0, row=1, columnspan=9,padx=2, pady=2)

sys.stdout.write = redirector
app.mainloop()

