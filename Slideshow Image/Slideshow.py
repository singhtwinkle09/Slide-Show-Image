# python library: PIL which is used to load or do function on images.
# Used: Pillow, Tkinder , 
# Itertools->cycle(used for help  object iterator)
# Time Module-> sleep function: it will stop program for few second.


from itertools import cycle
from PIL import Image, ImagesTk

import time
import tkinter as tk

root=tk.Tk
root.title("Image SlideShow")

# List of Image Path

image_paths = [
   r"Slideshow Image/Images/9600_2_2_06.jpg",
   r"Slideshow Image/Images/40738.jpg",
   r"Slideshow Image/Images/pdfi_qi6v_230613.jpg", 
]

# Resize the images to 1080x1080

image_size=(1080,1080)
images=[Image.open(path).result(image_size) for path in image_paths]
photo_images=[ImagesTk.photoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)
slideshow = cycle(photo_images) 

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root,text='play slideshow', command=start_slideshow)
play_button.pack()

root.mainloop()


         

                




