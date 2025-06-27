from itertools import cycle       # photo list ko bar bar repeat krne ke liye
from PIL import Image, ImageTk    # Image ko open krne aur GUI dikhane ke liye 
import time            # iska use krenge image ke time ko hold krne ke liye 
import tkinter as tk   #  GUI kon bnane ke liye 

root = tk.Tk()      # main tkinter window
root.title("Image Slider Viewer") # window ka tiltle

# list of Image Path
image_paths = [
    r"Project Python/Image Slider/image/2073.jpg",
    r"Project Python/Image Slider/image/e1f9cdafbc663b0442fb2404c752d4fd.jpg",
    r"Project Python/Image Slider/image/kunda.jpg"
]

# Resize the image to 1080x1080

image_size = (1080,1080) # ye set krenga ki image hme isi size ka chahiye 
images= [Image.open(path).resize(image_size) for path in image_paths]  # hr path ki image ko resize kr dega 

photo_images = [ImageTk.PhotoImage(image) for image in images]  # tkinter format me change kiya 

label = tk.Label(root)  # ek place bnaya jha image dikhai jaye
label.pack()   # label ko GUI me add kiya


# Image ki ek-ek krke update aur show krne wale function
def update_image():
    for photo_image in photo_images:  # hr image ko lebel pr show krna 
        label.config(image=photo_image)  # current image set krna label pr
        label.update() # GUI ko update krna taki image dikhe
        time.sleep(3)  # image ko 3 sec tk hold krna 

slideshow = cycle(photo_images)  # image ko repetable format me badlna


# slidshow suru krne ke liye  function
def start_slideshow():      
    for _ in range(len(image_paths)):   # image list ki length se update krna 
        update_image()

play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)   #Play slidshow nam ka buttom bnana
play_button.pack()      # buttom ko GUI me add krna 

root.mainloop()         # main GUI loop jisme window open and responsive rhe