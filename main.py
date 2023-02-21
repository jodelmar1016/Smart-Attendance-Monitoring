from tkinter import *
from tkinter import messagebox
import cv2
import os
from PIL import Image, ImageTk
from datetime import datetime
from attendance import recordAttendance
from logo import addLogo

root = Tk()
root.title("ATTENDANCE MONITORING SYSTEM")
root.geometry('600x300')
root.resizable(False, False)
root.iconbitmap('assets/logo.ico')

# -----------------------------------------------------
# Functions
def openCamera():
    if len(name_input.get())==0:
        messagebox.showerror("Error", "Please input name")
        return
    try:
        int(name_input.get())
        messagebox.showerror("Error", "Please enter a valid name!")
        return
    except:
        path = "./images/"
        registered_names = []
        name_inp=name_input.get().upper()

        names = os.listdir(path)
        for name in names:
            name_path = path + name
            registered_names.append(os.path.splitext(os.path.basename(name_path))[0].upper())

        if name_inp not in registered_names:
            video = cv2.VideoCapture(0)
            while True:
                ret, frame = video.read()

                addLogo(frame)
                cv2.imshow("Camera", frame)

                if cv2.waitKey(1) & 0xFF == ord('c'):
                    cv2.imwrite("images/"+ name_input.get() +".jpg",frame)
                    output_message.configure(text="Successfully Registered")
                    bot_item_reg.pack_forget()
                    bot_item_attendance.pack()
                    break
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    bot_item_attendance.pack_forget()
                    bot_item_reg.pack()
                    break

            video.release()
            cv2.destroyAllWindows()
        else:
            messagebox.showinfo("Message", "Already Registered!")

def register():
    bot_item_reg.pack()
    bot_item_attendance.pack_forget()
    print("Register")

def takeAttendance():
    output_message.configure(text="")
    bot_item_reg.pack_forget()
    bot_item_attendance.pack_forget()

    res = recordAttendance()

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H%M%S")
    f = open(dt_string+".txt", "w")

    for i in res:
        f.write(i[0]+"\t"+i[1]+"\n")
    f.close()

# -----------------------------------------------------
# Containers
container = Frame(root)
top = Frame(root)
buttons = Frame(root)
bot = Frame(root)

bot_item_reg = Frame(bot)
bot_item_attendance = Frame(bot)
video_container = Frame(bot)

container.pack()
top.pack(pady=10)
buttons.pack(pady=10)
bot.pack(pady=10)

# -----------------------------------------------------
# Top
img = ImageTk.PhotoImage(Image.open("assets/crop_logo-removebg-preview.png").resize((40,60), Image.Resampling.LANCZOS))
title = Label(top, text="ATTENDANCE MONITORING SYSTEM", font=("Arial", 20))
img_label = Label(top, image = img)

title.grid(row=0, column=1)
img_label.grid(row=0, column=0, padx=10)
# -----------------------------------------------------

# Buttons
reg = Button(buttons, text="Register", font=("Arial", 10), width=20, height=3, command=register, background='#000', foreground='#fff')
take_attendance = Button(buttons, text="Take Attendance", font=("Arial", 10), width=20, height=3, command=takeAttendance, background='#000', foreground='#fff')

reg.grid(row=0,column=0, padx=30, pady=10)
take_attendance.grid(row=0,column=1, padx=30, pady=10)
# -----------------------------------------------------

# Bot
name_label = Label(bot_item_reg, text="Name:", font=("Arial", 16))
name_input = Entry(bot_item_reg, font=("Arial", 16))
open_camera = Button(bot_item_reg, text="Open Camera", width=15, height=2, command=openCamera, background='#000', foreground='#fff')
output_message = Label(bot_item_attendance, text="", font=("Arial", 20))

name_label.grid(row=0, column=0, padx=10, pady=10)
name_input.grid(row=0, column=1)
open_camera.grid(row=1, column=0, columnspan=2)
output_message.grid(row=0, column=0, pady=10)
# -----------------------------------------------------

root.mainloop()