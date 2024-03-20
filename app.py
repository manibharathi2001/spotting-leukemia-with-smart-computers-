import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import traceback
from tkinter import Tk, Canvas, PhotoImage

import numpy
#load the trained model to classify sign
from keras.models import load_model
model = load_model("D://project//ALL-Subtype-Classification//Models//model1.h5")

#dictionary to label all traffic signs class.
classes = { 1:'Benign Stage',
            2:'Early Stage', 
            3:'Pre Stage', 
            4:'Pro Stage'}

#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Spotting Leukemia With Smart computers Using')
top.configure(background='#8e44ad')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

from PIL import Image
import numpy as np

def classify(file_path):
    try:
        image = Image.open(file_path)
        image = image.resize((224, 224))  # Resize to match the model's input shape
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        pred = model.predict(image)
        pred_class = np.argmax(pred)
        sign = classes[pred_class + 1]
        print(f"Predicted Sign: {sign}")
        label.configure(foreground='#011638', text=sign)
    except Exception as e:
        print(f"Error: {e}")
        print("Image classification failed.")
        traceback.print_exc()


# Example usage:
# classify('image.jpg', model, classes, label_widget)


def show_classify_button(file_path):
   try:
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364198', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
    print(f"Predicted Class: {pred_class}")
    sign = classes.get(pred_class, "Unknown Class")

   except:
      print("Run")

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        print("cannot upload Image")

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Spotting Leukemia (ALL)",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()


def create_gradient(canvas, x1, y1, x2, y2, color1, color2):
    """Create a gradient rectangle on the canvas."""
    canvas.create_rectangle(x1, y1, x2, y2, fill=color1, outline=color1)
    for i in range(y1, y2):
        ratio = (i - y1) / (y2 - y1)
        r = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        g = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        b = int(color1[3] * (1 - ratio) + color2[3] * ratio)
        color = f'#{r:02x}{g:02x}{b:02x}'
        canvas.create_line(x1, i, x2, i, fill=color, width=1)

top = Tk()
top.geometry('800x600')
top.title('Spotting Leukemia With Smart computer Using Deeplearning')

# Create a Canvas widget for the gradient background
canvas = Canvas(top, width=800, height=600, highlightthickness=0)
canvas.pack(fill=BOTH, expand=YES)

# Define the gradient colors
color1 = '#00000'  # Dark purple
color2 = '#ffff'  # Light blue

# Create the gradient background
create_gradient(canvas, 0, 0, 800, 600, color1, color2)

label = Label(top, background=color1, font=('arial', 15, 'bold'))
sign_image = Label(top)

def classify(file_path):
    try:
        image = Image.open(file_path)
        image = image.resize((224, 224))  # Resize to match the model's input shape
        image = np.expand_dims(image, axis=0)
        image = np.array(image)
        pred = model.predict(image)
        pred_class = np.argmax(pred)
        sign = classes[pred_class + 1]
        print(f"Predicted Sign: {sign}")
        label.configure(foreground='#011638', text=sign)
    except Exception as e:
        print(f"Error: {e}")
        print("Image classification failed.")
        traceback.print_exc()

def show_classify_button(file_path):
    try:
        classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5,
                            bg='#3498db', fg='white', font=('arial', 12, 'bold'), borderwidth=3, relief='raised')
        classify_b.place(relx=0.79, rely=0.46)
        print(f"Predicted Class: {pred_class}")
        sign = classes.get(pred_class, "Unknown Class")
    except:
        print("Run")

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        print("cannot upload Image")

upload = Button(top, text="Upload an image", command=upload_image, padx=10, pady=5,
                bg='#2ecc71', fg='white', font=('arial', 12, 'bold'), borderwidth=3, relief='raised')
upload.pack(side=BOTTOM, pady=20)
sign_image.pack(side=BOTTOM, expand=YES)
label.pack(side=BOTTOM, expand=YES)
heading = Label(top, text="Spotting Leukemia (ALL)", pady=20, font=('arial', 20, 'bold'))
heading.configure(background=color1, foreground='#364156')
heading.pack()

top.mainloop()