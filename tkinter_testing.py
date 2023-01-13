from tkinter import *

#makes window
root = Tk()

#Creating label widget
myLabel = Label(root, text="Hello world! How are you?")
myLabel1 = Label(root, text="My name is Josh Bellingham")
myLabel2 = Label(root, text="                   ")
#.pack just shoves it in to the first avaiilable slot on the screen
#.grid uses a grid system, starting at 0
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel1.grid(row=2, column=5)

#Can also be done in one line
myLabel3 = Label(root, text="This line of code is going to be too long and make my linter mad...").grid(row=3, column=6)

#Making buttons
#buttons have states (ie disabled)
myButton = Button(root, text="click me", padx=50, pady=50)
myButton.grid(row=3, column=6)
#making a loop to keep the program running until the loop is broken
root.mainloop()
