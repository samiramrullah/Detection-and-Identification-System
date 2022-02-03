# importing libraries
from tkinter import *
from PIL import Image, ImageTk
from FaceDetection import Detection
from Number_plate import Car
import face_recognition


class Detection_System:
    def __init__(self, root):
        self.root = root;
        self.root.title("Detection System")
        self.root.geometry("1600x900+0+0")

        top_image = Image.open(r"top.jpg")
        top_image = top_image.resize((1600, 150), Image.ANTIALIAS)  # convert high level image to low level image
        self.top = ImageTk.PhotoImage(top_image)  # convering with image toolkit

        top_label = Label(self.root, image=self.top, bd=4, relief=RIDGE)
        top_label.place(x=0, y=0, width=1600, height=150)

        ### Settling logo
        logo = Image.open(r"logo.jpg")
        logo = logo.resize((150, 150), Image.ANTIALIAS)
        self.logo1 = ImageTk.PhotoImage(logo)

        logo = Label(self.root, image=self.logo1, bd=4, relief=RIDGE)
        logo.place(x=0, y=0, width=170, height=150)

        ##Title##
        title = Label(self.root, text="Detection and Identification System", font=("new times roman", 40, "bold"), fg="black", bg="brown")
        title.place(x=0, y=151, width=1600, height=60)

        ##Main Frame###
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=210, width=1600, height=700)
        # Lebel inside frame###
        menu = Label(main_frame, text="MENU", font=("new times roman", 20, "bold"), fg="black", bg="brown")
        menu.place(x=0, y=0, width=200)
        ##Button frame for different buttons##
        frame = Frame(main_frame, bd=3, relief=RIDGE)
        frame.place(x=0, y=30, width=200, height=220)
        ## All buttons ###
        customer_button = Button(frame, text="Face Detection ", command=self.cust_details, width=15,
                                 font=("new times roman", 15, "bold"), fg="black", bg="white")
        customer_button.grid(row=0, column=0, pady=1)
        Room_button = Button(frame, text="Car Number Plate Detection", command=Car, width=15, font=("new times roman", 15, "bold"),
                             fg="black", bg="white")
        Room_button.grid(row=1, column=0, pady=1)


        # LEFT MAIN IMAGE###
        left_image = Image.open("main.jpg")
        left_image = left_image.resize((1400, 600), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(left_image)

        lbl_left = Label(self.root, image=self.img, bd=4, relief=RIDGE)
        lbl_left.place(x=200, y=212, width=1400, height=600)

        ###DOWN 1##
        down = Image.open(r"D:\TRY\Hotel Management\down1.jpg")
        down = down.resize((150, 150), Image.ANTIALIAS)
        self.down = ImageTk.PhotoImage(down)

        down = Label(self.root, image=self.down, bd=4, relief=RIDGE)
        down.place(x=0, y=463, width=205, height=150)
        ##DOWN 2##
        down2 = Image.open(r"D:\TRY\Hotel Management\down2.jpg")
        down2 = down2.resize((150, 150), Image.ANTIALIAS)
        self.down2 = ImageTk.PhotoImage(down2)

        down2 = Label(self.root, image=self.down2, bd=4, relief=RIDGE)
        down2.place(x=0, y=618, width=205, height=150)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.cust = Detection(self.new_window)

    def CarClass(self):
        self.new_window1 = Toplevel(self.root)
        self.new = Car(self.new_window1)


# driver Program
if __name__ == '__main__':
    root = Tk()
    obj = Detection_System(root)
    root.mainloop()
