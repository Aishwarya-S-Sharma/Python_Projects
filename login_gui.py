from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def login_handle():
    email=email_input.get()
    password=password_input.get()
    
    if email=='aishu@gmail.com' and password=='1235':
        messagebox.showinfo('Yayy','Login Successful')
    else:
        messagebox.showerror('Error','Login Unsuccessfull')
root=Tk()

root.title('Login Form')

root.iconbitmap('login.ico')

root.minsize(100,100)

root.geometry('350x500')

root.configure(background='#0095BD')

img=Image.open('br3.jpg')
resized_img=img.resize((50,50))
img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))

text_label=Label(root,text='Bliss n Bloom',fg='white',bg='#0095BD')
text_label.pack()
text_label.config(font=('verdana',20))

email_label=Label(root,text='Enter email',fg='white',bg='#0095BD')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input=Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label=Label(root,text='Enter password',fg='white',bg='#0095BD')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input=Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn=Button(root,text='Login',bg='white',fg='black',width=20,height=2,command=login_handle)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))



root.mainloop()
