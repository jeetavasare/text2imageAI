import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style
from tkinter import filedialog
import os, random

# create the main window
root = tk.Tk()
root.title("Image Generator")
# root.geometry("700x500")
# root.geometry("1820x1000")
root.geometry("1270x720")
root.config(bg="white")
root.resizable(False, False)
style = Style(theme="sandstone")

img_data = None
hasGenerated = False

def download_image(img_data):
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("PNG files", "*.png"),("JPG files", "*.jpg"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'wb') as f:
            f.write(current_img_data)
    
    os.system(file_path)

def modify_category(category):
    word_lists = {
        "Educational": ["quantum", "atoms"],
        "Flower": ["render", "amoled", "amoled", "neon"],
        "Art": ["abstract", "painting", "colors", "creative"],
        "Music": ["abstract", "waveform", "colors", "creative"],
        "Background": ["abstract", "painting", "texture", "creative", "futuristic"],
        "Vehicles": ["car cool", "cool",],
        # Add more categories and corresponding word lists as needed
    }

    if category in word_lists:
        random_word = random.choice(word_lists[category])
        print(f"{category} {random_word}" )
        return f"{category} {random_word}"     

# define a function to retrieve and display an image based on the selected category
def display_image(category):
    # make a request to the Unsplash API to get a random image
    global hasGenerated
    category = modify_category(category)
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=jSBZ852ubtyUe4ubC0_hp9xgn0KI489R9e3T4U-bC34"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    # photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
    label.config(image=photo)
    label.image = photo
    global current_img_data
    current_img_data = img_data
    hasGenerated = True
    enable_button()

# function to enable/disable the "Generate Image" button
def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() != "Choose Category" else "disabled")
    download_button.config(state="normal" if hasGenerated else "disabled")

# create the GUI elements
def create_gui():
    global category_var, generate_button, label, download_button

    # create a dropdown menu for selecting the category
    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Educational", "Flower", "Background", "Music", "Art", "Vehicles"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=30)
    

    # create a button for generating the image
    generate_button = ttk.Button(text="Generate Image", state="disabled", command=lambda: display_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    
    download_button = ttk.Button(text="Download Image", state="disabled", command=lambda: download_image(img_data))
    download_button.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # make the columns/rows expandable
    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    
    root.mainloop()

if __name__ == '__main__':
    create_gui()