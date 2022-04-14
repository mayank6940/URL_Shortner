#Created BY Mayank Raj...
#Feel free to contact me 


from tkinter.font import BOLD
import pyperclip
import pyshorteners
from tkinter import *

app = Tk()
app.title("Shortner")
app.configure(bg= "#2C5364")
app.iconbitmap("D:\\Python_DEV\\New_Project\\build\\link_20914.ico")
app.geometry("480x530")
app.resizable(False, False)


#varibales
url = StringVar()
Url_address = StringVar()

#images 
head_bg = PhotoImage(file= 'D:\\Python_DEV\\New_Project\\build\\logo.png')
generate_img = PhotoImage(file='D:\\Python_DEV\\New_Project\\build\\button.png')
copy_img = PhotoImage(file = 'D:\\Python_DEV\\New_Project\\build\\copy.png')

#define logic here..

#Shorting URl 
def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    Url_address.set(url_short)
    url.set('')

#Method for copy url
def copyurl():
    url_short = Url_address.get()
    pyperclip.copy(url_short)
    url.set('')



#LOGO of the URl 
heading = Label(image= head_bg, bd= 0, bg= "#2C5364")
heading.pack(pady=20)


link_1 = Label(app, text = "Put your LINK inside", font=("Verdana", 20,BOLD), bg="#2C5364", fg = "white")
link_1.place(x = 30, y = 120)

bar = Entry(app, textvariable= url, font= "Verdana 20 bold")
bar.place(x = 30, y = 170)

#BUtton 1....
create_btn = Button(app, image= generate_img, bd = 0, bg= "#2C5364", fg  = "#2C5364", command=urlshortener)
create_btn.place(x= 150, y = 240)

Generate = Label(app, text = "Generated Url", font=("Verdana" ,20, BOLD), bg="#2C5364", fg = "white")
Generate.place(x = 30, y = 320)

bar_end = Entry(app,textvariable=Url_address, font= ("Verdana", 20, BOLD))
bar_end.place(x = 30, y = 370)


#Button 2...
copy_btn = Button(app, image= copy_img, bg= "#2C5364", fg  = "#2C5364", bd = 0 ,command=copyurl)
copy_btn.place(x = 150, y = 450)



app.mainloop()