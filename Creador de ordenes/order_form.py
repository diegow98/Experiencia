
import datetime
from datetime import date 
import tkinter as tk 
import logging
import pyautogui
import bs4
from tkinter import *

fields = 'Style', 'Cut', 'Neck Size', 'Sleeve Length', 'Color', 'Fabric'
        
first_name = pyautogui.prompt("Customer's First Name: ", "First Name")
last_name = pyautogui.prompt("Customer's Last Name: ", "Last Name")

today = date.today()
d4 = today.strftime("%m_%d_%y_")
log_file_name = d4 + last_name + "_" + first_name + ".log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
file_handler = logging.FileHandler(log_file_name)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


variables=[]


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        variables.append(text)
        logger.debug('%s: %s' % (field, text))


def makeform(root, fields):
    entries = []
    var=StringVar()
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=20, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

def close_window(): 
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.configure(background="Alice Blue")
    root.title("Customer Order") 
    ents = makeform(root, fields) 
    b1 = tk.Button(root, text='Submit', command=lambda:(fetch(ents), close_window()))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    

    root.mainloop()
    
    now = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    
    logger.debug("\nCustomer: " + first_name + " " + last_name )
    logger.debug("\nOrder submitted on " + str(now))



if (logger.hasHandlers()):
    logger.handlers.clear()

style= variables[0]
cut= variables[1]
neck_size= variables[2]
sleeve_lenght= variables[3]
color= variables[4]
fabric= variables[5]
print(style)
print(cut)
print(neck_size)
print(sleeve_lenght)
print(color)
print(fabric)





    