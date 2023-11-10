from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter 
import random
import pymysql
import csv
from datetime import datetime 
import numpy as np


gui = tkinter.Tk()
gui.title("Stock Management System")
gui.geometry("750x750")
my_tree = ttk.Treeview(gui,show='headings', height=20)
style = ttk.Style()

placeholderArray = ['','','','','','']
numeric='1234567890'
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


#Connection to mysql database
def connection():
    conn = pymysql.connect(host = 'localhost',user = 'root',password ='Shrikanth_1', db='stockmanagementsystem')
    return conn

conn = connection()
cursor = conn.cursor()

for i in range(0,5):
    placeholderArray[i]=tkinter.StringVar()

# Read the data from table stocks
def read():
    cursor.connection.ping()
    sql=f"SELECT 'item_id', 'name', 'price', 'quantity', 'category', 'date' FROM stocks ORDER BY 'id' DESC"
    cursor.execute(sql)
    results=cursor.fetchall()
    conn.commit()
    conn.close()
    return results

# dummydata =[
#     ['123', '1345', '4567', '1234', '9877', '2345'],
#     ['12', '1345', '4567', '1234', '9877', '2345'],
#     ['143', '1345', '4567', '1234', '9877', '2345'],
#     ['153', '1345', '4567', '1234', '9877', '2345'],
#     ['163', '1345', '4567', '1234', '9877', '2345'],
#     ['183', '1345', '4567', '1234', '9877', '2345'],
# ]

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
    for array in read():
        my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag="orow")
    my_tree.tag_configure('orow',background="#02577A")
    my_tree.pack()

# Generate Random Number 
def setph(word,num):
    for ph in range(0,5):
        if ph == num:
            placeholderArray[ph].set(word)

def generateRand():
    itemId=''
    for i in range(0,3):
        randno=random.randrange(0,(len(numeric)-1))
        itemId=itemId+str(numeric[randno])
    randno=random.randrange(0,(len(alpha)-1))
    itemId=itemId+'-'+str(alpha[randno])
    print("generated: "+itemId)
    setph(itemId,0)

# Save an entry
def save():
    itemId=str(itemIDEntry.get())
    name=str(nameEntry.get())
    price=str(priceEntry.get())
    qnt=str(qntEntry.get())
    cat=str(categoryEntry.get())
    valid=True
    if not(itemId and itemId.strip()) or not(name and name.strip()) or not(price and price.strip()) or not(qnt and qnt.strip()) or not(cat and cat.strip()):
        messagebox.showwarning("","Please fill up all entries")
        return
    if len(itemId) < 5:
        messagebox.showwarning("","Invalid Item Id")
        return
    if(not(itemId[3]=='-')):
        valid=False
    for i in range(0,3):
        if(not(itemId[i] in numeric)):
            valid=False
            break
    if(not(itemId[4] in alpha)):
        valid=False
    if not(valid):
        messagebox.showwarning("","Invalid Item Id")
        return
    
    try:
        cursor.connection.ping()
        sql=f"SELECT * FROM stocks WHERE `item_id` = '{itemId}' "
        cursor.execute(sql)
        checkItemNo=cursor.fetchall()
        if len(checkItemNo) > 0:
            messagebox.showwarning("","Item Id already used")
            return
        else:
            cursor.connection.ping()
            sql=f"INSERT INTO stocks (`item_id`, `name`, `price`, `quantity`, `category`) VALUES ('{itemId}','{name}','{price}','{qnt}','{cat}')"
            cursor.execute(sql)
        conn.commit()
        conn.close()
        for num in range(0,5):
            setph('',(num))
    except:
        messagebox.showwarning("","Error while saving")
        return
    refreshTable()



#Frame
frame = tkinter.Frame(gui, bg='#02577A')
frame.pack()

btnColor = "#196E78"

#Manage Frame & buttons & position/grid
manageFrame = tkinter.LabelFrame(frame, text ='Manage', borderwidth=5)
manageFrame.grid(row=0, column=0, sticky='w', padx=[10,150], pady=20, ipadx=[6])

