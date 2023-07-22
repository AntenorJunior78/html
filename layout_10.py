
# # Geo-Resistivity-meter
# Hardware and software repository for a geophysical instrument
# 
from tkinter import*
from tkinter.ttk import *
from tkinter import ttk  
from PIL import Image, ImageTk
import main as ni
from PIL import Image, ImageTk
import customtkinter
import time
import pandas as pd



class janelaLogin():
    def __init__(self):
        self.root = Tk()
        self.root.title('Geo-Resistivity-Meter')
        width_of_window = 500
        height_of_window = 250
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.root.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        
        #self.root.overrideredirect(1)
        
        icon = PhotoImage(file="fig/energia64.png")
        self.root.iconphoto(True, icon)
        
        s = Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
        progress=Progressbar(self.root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)
        
        def EXT():
            self.root.destroy()
            
        def new_win():
            ni.screen_config()
            
            
        def bar():
            l4=Label(self.root,text='Loading...')
            lst4=('Calibri (Body)',10)
            l4.config(font=lst4)
            l4.place(x=18,y=210)
            import time
            r=0
            for i in range(100):
                progress['value']=r
                self.root.update_idletasks()
                time.sleep(0.03)
                r=r+1
            
            EXT()
            new_win()
        
        progress.place(x=0,y=235)
        a='#249794'
        frame1 = Frame(self.root,width=510,height=241).place(x=0,y=0)  #249794
        
        home_image = ImageTk.PhotoImage(Image.open("fig/logo1.png"))
        Label(frame1, image=home_image).grid(row=1,columnspan=1)
        
        
        
        b1=Button(self.root,text='Iniciar',command=bar)
        b1.place(x=158,y=198,width=100,height=42)
        b2=Button(self.root,text='Fechar',command=EXT)
        b2.place(x=262,y=198,width=100,height=42)
        

        self.root.mainloop()
        
janelaLogin()






