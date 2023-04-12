import tkinter as tk
from tkinter import ttk
import os
import sys
from PIL import Image

root = tk.Tk()

# Title
root.title("Stickermaker")

# Window Size
window_width = 600
window_height = 380
# Centering screen example
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# Resizable option
root.resizable(True, True)

# Min-Max Size for windows:
# root.minsize(min_width, min_height)
# root.maxsize(max_width, max_height)

# Setting window size
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# Setting default icon
# root.iconbitmap(".icopath")

message = ttk.Label(root, text="Clique aqui se tiver coragem >:)")
message.pack()


# Stickermaker function & button

def stickermaker():
    os.chdir(sys.path[0])
#    print(os.getcwd())
#    print(os.listdir(os.getcwd()))


    image_types = [".jpeg", ".jpg", ".png"]
    converted_folder = "converted"


    if not os.path.exists(converted_folder):
        os.mkdir(converted_folder)


    for sticker in os.listdir(os.getcwd()):
        if sticker.endswith(tuple(image_types)):
            with Image.open(sticker) as image_to_convert:
                width, height = image_to_convert.size
                if width == height:
                    image_to_convert.resize((512, 512)).save(f'{converted_folder}/{sticker}+CONVERTED.PNG')
                elif width > height:
                    image_to_convert.resize((512, int(height/(width/512)))).save(f'{converted_folder}/{sticker}+CONVERTED.PNG')
                elif height > width:
                    image_to_convert.resize((int(width/(height/512)), 512)).save(f'{converted_folder}/{sticker}CONVERTED.PNG')


stickermakerbutton = ttk.Button(root, text="Convert", command=stickermaker)
stickermakerbutton.place(x=260, y=100)


root.mainloop()