saveBtn = Button(manageFrame, text='SAVE', width=5, borderwidth=3, bg=btnColor, fg='blue', command = save)
updateBtn = Button(manageFrame, text='UPDATE', width=5, borderwidth=3, bg=btnColor, fg='blue')
deleteBtn = Button(manageFrame, text='DELETE', width=5, borderwidth=3, bg=btnColor, fg='blue')
selectBtn = Button(manageFrame, text='SELECT', width=5, borderwidth=3, bg=btnColor, fg='blue')
findBtn = Button(manageFrame, text='FIND', width=5, borderwidth=3, bg=btnColor, fg='blue')
clearBtn = Button(manageFrame, text='CLEAR', width=5, borderwidth=3, bg=btnColor, fg='blue')
exportBtn = Button(manageFrame, text='EXPORT', width=5, borderwidth=3, bg=btnColor, fg='blue')

saveBtn.grid(row=0, column=0, padx=5, pady=5)
updateBtn.grid(row=0, column=1, padx=5, pady=5)
deleteBtn.grid(row=0, column=2, padx=5, pady=5)
selectBtn.grid(row=0, column=3, padx=5, pady=5)
findBtn.grid(row=0, column=4, padx=5, pady=5)
clearBtn.grid(row=0, column=5, padx=5, pady=5)
exportBtn.grid(row=0, column=6, padx=5, pady=5)

#Entries Frame 

entriesFrame = tkinter.LabelFrame(frame, text ='Entries Form', borderwidth=5)
entriesFrame.grid(row=1, column=0, sticky='w', padx=[10,150], pady=[0,20], ipadx=[6])

itemIDLabel = Label(entriesFrame, text="ITEM ID", anchor='e', width=10)
nameLabel = Label(entriesFrame, text="NAME", anchor='e', width=10)
priceLabel = Label(entriesFrame, text="PRICE", anchor='e', width=10)
qntLabel = Label(entriesFrame, text="QNT", anchor='e', width=10)
categoryLabel = Label(entriesFrame, text="CATEGORY", anchor='e', width=10)

itemIDLabel.grid(row=0, column=0, padx=10)
nameLabel.grid(row=1, column=0, padx=10)
priceLabel.grid(row=2, column=0, padx=10)
qntLabel.grid(row=3, column=0, padx=10)
categoryLabel.grid(row=4, column=0, padx=10)

# categoryArray = ['Networking Tools', 'Computer Parts', 'Repair Tools', 'Gadgets']

itemIDEntry = Entry(entriesFrame,width= 50, textvariable=placeholderArray[0])
nameEntry = Entry(entriesFrame,width= 50, textvariable=placeholderArray[1])
priceEntry = Entry(entriesFrame,width= 50, textvariable=placeholderArray[2])
qntEntry = Entry(entriesFrame, width= 50, textvariable=placeholderArray[3])
categoryEntry = Entry(entriesFrame, width=50, textvariable=placeholderArray[4])
# categoryCombo = ttk.Combobox(entriesFrame,width= 47, textvariable=placeholderArray[4], values=categoryArray)


itemIDEntry.grid(row=0, column=2, padx=5, pady=5)
nameEntry.grid(row=1, column=2, padx=5, pady=5)
priceEntry.grid(row=2, column=2, padx=5, pady=5)
qntEntry.grid(row=3, column=2, padx=5, pady=5)
categoryEntry.grid(row=4,column=2, padx=5, pady=5)
# categoryCombo.grid(row=4, column=2, padx=5, pady=5)

#Generating Button for Random generator 
generateIdBtn = Button(entriesFrame, text="GENERATE ID", borderwidth=3, bg = btnColor, fg = "blue", command=generateRand)
generateIdBtn.grid(row=0, column=3, padx=5, pady=5)


#creating a columns and headings for the entries 
style.configure(gui)
my_tree['columns']=("Item Id","Name","Price","Quantity","Category","Date")
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Item Id",anchor=W,width=70)
my_tree.column("Name",anchor=W,width=125)
my_tree.column("Price",anchor=W,width=125)
my_tree.column("Quantity",anchor=W,width=100)
my_tree.column("Category",anchor=W,width=150)
my_tree.column("Date",anchor=W,width=150)

my_tree.heading("Item Id",text="Item Id",anchor=W)
my_tree.heading("Name",text="Name",anchor=W)
my_tree.heading("Price",text="Price",anchor=W)
my_tree.heading("Quantity",text="Quantity",anchor=W)
my_tree.heading("Category",text="Category",anchor=W)
my_tree.heading("Date",text="Date",anchor=W)
my_tree.tag_configure('orow',background="#EEEEEE")
my_tree.pack()

refreshTable()

gui.resizable(False, False)
gui.mainloop()

