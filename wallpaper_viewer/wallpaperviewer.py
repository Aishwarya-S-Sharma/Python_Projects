from tkinter import *
from PIL import ImageTk,Image
import os

def rotate_img():
    global counter
    img_label.config(image=img_arr[counter%len(img_arr)])
    counter+=1
counter=1

root=Tk()
root.title('Wallpaper Viewer')

root.geometry('250x400')
root.config(background='black')

text_label=Label(root,text='Wallpaper Viewer',fg='white',bg='black')
text_label.pack()
text_label.config(font=('Georgia',20))

files=os.listdir('wallpapers')

img_arr=[]
for file in files:
    img=Image.open(os.path.join('wallpapers',file))
    resized_img=img.resize((200,250))
    img_arr.append(ImageTk.PhotoImage(resized_img))

img_label=Label(root,image=img_arr[0])
img_label.pack()

next_btn=Button(root,text='Next',bg='white',fg='black',width=24,height=2,command=rotate_img)
next_btn.pack(pady=(10,20))
next_btn.config(font=('Georgia',10))
root.mainloop()