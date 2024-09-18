import webbrowser
from tkinter import *

root = Tk( )
root.title('Abrir Browser')
root.geometry('300x200')

def youtube():
  webbrowser.open('https://www.youtube.com/')
  
mydio = Button(root, text='Abrir o YT', command=youtube).pack(pady=20)
root.mainloop()