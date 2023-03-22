#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk

root  = Tk()

root.title("Khong Quynh Huong's Restaurant")
root.geometry("800x580")
# Menu images
displayDefaultImageObject = Image.open(r"C:\Users\Dell\Downloads\pho-bo-rat-giau-dinh-duong.jpg")
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)





# Section Frames
mainFrame = ttk.Frame(root, style='MainFrame.TFrame', width=800, height=580)
mainFrame.pack(fill=BOTH, expand=True)

topFrame = ttk.Frame(mainFrame)
topFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 2)

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame")
displayFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")
orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame")
orderFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")
# Dish Frames
phoboFrame = ttk.Frame(topFrame, style = "DishFrame.TFrame")
phoboFrame.grid(row = 0, column = 0, sticky = "NSEW")

bundauFrame = ttk.Frame(topFrame,style ="DishFrame.TFrame")
bundauFrame.grid(row = 0, column = 1, sticky ="NSEW")

buncaFrame = ttk.Frame(topFrame, style ="DishFrame.TFrame")
buncaFrame.grid(row = 0, column = 2, sticky ="NSEW")

phogaFrame = ttk.Frame(topFrame, style ="DishFrame.TFrame")
phogaFrame.grid(row = 0, column = 3, sticky ="NSEW")



#region Menu Section

phoboLabel = ttk.Label(phoboFrame, text ="Phobo...30000VNĐ", style ="MenuLabel.TLabel")
phoboLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "N")

bundauLabel = ttk.Label(bundauFrame, text ="Bundau...20000VNĐ", style ="MenuLabel.TLabel")
bundauLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "N")

buncaLabel = ttk.Label(buncaFrame, text ="Bunca...20000VNĐ", style ="MenuLabel.TLabel")
buncaLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "N")

phogaLabel = ttk.Label(phogaFrame, text ="Phoga ..... 30000VNĐ", style ="MenuLabel.TLabel")
phogaLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "N")



phoboButton = ttk.Button(phoboFrame, text ="Display")
phoboButton.grid(row = 1, column = 0, padx = 10)

bundauButton = ttk.Button(bundauFrame, text ="Display")
bundauButton.grid(row = 1, column = 0, padx = 10)

buncaButton = ttk.Button(buncaFrame, text ="Display")
buncaButton.grid(row = 1, column = 0, padx = 10)

phogaButton = ttk.Button(phogaFrame, text ="Display")
phogaButton.grid(row = 1, column = 0, padx = 10)

#region Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "ORDER")
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : ")
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel')
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel")
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER")
orderButton.grid(row = 4, column = 0, sticky = "EW")
# region Display Section
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage)
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER")
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE")
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")
#----------------------------- GRID CONFIGURATIONS -------------------------------------------#

mainFrame.columnconfigure(1, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
topFrame.rowconfigure(0, weight = 1)
topFrame.columnconfigure(0, weight = 1)
topFrame.columnconfigure(1, weight = 1)
topFrame.columnconfigure(2, weight = 1)
topFrame.columnconfigure(3, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)
displayFrame.rowconfigure(0, weight = 1)

root.mainloop()

#region Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28")
s.configure('TopFrame.TFrame', background = "#4A4A48")
s.configure('DisplayFrame.TFrame', background = "#0F1110")
s.configure('OrderFrame.TFrame', background = "#B7C4CF")


s.configure('orderTotalLabel.TLabel',
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel',
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )
root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




